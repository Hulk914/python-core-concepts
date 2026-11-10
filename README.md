# Core Python Field Guide

A practical, example-first course and refresher for core Python. Start with values and collections, work through functions and objects, then build and test a small command-line task tracker.

This project grew out of my Python course practice notes. The original experiments are preserved in [`archive/course_notes`](archive/course_notes); the lessons turn those experiments into an organized learning resource.

## Start here

You need **Python 3.10 or newer** and a terminal. The course uses only the standard library: no packages, accounts, or API keys are required. Run commands from this repository's root directory.

```console
python --version
python learn.py
python learn.py numbers
python learn.py all
python -m unittest discover -s tests -v
```

On Windows, use `py` instead of `python` if needed. `learn.py` with no arguments lists the lessons. Each example prints its results, avoids interactive input, and keeps temporary file operations in a disposable directory. Importing a lesson does not run its demonstration.

## Follow the course

Read each chapter's README, run its examples, then answer its self-check before opening the solutions. Work at your own pace; the [study plan](docs/study_plan.md) offers a suggested schedule.

| Step | Chapter | What you will practice | Run these lesson names |
| --- | --- | --- | --- |
| 1 | [Values and strings](lessons/basics/README.md) | Types, operators, conversion, indexing, slicing, formatting | `numbers`, `strings` |
| 2 | [Data structures](lessons/data_structures/README.md) | Lists, tuples, dictionaries, sets, references, copying | `sequences`, `mappings` |
| 3 | [Control flow](lessons/control_flow/README.md) | Conditions, loops, unpacking, comprehensions | `loops`, `comprehensions` |
| 4 | [Functions](lessons/functions/README.md) | Arguments, defaults, scope, lambda, map, filter | `arguments`, `functional`, `scope` |
| 5 | [Files and exceptions](lessons/files_exceptions/README.md) | Context managers, file modes, conversion, error handling | `files`, `exceptions` |
| 6 | [Objects](lessons/oop/README.md) | Classes, instance state, special methods, inheritance, composition | `classes`, `inheritance` |
| 7 | [Decorators and generators](lessons/advanced/README.md) | Closures, wrappers, lazy iteration, exhaustion | `decorators`, `generators` |
| 8 | [Modules and packages](lessons/modules/README.md) | Imports, packages, the main guard, module execution | `imports` |
| 9 | [Standard library](lessons/standard_library/README.md) | Collections, dates, paths, random, JSON, regular expressions | `collections`, `dates`, `paths`, `utilities` |
| 10 | [Testing and style](lessons/testing/README.md) | Unit tests, edge cases, naming, tracebacks | `testing` |
| 11 | [Build a task tracker](projects/task_tracker/README.md) | Combine a data model, persistence, CLI, exceptions, and tests | See project guide |

Run a chapter example with `python learn.py <name>`. You can also run it as a module, for example `python -m lessons.basics.strings`.

## Revise or practice

- [Quick reference](docs/quick_reference.md): compact syntax, common pitfalls, and links back to lessons.
- [Practice exercises](docs/exercises.md): tasks with example inputs, expected results, and hints.
- [Solutions and explanations](docs/solutions.md): chapter self-check answers and exercise solutions.
- [Original-to-new map](archive/README.md): where each course file's ideas went.

The examples discuss surprises such as list aliasing, mutable defaults, `is` versus `==`, tuple contents that can change, exhausted generators, and `finally` overriding a return. Comments explain why a result occurs, not just what to type.

## Final project preview

```console
python -m projects.task_tracker add "Revise dictionaries"
python -m projects.task_tracker list
python -m projects.task_tracker done 1
python -m projects.task_tracker summary
```

The CLI stores your tasks in `.practice/tasks.json`, ignored by Git. Use `--file <path>` before the subcommand to choose a different file. The project README explains the design and provides a guided build sequence.

## Repository map

```text
learn.py                   Lesson menu and runner
lessons/                   Ten chapters with runnable examples and guided notes
projects/task_tracker/     A complete standard-library CLI project
tests/                     Behavior and integration tests using unittest
docs/                      Study plan, reference, exercises, and solutions
archive/course_notes/      Unmodified original notes, stored as text
```

## Quality and sharing

```console
python -m unittest discover -s tests -v
python learn.py all
python -m compileall -q learn.py lessons projects tests
```

The GitHub Actions workflow is configured to run tests and syntax checks on Python 3.10, 3.12, and 3.14, including running every lesson through the test suite. See [CONTRIBUTING.md](CONTRIBUTING.md) for the lesson format and review checklist. [Showcase notes](docs/showcase.md) provide a repository description, demo outline, and a starting point for a resume or LinkedIn post.

The emphasis is on explaining behavior, testing boundaries, and connecting individual concepts to a working program.
