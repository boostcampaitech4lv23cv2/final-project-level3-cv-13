import sys

# [START storage_upload_file]
from google.cloud import storage


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        f"File {source_file_name} uploaded to {destination_blob_name}."
    )


# [END storage_upload_file]

if __name__ == "__main__":
    upload_blob(
        bucket_name="model-registry-cv13",
        source_file_name="/opt/ml/final-project-level3-cv-13/ml/output/exp/best.onnx",
        destination_blob_name="resnet50-0.6605-20230113.onnx",
    )