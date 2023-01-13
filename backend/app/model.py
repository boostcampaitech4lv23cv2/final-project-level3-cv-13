import torchvision
import torch.nn as nn


class EfficientNetB0(nn.Module):
    def __init__(self, num_classes=5):
        super().__init__()
        self.base_model = torchvision.models.efficientnet_b0(pretrained=True)
        self.fc = nn.Linear(in_features=self.base_model.classifier[1].out_features, out_features=num_classes)

    def forward(self, x):
        x=self.base_model(x)
        x=self.fc(x)
        return x