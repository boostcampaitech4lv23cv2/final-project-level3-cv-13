import torch.nn as nn
import albumentations
import pandas as pd
from torch.utils.data import Dataset
from torchvision import datasets
from torch.utils.data.sampler import SubsetRandomSampler
import cv2
import numpy as np
import json

class DataLoader(Dataset):

    def __init__(self, img_dir, transform = None):
        self.img_labels = 
        self.img_dir = img_dir
        self.transform = transform
    
    
    def __getitem__(self, idx):
        image = cv2.imread(self.img_dir[idx])
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        if self.transform:
            image = self.transform(image)
        label = self.img_labels[idx]
        return image, label

    def __len__(self):
        return len(self.img_labels)