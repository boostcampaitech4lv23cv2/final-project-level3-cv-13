import logging
import onnxruntime as ort
import numpy as np
import os
from google.cloud import storage

#Google Cloud Configuration
BUCKET_NAME="model-registry-cv13"

class CustomFormatter(logging.Formatter):

    grey = "\x1b[38;20m"
    green= "\x1b[32;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: green + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

class Logger:
    def __init__(self):
        self.logger = logging.getLogger()
        # DEBUG(10), INFO(20), WARNING(30, default), ERROR(40), CRITICAL(50)
        self.logger.setLevel("INFO")
        handler=logging.StreamHandler()
        handler.setFormatter(CustomFormatter())
        self.logger.addHandler(handler)
    def get_logger(self):
        return self.logger

class Inference:
    def __init__(self,logger) -> None:
        self.logger= logger
        self.storage_client = storage.Client()
        bucket = self.storage_client.bucket(BUCKET_NAME)
        best_blob=None
        best_blob_score=0
        for blob in bucket.list_blobs():
            # 분류태스크_모델명_성능_날짜.onnx
            task, _, score, _= blob.name.split("-")
            score=float(score)
            if task=="fish":
                if best_blob == None:
                    best_blob=blob
                    best_blob_score=score
                else:
                    if best_blob_score<score:
                        best_blob=blob
                        best_blob_score = score
        contents = best_blob.download_as_string()
        self.logger.info(f"Downloaded ONNX from {BUCKET_NAME} as {best_blob.name}")
        self.session=self.__create_session(contents)
        self.blob_name=best_blob.name

    def __create_session(self,model: str) -> ort.InferenceSession:
        return ort.InferenceSession(model)

    def run(self,x):
        out=self.session.run(None, {'input': x})
        return out[0][0]

class Inference_Sashimi:
    def __init__(self,logger) -> None:
        self.logger= logger
        self.storage_client = storage.Client()
        bucket = self.storage_client.bucket(BUCKET_NAME)
        best_blob=None
        best_blob_score=0
        for blob in bucket.list_blobs():
            # 분류태스크_모델명_성능_날짜.onnx
            task, _, score, _= blob.name.split("-")
            score=float(score)
            if task=="sashimi":
                if best_blob == None:
                    best_blob=blob
                    best_blob_score=score
                else:
                    if best_blob_score<score:
                        best_blob=blob
                        best_blob_score = score
        contents = best_blob.download_as_string()
        self.session=self.__create_session(contents)
        self.logger.info(f"Downloaded ONNX from {BUCKET_NAME} as {best_blob.name}")
        self.blob_name=best_blob.name

    def __create_session(self,model: str) -> ort.InferenceSession:
        return ort.InferenceSession(model)

    def run(self,x):
        out=self.session.run(None, {'input': x})
        return out[0][0]