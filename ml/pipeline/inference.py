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

def inference(data_dir, model_dir, args):
    SeedEverything.seed_everything(args.seed)

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
    # model input size에 맞게 b c h w 순으로 파라미터 설정
    x = torch.rand(batch_size, 3, 384, 384, requires_grad=True).to(device)
    # feed-forward test
    output = model(x)

    transform=A.Compose([
        # A.Resize(*HyperParameter.RESIZE),
        A.Normalize(),
        ToTensorV2(),
    ])

if __name__ == "__main__":
    path = input("inference를 실행할 output 폴더의 절대 경로를 적어주세요.\n")
    yaml = osp.join(path, 'config.yaml')
    model = glob.glob(f"{path}/*best*.pth")
    inference(model_dir=model)