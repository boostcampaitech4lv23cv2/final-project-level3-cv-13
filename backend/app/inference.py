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


class Inference:
    def __init__(self) -> None:
        self.logger = logging.getLogger()
        # DEBUG(10), INFO(20), WARNING(30, default), ERROR(40), CRITICAL(50)
        self.logger.setLevel("INFO")
        handler=logging.StreamHandler()
        handler.setFormatter(CustomFormatter())
        self.logger.addHandler(handler)
        self.logger.info(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])
        storage_client = storage.Client()
        bucket = storage_client.bucket(BUCKET_NAME)
        newest_blob=None
        for blob in bucket.list_blobs():
            if newest_blob==None:
                newest_blob=blob
            else:
                if newest_blob.time_created<blob.time_created:
                    
                    newest_blob=blob
        contents = blob.download_as_string()
        self.logger.info(f"Downloaded ONNX from {BUCKET_NAME} as {newest_blob.name}")
        self.session=self.__create_session(contents)
        self.blob_name=newest_blob.name

    def __create_session(self,model: str) -> ort.InferenceSession:
        return ort.InferenceSession(model)

    def run(self,x):
        out=self.session.run(None, {'input': x})
        self.logger.info(out[0][0].tolist())
        return out[0][0]