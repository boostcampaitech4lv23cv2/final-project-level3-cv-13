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
        logger = logging.getLogger()
        # DEBUG(10), INFO(20), WARNING(30, default), ERROR(40), CRITICAL(50)
        logger.setLevel("INFO")
        handler=logging.StreamHandler()
        handler.setFormatter(CustomFormatter())
        logger.addHandler(handler)
        logger.info(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])
        storage_client = storage.Client()
        bucket = storage_client.bucket(BUCKET_NAME)
        blob = next(bucket.list_blobs())
        contents = blob.download_as_string()
        logger.info(f"Downloaded ONNX from {BUCKET_NAME} as {blob.name}")
        self.session=self.__create_session(contents)

    def __create_session(self,model: str) -> ort.InferenceSession:
        return ort.InferenceSession(model)

    def run(self,x):
        out=self.session.run(None, {'input': x})
        return out[0][0].argmax(0)