from utils import UploadBlob
from datetime import datetime
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/opt/ml/storage_key.json"

today = datetime.today().strftime('%Y%m%d')
save_dir = "../output/EfficientNetB4_10_16_Adam_0.0001_exp"
data = "fish"

UploadBlob.upload_blob(
        bucket_name="model-registry-cv13",
        source_file_name=f"{save_dir}/{data}_EfficientNetB4_best_0.9681.onnx",
        destination_blob_name=f"{data}_EfficientNetB4-0.9681-{today}.onnx",
    )