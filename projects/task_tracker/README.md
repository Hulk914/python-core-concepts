# Final project: command-line task tracker

[Course home](../../README.md) · Previous: [Testing](../../lessons/testing/README.md)

Build a small program that remembers tasks between runs. This project combines functions, collections, classes, modules, JSON, file handling, exceptions, CLI arguments, and testing without external dependencies.

## Try the complete project

From the repository root:

```console
python -m projects.task_tracker --help
python -m projects.task_tracker add "Revise dictionaries"
python -m projects.task_tracker add "Practice generators"
python -m projects.task_tracker list
python -m projects.task_tracker done 1
python -m projects.task_tracker summary
```

On an initially empty task file, the last three commands produce:

```text
[ ] 1: Revise dictionaries
[ ] 2: Practice generators
Completed #1: Revise dictionaries
Total: 2 | Done: 1 | Pending: 1
```

Tasks are saved to `.practice/tasks.json` at the repository root. To use another file, put the global option **before** the subcommand:

```console
python -m projects.task_tracker --file .practice/demo.json add "Read about closures"
python -m projects.task_tracker --file .practice/demo.json list
```

IDs grow beyond the highest existing ID. Your actual IDs and summary depend on your saved tasks.

## Build it in layers

Read the completed code, then rebuild each layer in a practice copy. Keep the original tests available as a behavior specification.

| Step | File | Responsibility | What to explain |
| --- | --- | --- | --- |
| 1 | [model.py](model.py) | `Task`, add, complete, summarize | Why is this independent of files and printing? |
| 2 | [storage.py](storage.py) | Validate JSON, load and save records | How do dataclasses become dictionaries? |
| 3 | [cli.py](cli.py) | Parse arguments and display results | Why return an exit code instead of exiting everywhere? |
| 4 | [__main__.py](__main__.py) | Package execution entry point | What does `python -m` execute? |
| 5 | [Tests](../../tests/test_task_tracker.py) | Verify behavior through each layer | Which failures would a happy-path test miss? |

The flow is `CLI → load → model operation → save if changed → display`. Listing and summary commands load but never create or rewrite the task file.

### 1. Model the task

`@dataclass` creates initialization, representation, and equality methods for the three fields: a positive integer ID, a nonempty title, and a boolean completion flag.

`add_task()` trims a title and mutates the list intentionally. `complete_task()` changes only a matching task and raises for an unknown ID. `summarize()` returns a dictionary of counts. Type annotations on `Task` describe the fields; external JSON still needs explicit validation.

### 2. Persist validated data

A file looks like:

```json
[
  {"id": 1, "title": "Revise dictionaries", "done": true},
  {"id": 2, "title": "Practice generators", "done": false}
]
```

Missing files represent a fresh start. Invalid JSON, wrong field types, unexpected fields, duplicate IDs, and blank titles raise errors. The CLI reports those errors and leaves the original contents alone. Notice the strict check for IDs: `True` must not be accepted as integer 1.

Saving writes a neighboring `.tmp` file and replaces the destination only after the JSON write finishes. This avoids leaving a partially written destination when writing or replacement fails. The model functions expect valid `Task` objects from the CLI or validated storage; they are not a general validation framework for arbitrary Python objects.

### 3. Present errors clearly

`argparse` handles unknown commands, missing arguments, and non-integer IDs. Program failures go to standard error. Exit status 0 means success, 1 means a handled data/filesystem error, and 2 means an argument parsing error.

```console
python -m projects.task_tracker add "   "
python -m projects.task_tracker done 999
```

The first reports an empty title. The second reports an unknown ID unless your task file actually contains that ID. Both leave the file unchanged.

### 4. Test boundaries

```console
python -m unittest tests.test_task_tracker -v
```

The tests cover normal workflows, whitespace-only titles, sparse IDs, repeated completion, missing and corrupt files, invalid record types, Unicode text, failed file replacement, and the real module entry point. They use temporary directories and never write into your `.practice` task file.

## Scope and extension ideas

This is a single-user, one-process-at-a-time learning application. The fixed staging filename and read/modify/write flow do not coordinate simultaneous writers. It has no database, network service, authentication, or recovery journal.

Add pending-only filtering or renaming first. For due dates, design the JSON format change before editing the CLI. To explore concurrent use, replace the storage layer with SQLite and discuss transactions instead of assuming file replacement prevents lost updates.
