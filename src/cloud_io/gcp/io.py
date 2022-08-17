from pathlib import Path
from typing import Union

from cloud_io.gcp.base import get_client


def list_remote_files(bucket_name: str, prefix: Union[Path, str] = "") -> set[Path]:
    """List all files in a bucket given a prefix.

    If prefix is a Path: the prefix will be assumed to be a folder.
        Search for files within this folder.

    If prefix is a string: Search for files with that prefix.
    """
    if isinstance(prefix, Path):
        prefix = f"{prefix}/"
    remote_paths = get_client().list_blobs(bucket_name, prefix=prefix)
    return {Path(blob.name) for blob in remote_paths if not blob.name.endswith("/")}
