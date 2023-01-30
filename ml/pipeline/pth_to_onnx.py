import torch.onnx
from importlib import import_module

#Function to Convert to ONNX 
def Convert_ONNX(): 

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model_module = getattr(import_module("model"), 'EfficientNetB7')  # default: BaseModel
    model = model_module(
        num_classes = 12
    ).to(device)
    
    model.to(device)
    
    checkpoint = torch.load("/opt/ml/final-project-level3-cv-13/ml/output/EfficientNetB7_10_16_Adam_0.0001_exp4/fish_EfficientNetB7_best_epoch8_0.9727.pth", map_location=device)
    model.load_state_dict(checkpoint)
    model.eval()

    # Let's create a dummy input tensor  
    # make dummy data
    batch_size = 1
    # model input size에 맞게 b c h w 순으로 파라미터 설정
    x = torch.rand(batch_size, 3, 384, 384, requires_grad=True).to(device)
    # feed-forward test
    output = model(x)

    # convert
    torch.onnx.export(model, x, "./efficientnetb7.onnx", export_params=True, opset_version=10, do_constant_folding=True
                  , input_names = ['input'], output_names=['output']
                  # , dynamic_axes={'input' : {0 : 'batch_size'}, 'output' : {0 : 'batch_size'}}
                  # dynamic axes 는 pytorch 1.2 부터 지원하는듯??
                  )

if __name__ == "__main__": 
    # Conversion to ONNX 
    Convert_ONNX() 