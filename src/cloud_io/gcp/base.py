import json
import os
from pathlib import Path

import google.cloud.storage as gcs
from cloud_io.gcp.filesystem import prepare_filesystem
from cloud_io.tools.error import CloudIOError
from google.oauth2.service_account import Credentials


def download_blob(
    blob_path: Path,
    local_path: Path,
    bucket_name: str,
) -> Path:
    local_path = Path(local_path)
    existing_path = prepare_filesystem(local_path)
    if existing_path is not None:
        return existing_path

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
    elif "GOOGLE_APPLICATION_CREDENTIALS_JSON" in os.environ.keys():
        client = _access_with_raw_json()
    else:
        raise CloudIOError("Please setup your credentials.")
    return client


def _access_with_raw_json() -> gcs.Client:
    raw_json = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS_JSON")
    parsed_json = raw_json.replace("\n", "\\n")
    service_account_info = json.loads(parsed_json)
    credentials = Credentials.from_service_account_info(service_account_info)
    return gcs.Client(credentials=credentials, project=credentials.project_id)
