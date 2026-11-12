# Functions: contracts, returns and arguments
Section: Functions and scope

A function packages a computation behind a name and an interface. Its contract describes accepted inputs, returned outputs, deliberate mutations and possible failures. `def` creates a function object; calling it executes its body. Parameters are names in the definition; arguments are values supplied by a caller.

{{code:lessons/functions/arguments.py:add}}

```python verify
from lessons.functions.arguments import add

assert add(3) == 8
assert add(second=2, first=3) == 5
answer = add(10, 20)
assert answer * 2 == 60
```

Returning a value lets the caller reuse it. Printing writes a presentation to a stream. A function can print and return, but printing is not an implicit return. Falling off the end, or using bare `return`, returns `None`. A return exits only the current function, with cleanup constructs still honored.

## Argument passing follows the object model

When a call binds a parameter, the parameter refers to the supplied object. Rebinding that parameter does not rebind the caller's name. Mutating a supplied list changes the same list the caller references. This is often described as passing by assignment or object sharing.

```python verify
def change(items):
    items.append("shared")
    items = ["local replacement"]
    return items

original = []
assert change(original) == ["local replacement"]
assert original == ["shared"]
```

Avoid the claim “mutable values are passed by reference and immutable values by value.” The binding rule is the same; supported operations differ. State whether a helper mutates its inputs. A pure calculation with explicit inputs is usually easier to test than a function that also reads a file, prints and updates global state.

Checkpoint: modify a practice copy of `add()` to print rather than return. Explain why `add(2, 3) * 2` then fails even though the terminal showed `5`.

Run: `python learn.py arguments`. References: [[R03]], [[R08]].

<!-- page -->
# Parameter kinds and useful interfaces
Section: Functions and scope

An interface can distinguish parameters by how callers supply them. Positional-only parameters precede `/`. Positional-or-keyword parameters follow it. `*args` collects extra positional arguments into a tuple; parameters after `*` are keyword-only. `**kwargs` collects unmatched keyword arguments into a dictionary.

```python verify
def example(first, /, second=5, *extra, verbose=False, **options):
    return first, second, extra, verbose, options

assert example(1, 2, 3, 4, verbose=True, city="Pune") == (
    1, 2, (3, 4), True, {"city": "Pune"}
)
```

The stars in a definition collect arguments. At a call site, `*values` expands an iterable into positional arguments and `**options` expands a mapping into keyword arguments. Duplicate assignments to a parameter raise `TypeError`; they do not silently choose the last value.

{{code:lessons/functions/arguments.py:describe_person}}

```python verify
from lessons.functions.arguments import add, describe_person, sum_args

assert add(*[2, 3]) == 5
assert add(1, **{"second": 4}) == 5
assert sum_args() == 0
assert describe_person("Ayush", city="Pune")["city"] == "Pune"
```

Calling `describe_person(name="Ayush")` fails because the required positional-only argument was not supplied. A keyword named `name` can enter `details` when a positional name is supplied. In this particular implementation `**details` appears last in the returned dictionary, so it can override a prior `name` entry. That is an implementation consequence, not runtime signature enforcement of the returned data.

## Choose flexibility where it helps

Keyword-only flags make calls readable: `save(path, overwrite=False)` communicates more than `save(path, False)`. Excessive `**kwargs` can hide typos and unclear contracts. Prefer explicit parameters for stable public options and reserve forwarding for genuine adapters or decorators.

References: [[R03]], [[R07]].

<!-- page -->
# Defaults, sentinels and mutation policy
Section: Functions and scope

Default expressions are evaluated when the `def` statement executes. A mutable default therefore belongs to the function object and is reused across calls that omit that argument. It is not recreated at the start of every invocation.

```python verify
def bad_append(item, items=[]):
    items.append(item)
    return items

assert bad_append("a") == ["a"]
assert bad_append("b") == ["a", "b"]
```

That shared state is occasionally intentional, but usually a hidden bug. In the repository, omission means “create a fresh list,” while an explicitly supplied list means “mutate that list.” Checking identity with `None` preserves that distinction even if the supplied list is empty.

{{code:lessons/functions/arguments.py:append_item}}

```python verify
from lessons.functions.arguments import append_item

assert append_item("a") == ["a"]
assert append_item("b") == ["b"]
supplied = []
assert append_item("kept", supplied) is supplied
assert supplied == ["kept"]
```

`items = items or []` would discard an explicitly supplied empty list. That contradicts this contract. The correct condition depends on the meaning of omission, not on a general preference for short expressions.

## When None is valid data

Use a unique sentinel, such as `_MISSING = object()`, when the function needs to distinguish omission from an explicitly passed `None`. Check `value is _MISSING`. The same idea can distinguish a missing mapping key from a key whose stored value is `None`.

Time-dependent defaults have the same evaluation rule. A default of `datetime.now()` records definition time, not call time. Use an omitted value or inject a clock and compute inside the call. Test repeated calls to catch shared state; one happy-path call cannot reveal this class of bug.

References: [[R03]], [[R08]].

<!-- page -->
# Scope, closures and late binding
Section: Functions and scope

For ordinary name lookup in functions, LEGB means Local, Enclosing function, Global module and Builtins. Assignment normally makes a name local to the current function. Reading it before its local binding exists raises `UnboundLocalError`, even if a global variable has the same name.

{{code:lessons/functions/scope.py:make_counter}}

```python verify
from lessons.functions.scope import make_counter

first, second = make_counter(), make_counter(10)
assert [first(), first(), second()] == [1, 2, 11]
late = [lambda: index for index in range(3)]
captured = [lambda index=index: index for index in range(3)]
assert [function() for function in late] == [2, 2, 2]
assert [function() for function in captured] == [0, 1, 2]
```

The inner function retains access to its enclosing binding after the factory returns. `nonlocal count` lets it rebind that enclosing name. Every factory invocation creates an independent closure. Mutating a referenced list would not itself require `nonlocal`; rebinding the enclosing name does.

## Why the lambdas all return 2

Closures resolve the captured binding when called. The loop has finished by the time these lambdas run, so each sees the final index. A default parameter is evaluated when each lambda is created, capturing that iteration's value. A small function factory is another clear solution.

`global` selects a module-level binding for assignment. It does not make state global across all modules, processes or machines. Prefer explicit parameters and return values when possible; a global counter can complicate test isolation and concurrent calls.

## Protect useful names

Do not bind variables named `list`, `str`, `sum` or `id` without good reason: they hide builtins in that scope. Ordinary class bodies also have distinct scoping behavior; LEGB is a learning aid for function code, not a complete specification of every Python construct.

Run: `python learn.py scope`. Reference: [[R08]].

<!-- page -->
# Callables, sorting and functional tools
Section: Functions and scope

Functions are objects: they can be stored, passed and returned. A lambda creates a small function from one expression. It has the same closure rules as `def`; it is not automatically faster or isolated from external state. Name a function when its behavior deserves explanation or reuse.

```python verify
numbers = [1, 2, 3, 4, 5]
mapped = map(lambda number: number % 2 == 0, numbers)
assert list(mapped) == [False, True, False, True, False]
assert list(mapped) == []
assert list(filter(lambda number: number % 2 == 0, numbers)) == [2, 4]
people = [("Ada", 36), ("Grace", 30), ("Linus", 30)]
assert sorted(people, key=lambda person: person[1]) == [
    ("Grace", 30), ("Linus", 30), ("Ada", 36)
]
```

`map()` transforms every input item. `filter()` keeps original items whose predicate is true. Both return one-shot iterators. A comprehension is often easier to read when the operation combines a condition and transformation. Use a named callable directly when it already exists: `sorted(words, key=len)`.

## Stable ordering is useful

Grace stays before Linus because the ages tie and the sort is stable. A tuple key such as `(age, name)` introduces an explicit secondary ordering. Sorting incomparable objects without a key can raise `TypeError`. The key should represent the domain's order rather than an accidental string representation.

```python verify
from functools import partial

parse_binary = partial(int, base=2)
assert parse_binary("101") == 5
assert sorted(["Python", "a", "code"], key=len) == ["a", "code", "Python"]
```

`partial()` binds selected arguments and returns a callable. It is useful when an API expects one function with a simpler signature. Avoid adding abstraction when a short direct call is clearer.

Checkpoint: predict what happens if the same `map` object is passed to two consumers. The first consumer advances it; the second receives only what remains. If two independent traversals are required, create fresh iterators from a reusable source or materialize a bounded result intentionally.

Run: `python learn.py functional`. References: [[R07]], [[R11]].

<!-- page -->
# Recursion and decomposing a problem
Section: Functions and scope

Extension beyond the repo: recursion means a function calls itself directly or indirectly. A correct recursive design needs a base case, a smaller subproblem and a way to combine the answer. The same reasoning applies to directory trees, nested expressions and hierarchical data.

```python verify
def factorial(number):
    if type(number) is not int:
        raise TypeError("number must be an integer")
    if number < 0:
        raise ValueError("number must be non-negative")
    if number == 0:
        return 1
    return number * factorial(number - 1)

assert factorial(0) == 1
assert factorial(5) == 120
```

For `factorial(3)`, the call expands to `3 * factorial(2)`, then `3 * 2 * factorial(1)`, and stops at zero. Results return through the pending frames. This implementation is a teaching example; `math.factorial()` is the standard tool for actual factorial computation.

## Understand the cost

This recursion uses O(n) calls and O(n) stack frames, aside from growing-integer arithmetic. CPython does not perform general tail-call elimination. Deep recursive inputs can raise `RecursionError`. Increasing the recursion limit is not a substitute for choosing a suitable iterative algorithm.

A loop with an accumulator can compute the same result with constant auxiliary frame space. For a tree, recursion may closely match the structure; for a very deep or adversarial tree, an explicit stack gives more control. Cyclic object graphs need a visited policy or another termination rule.

## Decompose before compressing

The tracker separates “find a task,” “change its state,” “serialize records” and “display a result.” This is decomposition even without recursion. Each function answers one domain question. A useful helper earns its place by naming an idea, isolating a boundary or removing meaningful repetition.

Practice: write an iterative factorial in a scratch file. Reject the same invalid values, then compare outputs for 0 through 10. Explain why matching outputs on that range is evidence, rather than proof for all inputs.

References: [[R03]], [[R06]].

<!-- page -->
# Type hints and runtime validation
Section: Functions and scope

Type hints communicate intended interfaces to readers, editors and static analyzers. Python does not normally enforce annotations at call time. `def double(n: int) -> int: return n * 2` can still receive a string and return repeated text if no runtime check prevents it.

```python verify
from collections.abc import Iterable

def total(values: Iterable[int]) -> int:
    return sum(values)

def strict_pages(value: int) -> int:
    if type(value) is not int:
        raise TypeError("pages must be an integer")
    if value < 0:
        raise ValueError("pages must be non-negative")
    return value

assert total(iter([1, 2, 3])) == 6
assert strict_pages(0) == 0
```

Accept the least restrictive interface that meets the algorithm's needs. An `Iterable[int]` can supply one pass; a `Sequence[int]` promises more, including indexing and length. Requiring a `list[int]` unnecessarily rejects tuples or generators when all you do is iterate. Conversely, annotating an iterable does not make an algorithm safe to traverse it twice.

## Where checks belong

External JSON, user input and network responses need parsing and validation. A dataclass annotation alone cannot reject `Task(True, "", "false")`. Internal functions may rely on validated domain objects if that boundary is explicit. Repeat checks when a different trust boundary or invariant requires them, not mechanically in every helper.

`int | None` expresses a union in Python 3.10+. `Any` effectively relaxes static checking; it does not verify arbitrary data. A `Protocol` can describe a required interface by behavior and is introduced with the object-model extensions. Runtime-checkable protocols still do not validate every annotated method signature or a business invariant.

## Keep the version promise clear

This guide uses annotations compatible with the repo's 3.10 baseline. Annotation evaluation details have evolved in later Python versions. If building a library that inspects annotations at runtime, use documented inspection tools for the supported interpreter range rather than relying on an assumed evaluation time.

References: [[R15]], [[R14]].

<!-- page -->
# Files: modes, cursors and text encoding
Section: Files, errors and resources

A file object tracks an open resource and a current position. Reading consumes from that position. Text mode decodes bytes using an encoding and may translate newline conventions; binary mode reads or writes bytes. Specify UTF-8 when that is your file format rather than relying on an environment's default.

| Mode | Intent | Existing file |
| --- | --- | --- |
| `r` | Read text | Required; otherwise missing-file error |
| `w` | Write from the start | Truncated on opening |
| `a` | Append text | Preserved; writes append |
| `x` | Create exclusively | Refuses to overwrite |
| `rb` / `wb` | Read/write binary data | Use bytes rather than str |

```python verify
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as directory:
    path = Path(directory) / "notes.txt"
    path.write_text("Python\nPractice\n", encoding="utf-8")
    with path.open(encoding="utf-8") as stream:
        assert stream.read() == "Python\nPractice\n"
        assert stream.read() == ""
        stream.seek(0)
        assert stream.readline() == "Python\n"
    assert stream.closed
```

An empty string from `read()` means end of file for a text stream. `seek(0)` rewinds this ordinary file. Text-mode positions can be opaque cookies; do not assume every character position is a byte offset in a variable-width encoding. Line iteration often avoids needing manual seeks.

## Resource lifetime matters

`with` closes the stream when the block exits normally, returns or raises. It is more dependable than hoping a finalizer runs immediately. `TemporaryDirectory` similarly provides isolated practice storage and cleanup. The repository demonstrates all file mutation inside disposable directories.

Try changing append mode to write mode in a practice copy. Predict exactly when old contents disappear: opening in `w` truncates, before the new write succeeds.

Run: `python learn.py files`. References: [[R07]], [[R17]], [[R42]].

<!-- page -->
# Paths, streaming and filesystem boundaries
Section: Files, errors and resources

`Path("notes.txt")` describes a path; it does not create a file. Relative paths resolve against the process's current working directory. A path built from `Path(__file__)` is anchored to a module location. The tracker uses the latter to keep its default storage predictable across invocation directories.

```python verify
from pathlib import Path
from tempfile import TemporaryDirectory

def load_nonempty_lines(path):
    result = []
    with Path(path).open(encoding="utf-8") as stream:
        for line in stream:
            cleaned = line.strip()
            if cleaned:
                result.append(cleaned)
    return result

with TemporaryDirectory() as directory:
    path = Path(directory) / "notes.txt"
    path.write_text("  Python  \n\n Practice\n", encoding="utf-8")
    assert load_nonempty_lines(path) == ["Python", "Practice"]
```

This function streams the input lines but accumulates all retained results. Its memory is proportional to the returned data, not constant. A yielding version can stream results too, but then resource ownership and early termination require thought. A missing file raises; returning an empty list instead would hide a failure and change the stated contract.

## Race conditions in a familiar pattern

`if path.exists(): path.read_text()` can still fail if the file changes between those operations. Attempt the operation and catch the specific failure you can handle. A precheck can help a user interface, but it does not guarantee a later filesystem operation will succeed.

Use `.mkdir(parents=True, exist_ok=True)` to prepare directories when creating them is intended. `.unlink()` removes a file; `.rmdir()` removes an empty directory. `shutil.copy2()` copies a file with supported metadata, while `shutil.move()` moves it. The repository confines copy, move and deletion demonstrations to a temporary root.

For untrusted filenames, joining a user-provided string to a root is not automatically containment: absolute paths, `..` and symlinks need a deliberate policy. Resolve paths and validate the intended boundary where the application requires it.

References: [[R17]], [[R42]].

<!-- page -->
# Exceptions and useful failure contracts
Section: Files, errors and resources

An exception carries a failure up the call stack until a matching handler catches it. Syntax errors prevent a code unit from being parsed. Runtime errors occur while executing valid syntax. Catch the failures you can recover from or translate into a clearer boundary error; let unexpected defects retain their traceback.

{{code:lessons/files_exceptions/handling_errors.py:parse_integer}}

```python verify
from lessons.files_exceptions.handling_errors import parse_integer

assert parse_integer("12") == 12
try:
    parse_integer("oops")
except ValueError as error:
    assert "Expected a whole number" in str(error)
    assert isinstance(error.__cause__, ValueError)
else:
    raise AssertionError("Invalid numeric text must fail")
```

`raise ... from error` states that a higher-level error was caused by a lower-level one. This preserves diagnostic context. A bare `raise` inside a handler re-raises the current exception. `raise ... from None` suppresses displayed context and should be a deliberate presentation choice, not a way to conceal a useful cause.

## Keep the try block narrow

Put parsing inside `try`, handle `ValueError` in `except` and place success work in `else`. Errors in the success work then cannot be mistaken for parse failures. `finally` is for cleanup on the construct's exit; context managers are usually clearer for resource cleanup.

A return in `finally` can replace a pending return or suppress an exception. Avoid it. A bare `except:` also catches `KeyboardInterrupt` and `SystemExit`; ordinary application boundaries usually catch `Exception` or a specific tuple, and often should catch narrower types still.

The tracker reports `ValueError` and `OSError` to standard error and returns status 1. Argument errors are handled by `argparse` with status 2. A library function should generally raise rather than deciding to print and terminate the process itself.

Run: `python learn.py exceptions`. Reference: [[R09]].

<!-- page -->
# Context managers and dependable cleanup
Section: Files, errors and resources

A context manager defines entering and leaving a managed operation. `with expression as value` obtains the manager, calls its enter method and binds the returned value. Its exit method receives exception information on failure and runs for normal block exit too. Returning a truthy result from exit suppresses the active exception, so do that only as an intentional contract.

```python verify
from contextlib import contextmanager

@contextmanager
def recorded_resource(events):
    events.append("open")
    try:
        yield "resource"
    finally:
        events.append("close")

events = []
try:
    with recorded_resource(events) as resource:
        assert resource == "resource"
        raise ValueError("example failure")
except ValueError:
    pass
assert events == ["open", "close"]
```

`contextlib.contextmanager` adapts a generator with one yield into a context manager. The setup runs before the yield; the caller's block uses the yielded value; cleanup belongs in `finally`. If you catch an exception for logging and intend it to propagate, re-raise it. Accidentally swallowing it makes the caller believe the operation succeeded.

## Composition of lifetimes

Multiple managers can appear in one `with`; already-entered managers are exited if entering a later one fails. `ExitStack` helps when the number of resources is determined dynamically. It lets cleanup registration follow successful acquisition instead of scattering flags and nested `try` blocks.

The repo's `with TemporaryDirectory(...)` containing `with path.open(...)` is a practical example: the stream closes before the directory is removed. Do not depend on `__del__` for correctness. Reference cycles, interpreter shutdown and implementation differences make finalization timing unsuitable for reliable file release.

Cleanup is a language-level protocol, not a promise to survive abrupt process termination, power loss or machine failure. Persistent-data durability requires a separate storage design, discussed in the tracker and architect sections.

References: [[R13]], [[R06]].
