from pathlib import Path
from typing import Union, MutableSet

from cloud_io.gcp.base import get_client
from cloud_io.gcp.base import download_blob


def list_remote_files(bucket_name: str, prefix: Union[Path, str] = "") -> MutableSet[Path]:
    """List all files in a bucket given a prefix.

    If prefix is a Path: the prefix will be assumed to be a folder.
        Search for files within this folder.

    If prefix is a string: Search for files with that prefix.
    """
    if isinstance(prefix, Path):
        prefix = f"{prefix}/"
    remote_paths = get_client().list_blobs(bucket_name, prefix=prefix)
    return {Path(blob.name) for blob in remote_paths if not blob.name.endswith("/")}


def download_file(
    file_path: Path,
    bucket_as_local: Path,
    bucket_name: str,
) -> Path:
    """Download a single file from GCS"""
    local_path = Path(file_path)
    blob_path = local_path.relative_to(bucket_as_local)
    local_path = download_blob(
        blob_path,
        local_path,
        bucket_name=bucket_name,
    )
    return local_path
