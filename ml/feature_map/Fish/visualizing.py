import torch
import torchvision
import torchvision.transforms as transforms
import torch.nn as nn
import torch.nn.functional as F
import cv2
import numpy as np
import timm
import os
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import albumentations as A
import cv2
from albumentations.pytorch.transforms import ToTensorV2
from random import randint 


fish_category = {'Olive_flounder' : 0,
                 'Korea_rockfish' : 1,
                 'Red_seabream' : 2,
                 'Black_porgy' : 3,
                 'Rock_bream' : 4,
                 'Croaker' : 5,
                 'Argyrosomus_japonicus' : 6,
                 'Starry_flounder' : 7,
                 'Longtooth_grouper' : 8,
                 'Convict_grouper' : 9,
                 'Japanese_amberjack' : 10,
                 'Yellowtail_amberjack' : 11,
                }

use_cuda = torch.cuda.is_available()
device = torch.device("cuda" if use_cuda else "cpu")
print(f'Currently using {device}...')

class TempModel(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.efficientnet = timm.create_model('efficientnet_b4', pretrained = True, num_classes = num_classes, drop_rate=0.5, act_layer = nn.ReLU)

    def forward(self, x):
        x = self.efficientnet(x)
        return x

file_path = './fish_EfficientNetB4_best_epoch23_0.7847.pth'
model = TempModel(num_classes =12)
model.to(device)
model.load_state_dict(torch.load(file_path))
model.eval()

# making hook
activation=None
class_weight = None

def hook_4_fm(model,input,output):
    global activation
    activation =output.clone().detach().requires_grad_(True)

def hook_4_clf_w(model,input,output):
    global class_weight
    class_weight = model.weight

model.efficientnet.conv_head.register_forward_hook(hook_4_fm)
model.efficientnet.classifier.register_forward_hook(hook_4_clf_w)



class transforms_1:
    def __init__(self, resize) -> None:
        self.transforms = A.Compose([
            A.Resize(*resize, cv2.INTER_LINEAR),
            A.Normalize(),
            ToTensorV2(),
        ])
    
    def __call__(self, image):
        return self.transforms(image=image)

transform=A.Compose([
        A.Resize(384, 384),
        A.Normalize(),
        ToTensorV2(),
    ])

trans_resize = A.Compose([
    A.Resize(384,384)
])

current_path = os.getcwd()
dataset_dir = os.path.join(current_path,"test_data")

data_list = os.listdir(dataset_dir)

index = randint(0,len(data_list)-1)

image_name = data_list[index]

#추후 비교를 위해 따로 저장
origin_image = np.array(cv2.imread(os.path.join(dataset_dir,image_name)))
origin_image = trans_resize(image=origin_image)['image']

#학습을 위한 데이터
image = transform(image=origin_image)['image']
image = image.unsqueeze(0)
image = image.to(device, dtype=torch.float32)

output = model(image)
preds = torch.argmax(output, dim=-1)
tmp = activation.squeeze(axis = 0)
label_weight = class_weight[preds[0]]
label_weight = label_weight.unsqueeze(-1).unsqueeze(-1)



cam = torch.squeeze(tmp)* label_weight
cam = torch.sum(cam,axis = 0)
cam = cam.detach().cpu().numpy()

#origin = origin_img.detach().cpu().numpy()
from mpl_toolkits.axes_grid1 import make_axes_locatable

final_cam = cv2.resize(cam, dsize=(384, 384), interpolation= cv2.INTER_CUBIC)

plt.figure(figsize=(20,40))

plt.subplot(1,3,1)
plt.title("CAM + Image")

plt.imshow(origin_image)
plt.imshow(final_cam,cmap = 'Reds' ,alpha=0.7)

plt.subplot(1,3,2)
plt.title("Origin")
plt.imshow(origin_image)

ax = plt.subplot(1,3,3)
plt.title("CAM")
im =plt.imshow(final_cam, cmap = 'Reds' ,alpha=0.6)
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size = "5%", pad = 0.05)
plt.colorbar(im, cax= cax)
print("정답 : ", image_name)
keys = fish_category.keys()
key_lst = list(keys)
print("예측 : ",key_lst[preds[0]])