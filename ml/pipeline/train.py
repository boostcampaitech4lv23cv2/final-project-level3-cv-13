import argparse
import glob
import json
import multiprocessing
import os
import random
import re
from importlib import import_module
from pathlib import Path
import yaml
from tqdm import tqdm
import torch.onnx
from datetime import datetime
from shutil import copyfile

import matplotlib.pyplot as plt
import numpy as np
import torch
from torch.optim.lr_scheduler import StepLR, CosineAnnealingLR
from torch.utils.data import DataLoader, ConcatDataset
# from torch.utils.tensorboard import SummaryWriter
import albumentations as A
from albumentations.pytorch.transforms import ToTensorV2
from torchvision.transforms import Resize,ToTensor

from dataloader import Fish_Dataset
from loss import create_criterion

import wandb
import os.path as osp

# 저장경로 및 방식
# dataset & dataloader 수정
# optimizer config 작성

def seed_everything(seed):
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)  # if use multi-GPU
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    np.random.seed(seed)
    random.seed(seed)


def get_lr(optimizer):
    for param_group in optimizer.param_groups:
        return param_group['lr']


def grid_image(np_images, gts, preds, n=16, shuffle=False):
    batch_size = np_images.shape[0]
    assert n <= batch_size

    choices = random.choices(range(batch_size), k=n) if shuffle else list(range(n))
    figure = plt.figure(figsize=(12, 18 + 2))  # cautions: hardcoded, 이미지 크기에 따라 figsize 를 조정해야 할 수 있습니다. T.T
    plt.subplots_adjust(top=0.8)  # cautions: hardcoded, 이미지 크기에 따라 top 를 조정해야 할 수 있습니다. T.T
    n_grid = int(np.ceil(n ** 0.5))
    tasks = ["fish"]
    for idx, choice in enumerate(choices):
        gt = gts[choice].item()
        pred = preds[choice].item()
        image = np_images[choice]
        # gt_decoded_labels = Fish_Dataset.decode_multi_class(gt) # gt
        # pred_decoded_labels = Fish_Dataset.decode_multi_class(pred) # gt
        title = "\n".join([
            f"{tasks} - gt: {gt}, pred: {pred}"
        ])

        plt.subplot(n_grid, n_grid, idx + 1, title=title)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)

        plt.imshow((image*255).astype(np.uint8), cmap=plt.cm.binary)

    return figure

# output 폴더 생성하는 함수인데 약간 망가진 듯 작동 안해서 고정으로 바꿔놨음
def increment_path(path,  exist_ok=False):
    """ Automatically increment path, i.e. runs/exp --> runs/exp0, runs/exp1 etc.

    Args:
        path (str or pathlib.Path): f"{model_dir}/{args.name}".
        exist_ok (bool): whether increment path (increment if False).
    """
    path = Path(path)
    if path.exists() == False:
        os.mkdir(path)
        return str(path)
    else:
        dirs = glob.glob(f"{path}*")
        matches = [re.search(rf"%s(\d+)" % path.stem, d) for d in dirs]
        i = [int(m.groups()[0]) for m in matches if m]
        n = max(i) + 1 if i else 2 
        os.mkdir(f"{path}_exp{n}")
        return f"{path}_exp{n}"


# [START storage_upload_file]
from google.cloud import storage


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        f"File {source_file_name} uploaded to {destination_blob_name}."
    )

# #Function to Convert to ONNX 
# def Convert_ONNX(model, output_path): 

#     # set the model to inference mode 
#     model.eval() 

#     # Let's create a dummy input tensor  
#     dummy_input = torch.randn(1, 384, requires_grad=True)  

#     # Export the model   
#     torch.onnx.export(model,         # model being run 
#          dummy_input,       # model input (or a tuple for multiple inputs) 
#          output_path,       # where to save the model  
#          export_params=True,  # store the trained parameter weights inside the model file 
#          opset_version=10,    # the ONNX version to export the model to 
#          do_constant_folding=True,  # whether to execute constant folding for optimization 
#          input_names = ['modelInput'],   # the model's input names 
#          output_names = ['modelOutput'], # the model's output names 
#          dynamic_axes={'modelInput' : {0 : 'batch_size'},    # variable length axes 
#                                 'modelOutput' : {0 : 'batch_size'}}) 
#     print(" ") 
#     print('Model has been converted to ONNX')


def train(data_dir, model_dir, args):
    seed_everything(args.seed)

    global save_dir
    save_dir = increment_path(os.path.join(model_dir, f"{config.model}_{config.epochs}_{config.batch_size}_{config.optimizer}_{config.lr}"))
    

    # -- settings
    use_cuda = torch.cuda.is_available()
    device = torch.device("cuda" if use_cuda else "cpu")
    print(f'Currently using {device}...')
    print(f'Currently using {device}...')

    # -- dataset
    transform = A.Compose([
            A.Resize(*config.resize),
            #A.Normalize(mean=mean, std=std, max_pixel_value=255.0, p=1.0),
            ToTensorV2(p=1.0)
            ])

    train_dataset_module = getattr(import_module("dataloader"), args.dataset)
    train_dataset = train_dataset_module(
        img_dir = data_dir,
        ann_dir = osp.join(config.ann_dir, 'train.csv'),
        transform = transform,
    )
    num_classes = train_dataset.num_classes  # 18

    val_dataset_module = getattr(import_module("dataloader"), args.dataset)
    val_dataset = val_dataset_module(
        img_dir = data_dir,
        ann_dir = osp.join(config.ann_dir, 'valid.csv'),
        transform = transform,
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
    )
        
    val_loader = DataLoader(
        val_dataset,
        batch_size=args.valid_batch_size,
        num_workers=multiprocessing.cpu_count() // 2,
        shuffle=False,
        pin_memory=use_cuda,
        drop_last=True,
    )

    # -- model
    model_module = getattr(import_module("model"), args.model)  # default: BaseModel
    model = model_module(
        num_classes=num_classes
    ).to(device)
    # model = torch.nn.DataParallel(model)

    # -- loss & metric
    criterion = create_criterion(args.criterion)  # default: cross_entropy
    # optimizer 작성도 하면 좋을듯?
    opt_module = getattr(import_module("torch.optim"), args.optimizer)  # default: SGD
    optimizer = opt_module(
        filter(lambda p: p.requires_grad, model.parameters()),
        lr=args.lr,
        weight_decay=5e-4 # weight_decay 너무 튀지 않게??
    )
    
    # scheduler config 작성필요
    #scheduler = StepLR(optimizer, args.lr_decay_step, gamma=0.5)
    scheduler = CosineAnnealingLR(optimizer, 5, 0.00001)

    # -- logging
    #logger = SummaryWriter(log_dir=save_dir)
    # json 파일 생성하는 건데 필요없을 것 같아서 지움
    '''with open(os.path.join(save_dir, 'config.json'), 'w', encoding='utf-8') as f:
        json.dump(vars(args), f, ensure_ascii=False, indent=4)'''

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
        
        for idx, (inputs, labels) in enumerate(train_loader):
            # print(inputs,labels)
            # inputs, labels = train_batch
            # print(inputs)
            # print(type(labels))
            #inputs = torch.stack(inputs)       
            #labels = torch.stack(labels)
            inputs = inputs.to(device, dtype=torch.float32)
            labels = labels.to(device)

            optimizer.zero_grad()

            outs = model(inputs)
            preds = torch.argmax(outs, dim=-1)
            loss = criterion(outs, labels)
            # print(outs.size())
            # print(labels.size())


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
                #wandb.log({"Train/loss": {train_loss, epoch * len(train_loader) + idx},"Train/accuracy": {train_acc, epoch * len(train_loader) + idx}, 'epoch': epoch})
                #wandb.log({"Train/accuracy": {train_acc, epoch * len(train_loader) + idx}})

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
                # print(outs.size())
                # print(labels.size())
                loss_item = criterion(outs, labels).item()
                acc_item = (labels == preds).sum().item()
                val_loss_items.append(loss_item)
                val_acc_items.append(acc_item)

                if figure is None:
                    inputs_np = torch.clone(inputs).detach().cpu().permute(0, 2, 3, 1).numpy()
                    # inputs_np = val_dataset_module.denormalize_image(inputs_np*255, val_dataset.mean, val_dataset.std)
                    figure = grid_image(
                        inputs_np, labels, preds, n=16, shuffle= False
                    )

            val_loss = np.sum(val_loss_items) / len(val_loader)
            val_acc = np.sum(val_acc_items) / len(val_dataset)
            best_val_loss = min(best_val_loss, val_loss)
            dummy_input = torch.randn(1, 3, 384, 384).to(device)
            dummy_output = model(dummy_input)
            if val_acc > best_val_acc:
                early_stop = 0
                print(f"New best model for val accuracy : {val_acc:4.2%}! saving the best model..")
                torch.save(model.state_dict(), f"{save_dir}/{config.model}_best_{epoch}epoch_{val_acc:6.4}.pth")
                torch.onnx.export(model, dummy_input, f"{save_dir}/{config.model}_best_{val_acc:6.4}.onnx", export_params=True,
                      input_names = ['input'],
                      output_names = ['output'],
                      dynamic_axes={'input' : {0 : 'batch_size'},
                                'output' : {0 : 'batch_size'}})
                best_val_acc = val_acc
            torch.save(model.state_dict(), f"{save_dir}/{config.model}_last_{epoch}epoch_{val_acc:6.4}.pth")
            torch.onnx.export(model, dummy_input, f"{save_dir}/{config.model}_last_{val_acc:6.4}.onnx", export_params=True,
                      input_names = ['input'],
                      output_names = ['output'],
                      dynamic_axes={'input' : {0 : 'batch_size'},
                                'output' : {0 : 'batch_size'}})
            # 저장경로 짜는법 다시 작성해야함
            print(
                f"[Val] acc : {val_acc:4.2%}, loss: {val_loss:4.2} || "
                f"best acc : {best_val_acc:4.2%}, best loss: {best_val_loss:4.2}"
            )

            wandb.log({"Val/loss": val_loss, "epoch": epoch, "Val/accuracy": val_acc, "results": figure})
            #wandb.log({"val_loss": val_loss,"val_acc": val_acc})
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
    
    wandb_yaml = input("설정한 yaml 파일의 절대 경로를 넣어주세요...")
    if wandb_yaml == '':
        wandb_yaml = '/opt/ml/final-project-level3-cv-13/ml/config/config.yaml'
    elif wandb_yaml[-4:] != 'yaml':
        raise TypeError('This is not yaml file')
    print(wandb_yaml)
    
    # 🐝 initialise a wandb run
    wandb.init(
        entity='boostcamp_cv13',
        project="Final_Project",
        name='test',
        config = wandb_yaml
    )
    wandb.save(wandb_yaml)

    # Copy your config 
    config = wandb.config
    parser = argparse.ArgumentParser()

    # Data and model checkpoints directories
    parser.add_argument('--seed', type=int, default=config.seed, help='random seed (default: 42)')
    parser.add_argument('--epochs', type=int, default=config.epochs, help='number of epochs to train (default: 1)')
    parser.add_argument('--dataset', type=str, default=config.dataset, help='dataset augmentation type (default: MaskBaseDataset)')
    parser.add_argument('--transform', type=str, default=config.transform, help='data augmentation type (default: Basepreprocessing)')
    parser.add_argument("--resize", nargs="+", type=list, default=config.resize, help='resize size for image when training')
    parser.add_argument('--batch_size', type=int, default=config.batch_size, help='input batch size for training (default: 64)')
    parser.add_argument('--valid_batch_size', type=int, default=config.val_batch_size, help='input batch size for validing (default: 1000)')
    parser.add_argument('--model', type=str, default=config.model, help='model type (default: BaseModel)')
    parser.add_argument('--optimizer', type=str, default=config.optimizer, help='optimizer type (default: SGD)')
    parser.add_argument('--lr', type=float, default=config.lr, help='learning rate (default: 1e-3)')
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

    upload_blob(
        bucket_name="model-registry-cv13",
        source_file_name=f"{save_dir}/{config.model}_best_{best_val_acc:6.4}.onnx",
        destination_blob_name=f"{config.model}-{best_val_acc:6.4}-{today}.onnx",
    )

    