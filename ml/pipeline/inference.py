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
import cv2

from tqdm import tqdm
import time
from shutil import copyfile
from importlib import import_module
from torch.utils.data import DataLoader
from torchvision.utils import save_image
from albumentations.augmentations.transforms import InvertImg

from albumentations.pytorch.transforms import ToTensorV2

from dataloader import Fish_Dataset
from loss import create_criterion
# from scheduler import create_scheduler

# from utils import UploadBlob
from utils import IncrementPath
from utils import GridImage
from utils import SeedEverything

@torch.no_grad()
def inference(model_dir):
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model_module = getattr(import_module("model"), 'EfficientNetB0')  # default: BaseModel
    model = model_module(
        num_classes = 12
    ).to(device)
    
    model.to(device)
    
    checkpoint = torch.load("/opt/ml/final-project-level3-cv-13/ml/output/EfficientNetB0_30_8_Adam_0.0001_exp37/fish_EfficientNetB0_best_epoch25_0.9433.pth", map_location=device)
    model.load_state_dict(checkpoint)
    model.eval()
    # print(model)
    # Let's create a dummy input tensor  
    # make dummy data
    
    with torch.no_grad():
        batch_size = 1
        file_path = '/opt/ml/data/fish/Croaker/e4694ec0d379bdec6410312bb244d42d21279403e458a25cb0e31c470c1a.jpg'
        image = cv2.imread(file_path)

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # image = np.expand_dims(image, axis=0)

        transform=A.Compose([
            A.Resize(384, 384),
            A.Normalize(),
            ToTensorV2(),
        ])
        
        image = transform(image=image)['image']
        image = image/255
        image = image.unsqueeze(0)
        image = image.to(device, dtype=torch.float32)
        # feed-forward test
        start = time.time()

        # exp = image.detach().cpu().numpy()
        # print(image)
        output = model(image)
        print(output)
        preds = torch.argmax(output, dim=1)
        preds = preds.cpu().numpy()
        print(preds)
        end = time.time()
        print(f"{end - start:.5f} sec")

    


if __name__ == "__main__":
    SeedEverything.seed_everything(2023)
    path = '/opt/ml/final-project-level3-cv-13/ml/output/EfficientNetB0_30_8_Adam_0.0001_exp37'
    yaml = osp.join(path, 'config.yaml')
    model = glob.glob(f"{path}/*best*.pth")
    inference(model_dir=model)