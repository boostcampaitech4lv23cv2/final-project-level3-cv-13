import onnxruntime as ort
import numpy as np
import torch
import os
from google.cloud import storage

#Google Cloud Configuration
BUCKET_NAME="model-registry-cv13"
KEY_PATH="/opt/ml/helloworld-374304-e880cf8462f6.json"

class Inference:
    def __init__(self) -> None:
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= KEY_PATH
        storage_client = storage.Client()
        bucket = storage_client.bucket(BUCKET_NAME)
        blob = next(bucket.list_blobs())
        contents = blob.download_as_string()
        print(f"Downloaded ONNX from {BUCKET_NAME} as {blob.name}")
        self.session=self.__create_session(contents)

    def __create_session(self,model: str) -> ort.InferenceSession:
        return ort.InferenceSession(model)

    def run(self,x):
        out=self.session.run(None, {'input': x})
        return out[0][0].argmax(0)