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

class transforms_2:
    def __init__(self, resize) -> None:
        self.transforms = A.Compose([
            A.Resize(*resize, cv2.INTER_LINEAR),
            A.RandomRotate90(p=0.5),
            A.Normalize(),
            ToTensorV2()
        ])
    
    def __call__(self, image):
        return self.transforms(image=image)

class transforms_3:
    def __init__(self, resize) -> None:
        self.transforms = A.Compose([
            A.Resize(*resize, cv2.INTER_LINEAR),
            A.RandomRotate90(p=0.5),
            A.RandomBrightnessContrast(brightness_limit=(-0.2, 0.2)),
            A.Normalize(),
            ToTensorV2()
        ])
    
    def __call__(self, image):
        return self.transforms(image=image)

class transforms_4:
    def __init__(self, resize) -> None:
        self.transforms = A.Compose([
            A.Resize(*resize, cv2.INTER_LINEAR),
            A.RandomRotate90(p=0.5),
            A.RandomBrightnessContrast(brightness_limit=(-0.2, 0.2)),
            A.Oneof([
                A.CLAHE(p=0.3),
                A.Blur(blur_limit=(30, 40), p=0.3)
            ])
            A.Normalize(),
            ToTensorV2()
        ])
    
    def __call__(self, image):
        return self.transforms(image=image)