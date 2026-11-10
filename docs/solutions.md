# Solutions and explanations

[Exercises](exercises.md) · [Course home](../README.md)

## Chapter self-checks

### 1. Values and strings

1. `True`, `-3`, and `'on'`. A nonempty string is truthy; `int(float)` truncates toward zero; a negative slice starts from the end.
2. `int` and `str` do not support addition together. Converting first produces `12`; concatenating strings instead would produce `'102'`.

### 2. Data structures

1. `[1, 2]`. Both names reference the same list.
2. The tuple's references cannot be reassigned, but its inner list can change. It cannot be a dictionary key because it contains an unhashable list.

### 3. Control flow

1. `[5, 3, 1]`. Stop 0 is excluded and each step subtracts 2.
2. An empty loop reaches `else`; a loop that executes `break` does not.

### 4. Functions

1. The functions look up the same enclosing `i` when called, after it has reached 2. `[lambda i=i: i for i in range(3)]` captures each current value as a default.
2. `TypeError`: the required `name` is positional-only. With `**details`, a `name` keyword can be collected into details, but it still does not supply the required positional argument.

### 5. Files and exceptions

1. `w` truncates, `a` appends, and `x` raises `FileExistsError`.
2. `2` wins. Returning from `finally` replaces the pending return and can also suppress an exception, hiding a failure from the caller.

### 6. Objects

1. Each instance needs an independent list. A mutable class-level list would otherwise be shared through class attribute lookup.
2. There is no `__bool__`, so Python uses `__len__`. An empty name gives length zero and therefore falsy truthiness.

### 7. Decorators and generators

1. `[0, 1, 4]`, then `[]`. The generator is exhausted after the first conversion.
2. Construction returns a generator without running its body. `next()` begins execution, which checks the count and raises `ValueError`.

### 8. Modules

1. Its call to `main()` is inside a main guard. On import its name is `learn`, not `__main__`.
2. Normally no: Python reuses the module cached in `sys.modules`. Restarting the REPL is often the clearest option while learning; reloading has additional state considerations.

### 9. Standard library

1. `.get()` does not add the key or call the factory; `[]` does both for an absent key.
2. `5` and `172805.0`. The `seconds` attribute is the remainder after whole days.

### 10. Testing

1. Multiword inputs such as `'HELLO WORLD'`: capitalize returns `'Hello world'`; title returns `'Hello World'`.
2. A test should be independent, repeatable, and unable to overwrite the learner's tasks. Temporary directories provide isolated files and cleanup.

## Exercise solutions

These are complete definitions you can copy into a practice module. Compare the reasoning with your version; there is often more than one good implementation.

### 1. Alternating text

```python
def alternating_case(text):
    return "".join(
        character.lower() if index % 2 == 0 else character.upper()
        for index, character in enumerate(text)
    )
```

An empty input yields no fragments, so joining returns `''`. Spaces still occupy an index. This is the implementation in the strings lesson.

### 2. Unique values in order

```python
def unique_in_order(values):
    return list(dict.fromkeys(values))
```

Dictionary keys deduplicate while retaining first-insertion order. This contract requires hashable values; nested lists raise `TypeError`. Values that compare equal and share hashes, such as `1` and `True`, share a key.

### 3. Even squares

```python
def even_squares(values):
    return [number**2 for number in values if number % 2 == 0]
```

The filter operates on each original number before its square is included. Zero and negative even numbers are handled by the same condition.

### 4. Running counter

```python
def make_counter(start=0):
    count = start

    def increment():
        nonlocal count
        count += 1
        return count

    return increment
```

Each factory call creates a new enclosing scope. Without `nonlocal`, assigning `count` would make it local to `increment`, and reading it in `+=` would raise `UnboundLocalError`.

### 5. Load nonempty lines

```python
from pathlib import Path

def load_nonempty_lines(path):
    with Path(path).open(encoding="utf-8") as stream:
        result = []
        for line in stream:
            cleaned = line.strip()
            if cleaned:
                result.append(cleaned)
        return result
```

The explicit loop keeps transformation and filtering readable. `with` closes the file on return or failure. Missing-file errors propagate as required by the contract.

### 6. A small Book class

```python
class Book:
    def __init__(self, title, pages):
        if type(pages) is not int:
            raise TypeError("pages must be an integer")
        if pages < 0:
            raise ValueError("pages must be non-negative")
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title} ({self.pages} pages)"

    def __len__(self):
        return self.pages
```

A zero-page book is falsy through the length protocol. Decide deliberately whether this behavior makes sense in a real application. This small exercise checks the initial count; it does not enforce invariants on future attribute assignments.

### 7. A repeatable decorator

```python
from functools import wraps

def repeat(times):
    if type(times) is not int:
        raise TypeError("times must be an integer")
    if times < 0:
        raise ValueError("times must be non-negative")

    def decorate(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            return [function(*args, **kwargs) for _ in range(times)]
        return wrapper

    return decorate
```

Configuration is validated when `repeat(times)` runs, not on every wrapped call. For zero repetitions the wrapped function is never called. If one invocation raises, the exception propagates and later repetitions do not run. Repetition also repeats side effects, so choose what you decorate carefully.

### 8. Lazy running totals

```python
def running_totals(values):
    total = 0
    for value in values:
        total += value
        yield total
```

The input is consumed only as results are requested. `itertools.accumulate()` provides this behavior in the standard library; implementing it once helps explain the iterator model.

### 9. Word counts

```python
from collections import Counter

def word_counts(text):
    return Counter(text.casefold().split())
```

The contract deliberately treats punctuation as part of a token. Tokenization requirements should be explicit rather than silently changing what counts as a word.

### 10. Test a contract

```python
import unittest
from lessons.testing.text_tools import capitalize_text

class CapitalizeContractTests(unittest.TestCase):
    def test_multiword_text(self):
        self.assertEqual(capitalize_text("HELLO WORLD"), "Hello world")

    def test_empty_text(self):
        self.assertEqual(capitalize_text(""), "")

    def test_non_string(self):
        with self.assertRaises(TypeError):
            capitalize_text(123)
```

The first test distinguishes capitalization from title casing; the others document boundaries. Save in a file starting with `test_` and use unittest discovery.
