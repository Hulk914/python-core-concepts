# Core Python quick reference

[Course home](../README.md) · [Study plan](study_plan.md) · [Exercises](exercises.md)

Run a topic with `python learn.py <name>`. The examples below are small reminders; chapter links lead to explanations and edge cases.

## Values and text — `numbers`, `strings`

```python
number = int("12")             # input() would return text, not an int
7 / 2                         # 3.5
7 // 2                        # 3; -7 // 2 is -4
7 % 2                         # 1
2 ** 3                        # 8
bool("")                      # False; bool("False") is True
value = None
value is None                 # identity check for this sentinel
"Python"[1:4]                 # 'yth'; stop is excluded
"Python"[::-1]                # 'nohtyP'
"  a,b  ".strip().split(",")   # ['a', 'b']
"-".join(["a", "b"])          # 'a-b'
f"{12.5:.2f}"                 # '12.50'
```

[Chapter 1](../lessons/basics/README.md). `==` compares values; `is` compares identity. Use `math.isclose()` for approximate floating-point comparisons.

## Containers — `sequences`, `mappings`

```python
items = [3, 1, 1]
items.append(4)                # mutate; return None
last = items.pop()             # mutate; return removed item
ordered = sorted(items)       # new list; items.sort() would mutate
outer_copy = items.copy()     # shallow copy
point = (10, 20)
x, y = point                  # unpacking; singleton tuple is (10,)
profile = {"name": "Ada"}
profile.get("city", "unknown")
for key, value in profile.items():
    print(key, value)
{1, 2} | {2, 3}               # {1, 2, 3}, union
{1, 2} & {2, 3}               # {2}, intersection
{1, 2} - {2, 3}               # {1}, difference
empty_set = set()             # {} is a dict
```

[Chapter 2](../lessons/data_structures/README.md). Assignment aliases an object; a shallow copy shares nested objects. A tuple is hashable only when its elements are hashable. Sets have no order guarantee.

## Control flow — `loops`, `comprehensions`

```python
for index, item in enumerate(["a", "b"], start=1):
    print(index, item)
for left, right in zip([1, 2], [3, 4], strict=True):
    print(left, right)
evens = [n for n in range(6) if n % 2 == 0]
labels = ["even" if n % 2 == 0 else "odd" for n in range(4)]
squares = {n: n * n for n in range(3)}
unique_lengths = {len(word) for word in ["cat", "dog", "python"]}
```

[Chapter 3](../lessons/control_flow/README.md). `break` exits, `continue` skips one iteration, and a loop's `else` runs when no `break` occurs. `and`/`or` return operands. Filter into a new list instead of removing from the list being iterated.

## Functions — `arguments`, `functional`, `scope`

```python
def example(first, /, second=5, *, verbose=False, **options):
    return first + second

def total(*values):
    return sum(values)

def append_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

total(*[1, 2, 3])              # unpack values into positional arguments
sorted([("Ada", 36), ("Grace", 30)], key=lambda person: person[1])
list(map(str, [1, 2]))         # ['1', '2']
list(filter(lambda n: n > 0, [-1, 2]))  # [2]
```

[Chapter 4](../lessons/functions/README.md). Defaults are evaluated when `def` executes. No explicit return means `None`. Lookup follows LEGB; `nonlocal` rebinds an enclosing function variable. `map` and `filter` return one-shot iterators.

## Files and errors — `files`, `exceptions`

```python
from pathlib import Path

# 'example.txt' must exist for this read; paths are relative to cwd.
with Path("example.txt").open(encoding="utf-8") as stream:
    lines = [line.rstrip("\n") for line in stream]

try:
    number = int("12")
except ValueError:
    print("Expected an integer")
else:
    print(number + 10)
finally:
    print("Attempt finished")
```

[Chapter 5](../lessons/files_exceptions/README.md). `r`: read; `w`: create/truncate; `a`: append; `x`: create exclusively. `read()` advances the cursor; `seek(0)` rewinds. Catch a specific exception. Avoid returns inside `finally`.

## Objects — `classes`, `inheritance`

```python
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    pages: int

book = Book("Python Notes", 120)
```

[Chapter 6](../lessons/oop/README.md). `self` refers to the instance; `__init__` initializes its state. Class attributes can be shared; mutable per-instance values belong in `__init__` (or a dataclass `field(default_factory=list)`). `__str__` serves readers, `__repr__` debugging, and `__len__` the length protocol. Inheritance is an "is a" relationship; composition is "has a". Annotations do not enforce types at runtime.

## Decorators and generators — `decorators`, `generators`

```python
from functools import wraps

def passthrough(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)
    return wrapper

def cubes(count):
    for number in range(count):
        yield number ** 3

iterator = cubes(3)
next(iterator)                # 0
list(iterator)                # [1, 8]
next(iterator, "done")        # 'done'
```

[Chapter 7](../lessons/advanced/README.md). A decorator replaces a callable; preserve argument forwarding, return values, exceptions, and metadata. Generator bodies execute during iteration, retain state, and cannot be rewound.

## Imports and tools — `imports`, `collections`, `dates`, `paths`, `utilities`

| Need | Reach for | Reminder |
| --- | --- | --- |
| Execute a package module | `python -m package.module` | Run from the repository root |
| Entry-point guard | `if __name__ == "__main__":` | Protect demonstration calls |
| Count values | `collections.Counter` | Missing lookup returns 0 |
| Group values | `collections.defaultdict(list)` | `[]` can insert; `.get()` does not |
| Named immutable fields | `collections.namedtuple` | Fields may still reference mutable values |
| Calendar arithmetic | `datetime.date`, `timedelta` | `.total_seconds()` includes whole days |
| Path operations | `pathlib.Path` | A path object does not create a file |
| Temporary workspace | `tempfile.TemporaryDirectory` | Context-managed cleanup |
| Copy or move files | `shutil` | Work on disposable examples first |
| Data exchange | `json.dumps`, `json.loads` | JSON is not a Python object snapshot |
| Text patterns | `re.fullmatch`, `re.findall` | Raw strings help with backslashes |
| Randomized practice | `random.Random(seed)` | `shuffle` mutates; use `secrets` for tokens |

[Chapter 8](../lessons/modules/README.md) · [Chapter 9](../lessons/standard_library/README.md)

## Tests and debugging — `testing`

```console
python -m unittest discover -s tests -v
python -m unittest tests.test_text_tools -v
python -m compileall -q learn.py lessons projects tests
```

[Chapter 10](../lessons/testing/README.md). Test empty inputs, invalid values, repeated calls, and error paths. Use temporary storage. Read the exception message and relevant traceback frame; use `breakpoint()` when needed. Plain `assert` can be disabled by optimization.
