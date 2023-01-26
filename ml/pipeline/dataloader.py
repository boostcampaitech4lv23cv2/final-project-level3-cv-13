import torch.nn as nn
import albumentations
import pandas as pd
import torch
from torch.utils.data import Dataset
from torchvision import datasets
from torch.utils.data.sampler import SubsetRandomSampler
import cv2
import numpy as np
import json
import os.path as osp
import albumentations as A
import albumentations.pytorch
from albumentations.pytorch.transforms import ToTensorV2
from PIL import Image
from torchvision.transforms import Resize,ToTensor, Normalize, Compose, CenterCrop, ColorJitter, RandomCrop, RandomHorizontalFlip, RandomGrayscale
import wandb

class Fish_Dataset(Dataset):

    def __init__(self, img_dir, ann_dir, transform, num_classes):
        self.img_labels = pd.read_csv(ann_dir)
        self.img_dir = img_dir
        self.transform = transform
        self.num_classes = num_classes
    
    def __getitem__(self, idx):
        assert self.transform is not None, ".set_tranform 메소드를 이용하여 transform 을 주입해주세요"
        file_path = self.img_labels.iloc[idx+1, 0]
        label = self.img_labels.iloc[idx+1, 1]
        image = cv2.imread(osp.join(self.img_dir, file_path))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = self.transform(image=image)['image']
        return image/255, label

    def set_transform(self, transform):
        self.transform = transform

    def __len__(self):
        return len(self.img_labels)-1