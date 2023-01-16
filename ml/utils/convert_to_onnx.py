import torch.onnx
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# sys.path.append('ml/final-project-level3-cv-13/ml/pipeline/model')

from pipeline import model
'''
#Function to Convert to ONNX 
def Convert_ONNX(): 

    # set the model to inference mode 
    model.eval() 

    # Let's create a dummy input tensor  
    dummy_input = torch.randn(1, 3, 384, 384, requires_grad=True)  

    # Export the model   
    torch.onnx.export(model,         # model being run 
         dummy_input,       # model input (or a tuple for multiple inputs) 
         "ImageClassifier.onnx",       # where to save the model  
         export_params=True,  # store the trained parameter weights inside the model file 
         opset_version=10,    # the ONNX version to export the model to 
         do_constant_folding=True,  # whether to execute constant folding for optimization 
         input_names = ['modelInput'],   # the model's input names 
         output_names = ['modelOutput'], # the model's output names 
         dynamic_axes={'modelInput' : {0 : 'batch_size'},    # variable length axes 
                                'modelOutput' : {0 : 'batch_size'}}) 
    print(" ") 
    print('Model has been converted to ONNX')

if __name__ == "__main__": 

    # Let's build our model 
    #train(5) 
    #print('Finished Training') 

    # Test which classes performed well 
    #testAccuracy() 

    # Let's load the model we just created and test the accuracy per label 
    model = model.EfficientNetB0
    path = "/opt/ml/final-project-level3-cv-13/ml/output/exp/best.pth" 
    model.load_state_dict(torch.load(path)) 

    # Test with batch of images 
    #testBatch() 
    # Test how the classes performed 
    #testClassess() 
 
    # Conversion to ONNX 
    Convert_ONNX()'''

from torch.autograd import Variable

#import torch.onnx
import torchvision
import torch
import onnx

model = model.Resnet50(num_classes=5)
dummy_input = Variable(torch.randn(1, 3, 384, 384))
path = "/opt/ml/final-project-level3-cv-13/ml/output/exp/best.pth" 
model.load_state_dict(torch.load(path))
model.eval()
torch.onnx.export(model, dummy_input, "moment-in-time.onnx", opset_version=12)