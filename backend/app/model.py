import torchvision
import torch.nn as nn
import torch

class EfficientNetB0(nn.Module):
    def __init__(self, num_classes=5):
        super().__init__()
        self.base_model = torchvision.models.efficientnet_b0(pretrained=True)
        self.fc = nn.Linear(in_features=self.base_model.classifier[1].out_features, out_features=num_classes)

    def forward(self, x):
        x=self.base_model(x)
        x=self.fc(x)
        return x
    
if __name__=="__main__":
    model=EfficientNetB0()
    x=torch.randn(1, 3, 512,512, requires_grad=True)
    torch.onnx.export(model,
                      x,
                      "ImageClassifier.onnx",
                      export_params=True,
                      input_names = ['input'],
                      output_names = ['output'],
                      dynamic_axes={'input' : {0 : 'batch_size'},
                                'output' : {0 : 'batch_size'}})
    