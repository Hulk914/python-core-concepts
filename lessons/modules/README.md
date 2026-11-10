# 8. Modules and packages

Previous: [Decorators and generators](../advanced/README.md) · Next: [Standard library](../standard_library/README.md)

**Goal:** split code by responsibility and import reusable behavior without executing demonstrations.

## Walkthrough

1. Inspect this directory: `imports.py` is a module; `sample_package/` is a package; `reports/` is a nested package. These regular packages contain `__init__.py`.
2. Read [imports.py](imports.py) and follow its imports into [greetings.py](sample_package/greetings.py) and [summary.py](sample_package/reports/summary.py).
3. Run `python learn.py imports`, then `python -m lessons.modules.imports`. The output differs for `__name__` because the second command executes the module as the entry point.
4. Notice that the imported helper modules return values and do not print at import time.

```python
def main():
    print("Only run the demonstration when explicitly requested")

if __name__ == "__main__":
    main()
```

## Tricky cases

- Running `python lessons/modules/imports.py` sets up a different import path from `python -m lessons.modules.imports`. Use the documented module command from the repository root.
- Top-level statements run when a module is first imported; a main guard protects only the code placed inside it.
- Python normally caches imports in `sys.modules`. Import is not a general way to rerun a script.
- Avoid filenames such as `random.py`, `json.py`, or `unittest.py` at the repository root: they can shadow standard library modules.
- `from module import *` hides where names come from. Prefer explicit imports.
- `__init__.py` is used here for regular packages; Python also supports namespace packages without it.

## Self-check

1. Why does importing `learn` not print the lesson menu?
2. If you edit a module while a REPL remains open, will another ordinary `import` necessarily execute it again?

Practice by moving your exercise 6 `Book` class into a package and importing it from another module. [Answers](../../docs/solutions.md#chapter-self-checks).
