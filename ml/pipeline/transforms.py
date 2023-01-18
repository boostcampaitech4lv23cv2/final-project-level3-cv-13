import albumentations as A
from albumentations.pytorch.transforms import ToTensorV2
import wandb

def transforms_1():
    return A.Compose([
                A.Resize(*wandb.config.resize),
                #A.Normalize(mean=mean, std=std, max_pixel_value=255.0, p=1.0),
                ToTensorV2(p=1.0)
                ])