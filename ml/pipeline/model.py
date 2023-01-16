import torch.nn as nn
import torch
import timm
#from torchsummaryX import summary

class Resnet50(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.resnet = timm.create_model('resnet50', pretrained = True, num_classes = num_classes, drop_rate=0.5)

    def forward(self, x):
        x = self.resnet(x)
        return x

class EfficientNetB0(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.efficientnet = timm.create_model('efficientnet_b0', pretrained = True, num_classes = num_classes, drop_rate=0.5)

    def forward(self, x):
        x = self.efficientnet(x)
        return x
