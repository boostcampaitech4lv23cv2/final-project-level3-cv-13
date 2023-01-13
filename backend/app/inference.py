import onnxruntime as ort
import numpy as np
import torch

MODEL_FILE = '/opt/ml/final-project-level3-cv-13/test/ImageClassifier.onnx'
DEVICE_NAME = 'cuda' if torch.cuda.is_available() else 'cpu'
DEVICE_INDEX = 0     # Replace this with the index of the device you want to run on
DEVICE=f'{DEVICE_NAME}:{DEVICE_INDEX}'

class Inference:
    def __init__(self) -> None:
        self.session=self.__create_session(MODEL_FILE)

    def __create_session(self,model: str) -> ort.InferenceSession:
        return ort.InferenceSession(model)

    def run(self,x):
        out=self.session.run(None, {'input': x})
        return out[0][0].argmax(0)