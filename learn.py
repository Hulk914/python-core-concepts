"""Discover and run the course examples: python learn.py [lesson | all]."""

import argparse
from importlib import import_module

# Explicit names make the learning order visible and keep the runner predictable.
LESSONS = {
    "numbers": ("lessons.basics.numbers", "Values, types, operators, and conversion"),
    "strings": ("lessons.basics.strings", "Indexing, slicing, and formatting"),
    "sequences": ("lessons.data_structures.sequences", "Lists, tuples, and copying"),
    "mappings": ("lessons.data_structures.mappings_sets", "Dictionaries and sets"),
    "loops": ("lessons.control_flow.branching_loops", "Conditions and iteration"),
    "comprehensions": ("lessons.control_flow.comprehensions", "Building collections"),
    "arguments": ("lessons.functions.arguments", "Parameters, defaults, *args, **kwargs"),
    "functional": ("lessons.functions.functional_tools", "Lambda, map, filter, sorting"),
    "scope": ("lessons.functions.scope", "Local names, closures, and nonlocal"),
    "files": ("lessons.files_exceptions.reading_writing", "File modes and context managers"),
    "exceptions": ("lessons.files_exceptions.handling_errors", "Specific exceptions and finally"),
    "classes": ("lessons.oop.classes", "Instances, attributes, and special methods"),
    "inheritance": ("lessons.oop.inheritance", "Inheritance and composition"),
    "decorators": ("lessons.advanced.decorators", "Wrapping calls with functools.wraps"),
    "generators": ("lessons.advanced.generators", "Yield, next, and lazy iteration"),
    "imports": ("lessons.modules.imports", "Modules, packages, and the main guard"),
    "collections": ("lessons.standard_library.collections_demo", "Counter, defaultdict, namedtuple"),
    "dates": ("lessons.standard_library.dates_times", "Dates, durations, and timezone awareness"),
    "paths": ("lessons.standard_library.paths_os", "pathlib, os, and shutil"),
    "utilities": ("lessons.standard_library.utilities", "Random, JSON, regex, and itertools"),
    "testing": ("lessons.testing.demo", "Assertions and testing behavior"),
}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("lesson", nargs="?", choices=["list", "all", *LESSONS])
    args = parser.parse_args(argv)
    if args.lesson in (None, "list"):
        for name, (_, description) in LESSONS.items():
            print(f"{name:16} {description}")
        print("\nRun: python learn.py <lesson>  |  python learn.py all")
        return

    selected = LESSONS if args.lesson == "all" else [args.lesson]
    for name in selected:
        module_path, description = LESSONS[name]
        print(f"\n=== {name}: {description} ===")
        import_module(module_path).main()


if __name__ == "__main__":
    main()
