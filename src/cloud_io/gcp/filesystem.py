from pathlib import Path
from typing import Optional

from cloud_io.tools.error import FileSystemError


def prepare_filesystem(path: Path, is_file: bool = True) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    if not path.exists():
        return None
    
    return clear_filesystem(path, is_file)


def clear_filesystem(path: Path, is_file: bool = True):
    if path.is_dir() and is_file:
        msg = f"Cannot clear {path=}. Expected a file, found a directory."
        raise FileSystemError(msg)

    if path.is_file():
        return clear_file(path)

    return clear_dir(path)


def clear_dir(path: Path) -> Optional[Path]:
    if not path.is_dir():
        msg = f"{path=} is not a directory."
        raise FileSystemError(msg)
    return path


def clear_file(path: Path) -> Optional[Path]:
    if not path.is_file():
        msg = f"{path=} is not a file."
        raise FileSystemError(msg)
    return path
