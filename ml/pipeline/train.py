import argparse
import glob
import json
import multiprocessing
import os
import random
import torch.onnx
import numpy as np
import torch
import albumentations as A
import os.path as osp
import wandb
import fnmatch

from tqdm import tqdm
from datetime import datetime
from shutil import copyfile
from importlib import import_module
from torch.utils.data import DataLoader

from albumentations.pytorch.transforms import ToTensorV2

from dataloader import Fish_Dataset
from loss import create_criterion
# from scheduler import create_scheduler

from utils import UploadBlob
from utils import IncrementPath
from utils import GridImage
from utils import SeedEverything

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/opt/ml/storage_key.json"

def get_lr(optimizer):
    for param_group in optimizer.param_groups:
        return param_group['lr']


def train(data_dir, model_dir, args):
    SeedEverything.seed_everything(args.seed)

    global save_dir
    save_dir = IncrementPath.increment_path(os.path.join(model_dir, f"{config.model}_{config.epochs}_{config.batch_size}_{config.optimizer}_{config.lr}_exp"))
    

    # -- settings
    use_cuda = torch.cuda.is_available()
    device = torch.device("cuda" if use_cuda else "cpu")
    print(f'Currently using {device}...')
    print(f'Currently using {device}...')

    # -- dataset
    transform_module = getattr(import_module("transforms"), args.transform)
    transform = transform_module(resize = config.resize)
    # transform = A.Compose([
    #         A.Resize(*config.resize),
    #         #A.Normalize(mean=mean, std=std, max_pixel_value=255.0, p=1.0),
    #         ToTensorV2()
    #         ])

    train_dataset_module = getattr(import_module("dataloader"), args.dataset)
    train_dataset = train_dataset_module(
        img_dir = data_dir,
        ann_dir = osp.join(config.ann_dir, 'train.csv'),
        transform = transform,
        num_classes = len(args.classes)
    )

    val_dataset_module = getattr(import_module("dataloader"), args.dataset)
    val_dataset = val_dataset_module(
        img_dir = data_dir,
        ann_dir = osp.join(config.ann_dir, 'valid.csv'),
        transform = transform,
        num_classes = len(args.classes)
    )

    # -- transform --data_set
    # transform_module = getattr(import_module("dataloader"), args.transform)
    mean=(0.548, 0.504, 0.479)
    std=(0.237, 0.247, 0.246)
    
    # train_dataset.set_transform(transform)
    # val_dataset.set_transform(transform)
    # train_set,val_set = dataset.split_dataset()

    # collate_fn needs for batch
    def collate_fn(batch):
        return tuple(zip(*batch))

    def seed_worker(worker_id):
        worker_seed = torch.initial_seed() % 2**32
        np.random.seed(worker_seed)
        random.seed(worker_seed)

    g = torch.Generator()
    g.manual_seed(args.seed)

    # # -- data_loader

    train_loader = DataLoader(
        train_dataset,
        batch_size=args.batch_size,
        num_workers=multiprocessing.cpu_count() // 2,
        # collate_fn=collate_fn,
        worker_init_fn=seed_worker,
        shuffle=True,
        pin_memory=use_cuda,
        drop_last=True,
        generator=g
    )
        
    val_loader = DataLoader(
        val_dataset,
        batch_size=args.valid_batch_size,
        num_workers=multiprocessing.cpu_count() // 2,
        shuffle=False,
        pin_memory=use_cuda,
        drop_last=True,
        generator=g
    )

    # -- model
    model_module = getattr(import_module("model"), args.model)  # default: BaseModel
    model = model_module(
        num_classes=len(args.classes)
    ).to(device)

    # -- loss & metric
    criterion = create_criterion(args.criterion, classes = len(args.classes))  # default: cross_entropy
    optimizer = getattr(import_module("optimizer"), args.optimizer)(model)  # default: SGD
    
    # scheduler
    scheduler = getattr(import_module("scheduler"), args.scheduler)
    scheduler = scheduler(optimizer)


    global best_val_acc
    best_val_acc = 0
    best_val_loss = np.inf

    early_stop = 0
    breaker = False
    early_stop_arg = args.early_stop

    for epoch in range(args.epochs):
        # train loop
        model.train()
        loss_value = 0
        matches = 0
        
        for idx, (inputs, labels) in enumerate(tqdm(train_loader, leave=True)):

            inputs = inputs.to(device, dtype=torch.float32)
            labels = labels.to(device)

            optimizer.zero_grad()

            outs = model(inputs)
            preds = torch.argmax(outs, dim=-1)
            loss = criterion(outs, labels)


            loss.backward()
            optimizer.step()

            loss_value += loss.item()
            matches += (preds == labels).sum().item()
            if (idx + 1) % args.log_interval == 0:
                train_loss = loss_value / args.log_interval
                train_acc = matches / args.batch_size / args.log_interval
                current_lr = get_lr(optimizer)
                print(
                    f"Epoch[{epoch+1}/{args.epochs}]({idx + 1}/{len(train_loader)}) || "
                    f"training loss {train_loss:4.4} || training accuracy {train_acc:4.2%} || lr {current_lr}"
                )
                wandb.log({"Train/loss": train_loss,"Train/accuracy": train_acc, 'epoch': epoch})

                loss_value = 0
                matches = 0

        scheduler.step()

        # val loop
        with torch.no_grad():
            print("Calculating validation results...")
            model.eval()
            val_loss_items = []
            val_acc_items = []
            figure = None
            for val_batch in val_loader:
                inputs, labels = val_batch
                inputs = inputs.to(device, dtype=torch.float32)
                labels = labels.to(device)

                outs = model(inputs)
                preds = torch.argmax(outs, dim=-1)

                loss_item = criterion(outs, labels).item()
                acc_item = (labels == preds).sum().item()
                val_loss_items.append(loss_item)
                val_acc_items.append(acc_item)

                if figure is None:
                    inputs_np = torch.clone(inputs).detach().cpu().permute(0, 2, 3, 1).numpy()
                    # inputs_np = val_dataset_module.denormalize_image(inputs_np*255, val_dataset.mean, val_dataset.std)
                    figure = GridImage.grid_image(
                        inputs_np, labels, preds, n=16, shuffle= False
                    )

            val_loss = np.sum(val_loss_items) / len(val_loader)
            val_acc = np.sum(val_acc_items) / len(val_dataset)
            best_val_loss = min(best_val_loss, val_loss)
            dummy_input = torch.randn(1, 3, 384, 384).to(device)
            if val_acc > best_val_acc:
                early_stop = 0

                [os.remove(f) for f in glob.glob(f"{save_dir}/*_best_*")]
                print(f"New best model for val accuracy : {val_acc:4.2%}! saving the best model..")
                torch.save(model.state_dict(), f"{save_dir}/{config.model}_best_{epoch}epoch_{val_acc:6.4}.pth")
                torch.onnx.export(model, dummy_input, f"{save_dir}/{config.model}_best_{val_acc:6.4}.onnx", export_params=True,
                      input_names = ['input'],
                      output_names = ['output'],
                      dynamic_axes={'input' : {0 : 'batch_size'},
                                'output' : {0 : 'batch_size'}})
                best_val_acc = val_acc
            [os.remove(f) for f in glob.glob(f"{save_dir}/*_last_*")]
            torch.save(model.state_dict(), f"{save_dir}/{config.model}_last_{epoch}epoch_{val_acc:6.4}.pth")
            torch.onnx.export(model, dummy_input, f"{save_dir}/{config.model}_last_{val_acc:6.4}.onnx", export_params=True,
                      input_names = ['input'],
                      output_names = ['output'],
                      dynamic_axes={'input' : {0 : 'batch_size'},
                                'output' : {0 : 'batch_size'}})

            print(
                f"[Val] acc : {val_acc:4.2%}, loss: {val_loss:4.2} || "
                f"best acc : {best_val_acc:4.2%}, best loss: {best_val_loss:4.2}"
            )

            wandb.log({"Val/loss": val_loss, "epoch": epoch, "Val/accuracy": val_acc, "results": figure})

            print(f'{early_stop_arg-early_stop} Epoch left until early stopping..')                
            if val_acc <= best_val_acc:                
                if early_stop == early_stop_arg:
                    breaker = True
                    print(f'--------epoch {epoch} early stopping--------')
                    print(f'--------epoch {epoch} early stopping--------')                                       
                    break
            early_stop += 1

        if breaker == True:
            break        

            # Optional
            wandb.watch(model)

if __name__ == '__main__':
    wandb.login()
    # 🐝 initialise a wandb run
    runs=wandb.Api().runs(path="boostcamp_cv13/Final_Project",order="created_at")
    
    # yaml file 경로
    wandb_yaml = '/opt/ml/final-project-level3-cv-13/ml/config/config.yaml'

    wandb.init(
        entity='boostcamp_cv13',
        project="Final_Project",
        config = wandb_yaml
    )
    this_run_name=f"{wandb.config.model}_{wandb.config.epochs}_{wandb.config.batch_size}_{wandb.config.optimizer}_{wandb.config.lr}"
    wandb.run.name=this_run_name
    wandb.save(wandb_yaml)

    # Copy your config 
    config = wandb.config
    parser = argparse.ArgumentParser()

    # Data and model checkpoints directories
    parser.add_argument('--seed', type=int, default=config.seed, help='random seed (default: 42)')
    parser.add_argument('--classes', type=list, default=config.classes, help='category id')
    parser.add_argument('--epochs', type=int, default=config.epochs, help='number of epochs to train (default: 1)')
    parser.add_argument('--dataset', type=str, default=config.dataset, help='dataset augmentation type (default: MaskBaseDataset)')
    parser.add_argument('--transform', type=str, default=config.transform, help='data augmentation type (default: Basepreprocessing)')
    parser.add_argument("--resize", nargs="+", type=list, default=config.resize, help='resize size for image when training')
    parser.add_argument('--batch_size', type=int, default=config.batch_size, help='input batch size for training (default: 64)')
    parser.add_argument('--valid_batch_size', type=int, default=config.val_batch_size, help='input batch size for validing (default: 1000)')
    parser.add_argument('--model', type=str, default=config.model, help='model type (default: BaseModel)')
    parser.add_argument('--optimizer', type=str, default=config.optimizer, help='optimizer type (default: SGD)')
    parser.add_argument('--lr', type=float, default=config.lr, help='learning rate (default: 1e-3)')
    parser.add_argument('--scheduler', type=str, default=config.scheduler, help='scheduler (default: lambda_lr')
    parser.add_argument('--val_ratio', type=float, default=config.val_ratio, help='ratio for validaton (default: 0.2)')
    parser.add_argument('--criterion', type=str, default=config.criterion, help='criterion type (default: cross_entropy)')
    parser.add_argument('--lr_decay_step', type=int, default=20, help='learning rate scheduler deacy step (default: 20)')
    parser.add_argument('--log_interval', type=int, default=config.log_interval, help='how many batches to wait before logging training status')
    parser.add_argument('--name', default=config.output_folder_name, help='model save at {SM_MODEL_DIR}/{name}')

    # Container environment
    parser.add_argument('--data_dir', type=str, default=os.environ.get('SM_CHANNEL_TRAIN', config.data_dir))
    parser.add_argument('--model_dir', type=str, default=os.environ.get('SM_MODEL_DIR', config.model_dir))
    parser.add_argument('--early_stop', type=int, default=config.early_stop, help='number of early_stop (default : 10')

    args = parser.parse_args()
    print(args)

    data_dir = args.data_dir
    model_dir = args.model_dir

    train(data_dir, model_dir, args)
    wandb.finish()
    
    copyfile(wandb_yaml, f"{save_dir}/config.yaml")

    today = datetime.today().strftime('%Y%m%d')

    UploadBlob.upload_blob(
        bucket_name="model-registry-cv13",
        source_file_name=f"{save_dir}/{config.model}_best_{best_val_acc:6.4}.onnx",
        destination_blob_name=f"{config.model}-{best_val_acc:6.4}-{today}.onnx",
    )

    