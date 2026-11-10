# 10. Testing, style, and debugging

Previous: [Standard library](../standard_library/README.md) · Next: [Task tracker project](../../projects/task_tracker/README.md)

**Goal:** verify behavior at boundaries and make small examples easy to maintain.

## Walkthrough

1. Read [text_tools.py](text_tools.py), then run `python learn.py testing`. The original course's `cap()` exercise is now a reusable function with a clear text-only contract.
2. Read [test_text_tools.py](../../tests/test_text_tools.py). Follow arrange (input), act (call), and assert (expected outcome).
3. Run `python -m unittest tests.test_text_tools -v`, then `python -m unittest discover -s tests -v`.
4. Change the function to use `.title()` instead of `.capitalize()`. Predict which tests fail, run them, and then restore the function. A failing expectation helps explain the difference.
5. Inspect the project tests for temporary storage, malformed JSON, and command-line errors. Each test should use its own data.

## Tricky cases

- `"HELLO WORLD".capitalize()` is `"Hello world"`, not `"Hello World"`.
- Python's `assert` may be removed with `-O`. Use explicit exceptions for user-input validation and `unittest` assertions for tests.
- Test discovery uses `test*.py` by default. Importing tests and helpers should not print, prompt, or write data.
- One happy-path example does not establish the behavior for empty inputs, invalid types, repeated calls, or missing resources.
- Avoid tests that merely repeat implementation steps. Test outcomes a caller cares about.

## Style and debugging habits

- Use `snake_case` for functions and variables, `PascalCase` for classes, and `UPPER_CASE` for constants.
- Keep imports explicit and separate program entry points from reusable code.
- Use docstrings for contracts, and comments to explain reasoning or a non-obvious limitation.
- Read the exception type and message, then inspect the last relevant frame in the traceback. Use `breakpoint()` for a local debugger when print statements stop being useful.
- Compilation checks syntax, unit tests check selected behavior, and linting checks additional code-quality rules. None proves a program correct by itself.

An optional Ruff configuration is included in `pyproject.toml`. If Ruff is installed, run `python -m ruff check .`. It is a development tool; no third-party tools are needed to use the course or run the tests.

## Self-check

1. Which inputs would expose a mistaken switch from `.capitalize()` to `.title()`?
2. Why should a storage test use a temporary directory rather than the learner's task file?

Then try [exercise 10](../../docs/exercises.md#10-test-a-contract). [Answers](../../docs/solutions.md#chapter-self-checks).
