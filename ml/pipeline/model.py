import torch.nn as nn
import torch
import timm

# timm create_model
# timm.models
'''
def __init__(
        self, block_args, num_classes=1000, num_features=1280, in_chans=3, stem_size=32, fix_stem=False,
        output_stride=32, pad_type='', round_chs_fn=round_channels, act_layer=None, norm_layer=None,
        se_layer=None, drop_rate=0., drop_path_rate=0., global_pool='avg'):
    super(EfficientNet, self).__init__()
    act_layer = act_layer or nn.ReLU
    norm_layer = norm_layer or nn.BatchNorm2d
    norm_act_layer = get_norm_act_layer(norm_layer, act_layer)
    se_layer = se_layer or SqueezeExcite
    self.num_classes = num_classes
    self.num_features = num_features
    self.drop_rate = drop_rate
    self.grad_checkpointing = False
    
    Changeable kwargs...
'''
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
        self.efficientnet = timm.create_model('efficientnet_b0', pretrained = True, num_classes = num_classes, drop_rate=0.5, act_layer = nn.ReLU)

    def forward(self, x):
        x = self.efficientnet(x)
        return x

class EfficientNetB4(nn.Module):
    
    def __init__(self, num_classes):
        super().__init__()
        self.efficientnet = timm.create_model('efficientnet_b4', pretrained = True, num_classes = num_classes, drop_rate=0.5, act_layer = nn.ReLU)

    def forward(self, x):
        x = self.efficientnet(x)
        return x

class EfficientNetB7(nn.Module):
    
    def __init__(self, num_classes):
        super().__init__()
        self.efficientnet = timm.create_model('efficientnet_b7', pretrained = True, num_classes = num_classes, drop_rate=0.5, act_layer = nn.ReLU)

    def forward(self, x):
        x = self.efficientnet(x)
        return x

class Swin_Base_patch4_window12_384_in22k(nn.Module):
    
    def __init__(self, num_classes):
        super().__init__()
        self.swin_base = timm.create_model('swin_base_patch4_window12_384_in22k', pretrained = True, num_classes = num_classes, drop_rate=0.5, act_layer = nn.ReLU)

    def forward(self, x):
        x = self.swin_base(x)
        return x
class Swin_Tiny_patch4_window7_224(nn.Module):
    
    def __init__(self, num_classes):
        super().__init__()
        self.swin_base = timm.create_model('swin_tiny_patch4_window7_224', pretrained = True, num_classes = num_classes, drop_rate=0.5, act_layer = nn.ReLU)

    def forward(self, x):
        x = self.swin_base(x)
        return x
    
class efficientnetv2_l(nn.Module):
    
    def __init__(self, num_classes):
        super().__init__()
        self.efficientnetv2 = timm.create_model('efficientnetv2_l', pretrained = True, num_classes = num_classes, drop_rate=0.5, act_layer = nn.ReLU)

    def forward(self, x):
        x = self.efficientnetv2(x)
        return x
    
class efficientnetv2_s(nn.Module):
    
    def __init__(self, num_classes):
        super().__init__()
        self.efficientnetv2 = timm.create_model('efficientnetv2_s', pretrained = True, num_classes = num_classes, drop_rate=0.5, act_layer = nn.ReLU)

    def forward(self, x):
        x = self.efficientnetv2(x)
        return x