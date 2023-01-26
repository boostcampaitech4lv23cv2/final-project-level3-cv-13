import albumentations as A
from albumentations.pytorch.transforms import ToTensorV2
import cv2


class transforms_1:
    def __init__(self, resize, **args):
        self.transform = A.Compose([
            A.Resize(*resize, cv2.INTER_LINEAR),
            A.Normalize(),
            ToTensorV2()
        ])

    def __call__(self, image):
        return self.transform(image=image)