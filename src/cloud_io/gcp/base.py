import os
from pathlib import Path

import google.cloud.storage as gcs
from cloud_io.tools.error import CloudIOError


def download_blob(
    blob_path: Path,
    local_path: Path,
    bucket_name: str,
) -> Path:
    local_path = Path(local_path)

    blob = get_blob(blob_path, bucket_name)
    blob.download_to_filename(local_path)
    return local_path


def get_blob(blob_name: Path, bucket_name: str) -> gcs.Blob:
    bucket = get_bucket(bucket_name)
    if isinstance(blob_name, Path):
        return bucket.blob(blob_name.as_posix())
    return bucket.blob(blob_name)


def get_bucket(bucket_name: str) -> gcs.Bucket:
    client = get_client()
    return client.bucket(bucket_name=bucket_name)


def get_client() -> gcs.Client:
    if "GOOGLE_APPLICATION_CREDENTIALS" in os.environ.keys():
        client = gcs.Client()
    else:
        raise CloudIOError("Please setup your credentials.")
    return client
