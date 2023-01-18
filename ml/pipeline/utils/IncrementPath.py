import os
import glob
import re

from pathlib import Path

def increment_path(path, exist_ok=False):
    """ Automatically increment path, i.e. runs/exp --> runs/exp0, runs/exp1 etc.

    Args:
        path (str or pathlib.Path): f"{model_dir}/{args.name}".
        exist_ok (bool): whether increment path (increment if False).
    """
    path = Path(path)
    if path.exists() == False:
        os.mkdir(path)
        return str(path)
    else:
        dirs = glob.glob(f"{path}*")
        split_path = str(path).split('/')[-1]
        matches = [re.search(rf"{split_path}(\d+)", d) for d in dirs]
        i = [int(m.groups()[0]) for m in matches if m]
        n = max(i) + 1 if i else 2
        os.mkdir(f"{path}{n}")
        return f"{path}{n}"
