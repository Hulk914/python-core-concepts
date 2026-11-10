"""Absolute imports, nested packages, and module entry points.

Run: python learn.py imports
Also: python -m lessons.modules.imports
"""

from lessons.modules.sample_package import greetings
from lessons.modules.sample_package.reports.summary import report


def main():
    print(greetings.greet("Ayush"))
    print(report([2, 4, 6]))
    print("This module's __name__:", __name__)
    # Under learn.py this is lessons.modules.imports; under -m it is __main__.
    # Python usually executes a module once per interpreter, then caches it in
    # sys.modules. Keep demonstrations behind the guard below.


if __name__ == "__main__":
    main()
