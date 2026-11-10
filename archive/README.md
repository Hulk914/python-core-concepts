# Original course notes

[Course home](../README.md)

`course_notes/` contains byte-for-byte copies of the original project files. Original Python files now have a `.py.txt` suffix so they can be read without being mistaken for maintained runnable lessons or discovered tests. Other text files keep their original names and contents.

The archive captures experiments, including commented code, unfinished paths, and input prompts. Use the new lessons to run examples. The archive is a historical reference.

| Original file or folder | Maintained home | Improvements |
| --- | --- | --- |
| `demo.py`: values, strings, containers | [Basics](../lessons/basics/README.md), [Data structures](../lessons/data_structures/README.md) | Separate runnable examples, slicing and mutability explanations |
| `demo.py`: loops and comprehensions | [Control flow](../lessons/control_flow/README.md) | Predictable output, unpacking, loop `else`, empty inputs |
| `demo.py`: functions, `*args`, `**kwargs`, lambda | [Functions](../lessons/functions/README.md) | Return values, safe defaults, parameter kinds, scope |
| `demo.py`: file reads and exception handling | [Files and exceptions](../lessons/files_exceptions/README.md) | Temporary files, explicit conversion, specific exceptions |
| `demo.py`: optional `colorama` snippet | No third-party dependency retained | The maintained course uses the standard library only |
| `classes.py` | [Objects](../lessons/oop/README.md) | Shared versus instance state, protocols, composition, no finalizer side effects |
| `decorators.py` | [Decorators](../lessons/advanced/decorators.py) | Argument forwarding, return values, `functools.wraps` |
| `generators.py` | [Generators](../lessons/advanced/generators.py) | Cubes, Fibonacci, `next`, exhaustion, lazy execution |
| `modules lesson/` | [Modules and packages](../lessons/modules/README.md) | Importable names, explicit package structure, main guards |
| `inbuildModules/collection_demo.py` | [Collections](../lessons/standard_library/collections_demo.py) | All three tools demonstrated, missing-key behavior |
| `inbuildModules/datetimemod.py` | [Dates and times](../lessons/standard_library/dates_times.py) | Fixed examples, leap years, durations, timezone awareness |
| `inbuildModules/osmodule.py` | [Paths and OS](../lessons/standard_library/paths_os.py) | Copy/move/delete contained in temporary directories |
| `unitTestsLinting/` | [Testing](../lessons/testing/README.md), [Tests](../tests/) | Discoverable tests, importable functions, edge-case coverage |
| `files/` | [File lesson](../lessons/files_exceptions/reading_writing.py) | Fixtures created on demand, no working-directory assumptions |

Two original details are worth revisiting: `input()` produces text (the old `add()` mixed it with an integer), and `/n` is literal text while `\n` is a newline escape. The file lesson demonstrates the latter with `repr()` so the difference is visible.
