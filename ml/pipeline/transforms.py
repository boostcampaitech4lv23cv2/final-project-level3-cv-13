import albumentations as A
import cv2
from albumentations.pytorch.transforms import ToTensorV2


class transforms_1:
    def __init__(self, resize) -> None:
        self.transforms = A.Compose([
            A.Resize(*resize, cv2.INTER_LINEAR),
            A.Normalize(),
            ToTensorV2()
        ])
    
    def __call__(self, image):
        return self.transforms(image=image)
