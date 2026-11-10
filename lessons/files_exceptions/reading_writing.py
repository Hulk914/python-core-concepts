"""Text file modes and the file cursor, using disposable practice files.

Run: python learn.py files
Try: replace mode='a' with mode='w' and predict the contents.
"""

from pathlib import Path
from tempfile import TemporaryDirectory


def main():
    with TemporaryDirectory(prefix="python-files-") as directory:
        path = Path(directory) / "notes.txt"
        # w creates or TRUNCATES a file; use it deliberately.
        with path.open(mode="w", encoding="utf-8") as stream:
            stream.write("Python\nPractice\n")
        with path.open(mode="r", encoding="utf-8") as stream:
            print("Read all:", repr(stream.read()))
            print("At end:", repr(stream.read()))  # '' because the cursor is at EOF
            stream.seek(0)
            print("After seek:", stream.readlines())
        print("Closed after with:", stream.closed)

        with path.open(mode="a", encoding="utf-8") as stream:
            stream.write("Revise\n")
        print("Appended:", path.read_text(encoding="utf-8").splitlines())
        with path.open(encoding="utf-8") as stream:
            print("Iterate lines:", [line.strip() for line in stream])
        try:
            with path.open(mode="x", encoding="utf-8"):
                pass
        except FileExistsError:
            print("x mode refuses to overwrite an existing file")
        # TemporaryDirectory removes its own directory when the context exits.


if __name__ == "__main__":
    main()
