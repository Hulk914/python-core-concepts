"""Inspect paths and practice copy/move/delete only inside a temporary folder.

Run: python learn.py paths
Try: explain why a path relative to __file__ differs from a path relative to cwd.
"""

import os
from pathlib import Path
import shutil
from tempfile import TemporaryDirectory


def main():
    print("Current working directory:", os.getcwd())
    print("Module filename:", Path(__file__).name)
    with TemporaryDirectory(prefix="python-paths-") as directory:
        root = Path(directory)
        source = root / "source.txt"
        source.write_text("practice\n", encoding="utf-8")
        destination = root / "copies"
        destination.mkdir()
        copied = destination / "copy.txt"
        shutil.copy2(source, copied)
        moved = destination / "moved.txt"
        shutil.move(str(copied), str(moved))
        print("Directory names:", sorted(path.name for path in root.iterdir()))
        print("Found text files:", sorted(path.name for path in root.rglob("*.txt")))
        print("Exists / suffix:", moved.exists(), moved.suffix)
        moved.unlink()  # remove one file
        destination.rmdir()  # remove an EMPTY directory
        print("After cleanup:", sorted(path.name for path in root.iterdir()))
    # Do not copy these delete operations onto personal folders for experiments.


if __name__ == "__main__":
    main()
