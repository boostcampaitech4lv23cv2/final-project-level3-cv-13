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

from utils import UploadBlob
from utils import IncrementPath
from utils import GridImage
from utils import SeedEverything

def inference(model_dir):
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model_module = getattr(import_module("model"), 'EfficientNetB7')  # default: BaseModel
    model = model_module(
        num_classes = 12
    ).to(device)
    
    model.to(device)
    
    checkpoint = torch.load("/opt/ml/final-project-level3-cv-13/ml/output/EfficientNetB7_10_16_Adam_0.0001_exp4/fish_EfficientNetB7_best_epoch8_0.9727.pth", map_location=device)
    model.load_state_dict(checkpoint)
    model.eval()

    # Let's create a dummy input tensor  
    # make dummy data
    

    batch_size = 1
    file_path = '/opt/ml/data/fish/Croaker/0aadb8e6d39db834124c877bad828f2007e84a5006d4599788f5cb96b481.jpg'
    image = cv2.imread(file_path)
    image = np.expand_dims(image, axis=0)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    transform=A.Compose([
        A.Resize(384, 384),
        A.Normalize(),
        ToTensorV2(),
    ])

    image = transform(image=image)['image']
    image = image.unsqueeze(0)
    image = image.to(device, dtype=torch.float32)
    # feed-forward test
    start = time.time()
    output = model(image)
    preds = torch.argmax(output, dim=-1)
    end = time.time()
    print(f"{end - start:.5f} sec")

    


if __name__ == "__main__":
    path = '/opt/ml/final-project-level3-cv-13/ml/output/EfficientNetB7_10_16_Adam_0.0001_exp4'
    yaml = osp.join(path, 'config.yaml')
    model = glob.glob(f"{path}/*best*.pth")
    inference(model_dir=model)