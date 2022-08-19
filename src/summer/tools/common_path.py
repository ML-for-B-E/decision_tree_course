from pathlib import Path

LIB_PATH = Path(__file__).parents[1]
SRC_PATH = LIB_PATH.parent
ROOT_PATH = SRC_PATH.parent
NOTEBOOK_PATH = Path(ROOT_PATH, "notebook")
DATA_PATH = Path(ROOT_PATH, "data")
