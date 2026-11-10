# 5. Files and exceptions

Previous: [Functions](../functions/README.md) · Next: [Objects](../oop/README.md)

**Goal:** handle resources reliably and distinguish expected bad input from programming errors.

## Walkthrough

1. Run `python learn.py files` and read [reading_writing.py](reading_writing.py). Its files live inside `TemporaryDirectory`, which cleans up on exit.
2. Follow the cursor through `read()`, another `read()`, `seek(0)`, and `readlines()`.
3. Compare modes: `r` reads an existing file; `w` creates or truncates; `a` appends; `x` creates and fails if the path exists. Text mode accepts strings; binary mode such as `rb` reads bytes.
4. Run `python learn.py exceptions` and read [handling_errors.py](handling_errors.py). Observe that `else` runs only when the `try` suite succeeds; `finally` runs as control leaves the statement during normal execution or exception propagation.
5. Replace `"oops"` with `"12.5"`. It is a valid float string, but not a valid input for `int()`.

## Tricky cases

- A second read at the end of the file returns `''`; the data did not disappear. The cursor advanced.
- `with` closes the file even when an exception leaves the block. Use an explicit text encoding, usually UTF-8.
- A relative path starts at the process working directory, not automatically beside the source file. `Path(__file__)` can locate resources relative to a module.
- `except:` also catches control signals such as `KeyboardInterrupt`. Catch specific exception types that the code can actually handle.
- `raise NewError(...) from error` preserves a causal traceback. Do not replace every failure with a vague message.
- Returning from `finally` can replace a previous return or suppress an exception. Keep returns out of cleanup blocks.
- `finally` is not a guarantee against forced process termination or a machine losing power.

## Self-check

1. What is the difference between `w`, `a`, and `x` when a file already exists?
2. If `try` returns 1 and `finally` returns 2, which value reaches the caller? Why is this dangerous?

Then try [exercise 5](../../docs/exercises.md#5-load-nonempty-lines). [Answers](../../docs/solutions.md#chapter-self-checks).
