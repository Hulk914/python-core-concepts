# The Ultimate Core Python Guide

Repository edition · 12 November 2026

<a id="page-2"></a>

# Contents · 1 of 2
Section: Navigation

## [Start here](#page-4)  ·  4–5
How to use this guide; Run Python and explore the repository.

## [Values and text](#page-6)  ·  6–13
Names, objects and the execution model; Numeric types, operators and conversion; Floating point and deliberate comparisons; Operators, precedence and bitwise work; plus 4 further topics.

## [Containers and references](#page-14)  ·  14–17
Choose the right container; Lists and tuples in practice; Aliasing, shallow copies and deep copies; Dictionaries, sets and hashability.

## [Control flow](#page-18)  ·  18–21
Branches, loops and loop else; Iteration helpers and comprehensions; Pattern matching and readable dispatch; Costs, contracts and choosing an algorithm.

## [Functions and scope](#page-22)  ·  22–28
Functions: contracts, returns and arguments; Parameter kinds and useful interfaces; Defaults, sentinels and mutation policy; Scope, closures and late binding; plus 3 further topics.

## [Files, errors and resources](#page-29)  ·  29–32
Files: modes, cursors and text encoding; Paths, streaming and filesystem boundaries; Exceptions and useful failure contracts; Context managers and dependable cleanup.

## [Objects and protocols](#page-33)  ·  33–39
Classes, instances and bound methods; Class state, shadowing and method kinds; Special methods and Python protocols; Inheritance, super and composition; plus 3 further topics.

## [Iterators and decorators](#page-40)  ·  40–45
Iterables, iterators and exhaustion; Implement an iterator protocol; Generator functions and suspended state; Streaming pipelines and iterator tools; plus 2 further topics.

## [Modules and environments](#page-46)  ·  46–48
Modules, packages and import behavior; Entry points and command-line behavior; Environments, style and project hygiene.

## [Standard-library toolbox](#page-49)  ·  49–53
Counter, defaultdict, namedtuple and deque; Dates, durations and time zones; JSON and data-boundary validation; Regular expressions and precise text rules; plus 1 further topics.

## [Testing and debugging](#page-54)  ·  54–56
Tests that distinguish correct behavior; Isolation, failure injection and integration; Read tracebacks and diagnose deliberately.

Select a section title to jump there. PDF bookmarks also list every page.
Page numbers in this guide are the PDF's physical page numbers.

---

<a id="page-3"></a>

# Contents · 2 of 2
Section: Navigation

## [Capstone implementation](#page-57)  ·  57–61
Task tracker: trace a complete workflow; Task tracker: model operations and identity; Task tracker: validate before constructing; Task tracker: replacement and its limits; plus 1 further topics.

## [Deeper Python extensions](#page-62)  ·  62–64
CPython memory, references and measurement; Concurrency, parallelism and the GIL; Performance, observability and robustness.

## [Practice workbook](#page-65)  ·  65–70
Practice workbook · values and functions; Practice workbook · resources and objects; Practice workbook · iteration and testing; Workbook answers · exercises 1–4; plus 2 further topics.

## [Revision desk](#page-71)  ·  71–72
Revision map and a practical study plan; The pitfalls checklist.

## [Official reference library](#page-73)  ·  73–74
Reference library · language and data; Reference library · engineering and tooling.

## [Mock interview · instructions](#page-75)  ·  75–75
Mock interviews: format and scoring.

## [Mock interview · fresher](#page-76)  ·  76–81
Fresher · objects, equality and arithmetic; Fresher · text and container choice; Fresher · copying and control flow; Fresher · functions and defaults; plus 2 further topics.

## [Mock interview · mid-level](#page-82)  ·  82–87
Mid-level · signatures and closures; Mid-level · laziness and decorators; Mid-level · hashing and domain objects; Mid-level · error boundaries and imports; plus 2 further topics.

## [Mock interview · senior](#page-88)  ·  88–93
Senior · memory ownership and object design; Senior · profiling and cache correctness; Senior · concurrency and cancellation; Senior · persistence and schema evolution; plus 2 further topics.

## [Mock interview · architect](#page-94)  ·  94–99
Architect · requirements and persistence; Architect · concurrent edits and idempotency; Architect · workload and streaming design; Architect · plugins and trust boundaries; plus 2 further topics.

Select a section title to jump there. PDF bookmarks also list every page.
Page numbers in this guide are the PDF's physical page numbers.

---

<a id="page-4"></a>

# How to use this guide
Section: Start here

This book grows from the repository's maintained course: ten chapters, 21 runnable lessons, ten practice exercises and a command-line task tracker. It serves two readers: a new student who needs the reasoning behind the syntax, and a returning developer who needs to explain behavior precisely. Read in order the first time; use the contents and bookmarks when revising.

## The learning loop

For each topic, predict the output before running the code. Draw the references when objects are shared. Change one input, explain what should happen and then check. Finally, close the book and rebuild the smallest useful example. Recognizing a solution is easier than producing one; the second skill is what practice develops.

**Repository excerpt** identifies code extracted directly from a maintained source file, with its original line number. Other examples are new teaching examples or small adaptations. Run commands from the repository root unless a page explicitly says otherwise. Output blocks and comments describe the stated inputs; temporary paths and environment details can vary.

In code examples, `assert expression` states an expected result: a true expression is silent; a false one raises `AssertionError`. For example, `assert 2 + 3 == 5` checks arithmetic. These checks let you run predictions directly. `#` introduces a comment, and quoted text such as `'hello'` is a string value. Use `print(value)` when you want to display a result. Later chapters distinguish teaching assertions from production input validation.

## Compatibility and scope

The repository targets Python 3.10 or newer and needs only the standard library. Teaching examples keep that baseline. Official reference links are pinned to Python 3.14 for a consistent reference edition; version-sensitive additions are called out. The guide was checked on the available Python 3.15 interpreter, with 34 repository tests passing. That run is evidence for that interpreter, not a claim that every Python version was tested locally.

The foundations follow the repo. Clearly marked extension pages introduce protocols, typing, performance and concurrency to prepare for deeper interviews. Frameworks and data-science libraries are outside this core-language course. Architect questions use the tracker as a design exercise; they do not imply the sample application already has those capabilities.

## What success looks like

You can explain why two names see the same mutation, design a function with a clear contract, handle a file failure without losing data, test an edge case and trace an operation through the tracker. In an interview, lead with behavior, show a short example and then discuss assumptions and tradeoffs.

Source: `README.md`, `docs/study_plan.md`, `docs/exercises.md`, `docs/solutions.md`.

---

<a id="page-5"></a>

# Run Python and explore the repository
Section: Start here

Python executes statements in a file from top to bottom. A terminal command launches the interpreter; the interactive prompt, or REPL, evaluates short experiments immediately. Type the code after `>>>` when a tutorial shows a prompt. The examples in this guide omit that prompt so code can be copied into a file.

```console
python --version
python learn.py
python learn.py strings
python learn.py all
python -m unittest discover -s tests -v
```

On Windows, `py` can replace `python`. The lesson menu prints names such as `numbers`, `sequences` and `generators`. Running a single name calls that lesson's `main()`. Running `all` follows the explicit registry in `learn.py`. You do not need to install a web framework or obtain credentials.

## Read the tree as a map of responsibilities

| Location | What to find there |
| --- | --- |
| `learn.py` | Lesson names and the command-line runner |
| `lessons/` | Reusable functions, demonstrations and chapter notes |
| `projects/task_tracker/` | A model, JSON storage and a CLI |
| `tests/` | Behavior checks and integration workflows |
| `docs/` | Study plan, exercises, solutions and this guide |
| `archive/course_notes/` | Historical experiments stored as text |

The archive preserves early notes, including incomplete fragments. Learn from the maintained lesson modules first. A file ending in `.py.txt` is a readable historical note, not a module to run.

## First five minutes

Run `numbers`. Predict `-7 // 2` and `bool("False")`, then explain the results. Run `strings`, locate `alternating_case()` and change its input without changing the function. Finally run the tests once so you know what a healthy checkout looks like.

If imports fail, check the working directory and interpreter before editing `sys.path`. A module command such as `python -m lessons.basics.strings` is meant to run from the repository root. A relative filename resolves against the process's current working directory, which need not be the script's directory.

References: [R27: Modules tutorial](https://docs.python.org/3.14/tutorial/modules.html), [R28: Virtual environments tutorial](https://docs.python.org/3.14/tutorial/venv.html).

---

<a id="page-6"></a>

# Names, objects and the execution model
Section: Values and text

A name is a binding to an object. Objects have identity, type and value. Assignment changes a binding; it does not automatically copy the object. Dynamic typing means a name can later refer to an object of a different type. The object still has a type, and that type determines which operations it supports.

```python
left = [1, 2]
right = [1, 2]
alias = left
assert left == right       # equal values
assert left is not right   # separate list objects
assert alias is left       # two bindings to one object
alias.append(3)
assert left == [1, 2, 3]
alias = "rebound"
assert left == [1, 2, 3]   # rebinding alias did not change left
```

Think of the first three assignments as arrows: `left` and `alias` point to list A; `right` points to list B. Mutation changes A, so every reference to A observes the change. Rebinding `alias` draws a new arrow and leaves A alone. This model explains function arguments, shared class state and shallow copying later in the book.

## Equality, identity and missing values

`==` asks whether objects compare equal; a type can define that comparison. `is` asks whether both references identify one object and cannot be overloaded. Use `value is None` for the missing-value singleton. Never use `is` to compare strings or numbers: interpreter reuse of some objects is not an application equality rule.

An immutable object cannot change its own value. An integer binding can still be rebound: `count += 1` calculates an integer and updates the binding. A list can change its contents while retaining its identity. Immutability of an outer container does not promise immutability of every object it references.

## Execution is more than “interpreted”

In CPython, source is compiled to bytecode and executed by a virtual machine. Bytecode caching can reduce repeated compilation; it does not eliminate execution. Other implementations can make different choices. Distinguish a Python language guarantee from a CPython implementation detail when discussing memory or performance.

Run: `python learn.py numbers`. References: [R06: Python data model](https://docs.python.org/3.14/reference/datamodel.html), [R08: Execution model and name binding](https://docs.python.org/3.14/reference/executionmodel.html).

---

<a id="page-7"></a>

# Numeric types, operators and conversion
Section: Values and text

Use `int` for whole numbers, `float` for approximate binary fractions and `complex` when real and imaginary parts are needed. Python integers have arbitrary precision within available memory; they are not fixed 32-bit machine integers. `bool` has the values `True` and `False` and is a subclass of `int`, which matters at validation boundaries.

```python
assert 7 / 2 == 3.5
assert 7 // 2 == 3
assert -7 // 2 == -4
assert -7 % 2 == 1
assert 2 ** 3 == 8
assert int(-3.9) == -3
assert int("42") + 1 == 43
assert isinstance(True, int)
assert True + True == 2
```

`/` is true division. `//` floors the quotient toward negative infinity; `int(float_value)` truncates toward zero. The distinction appears for negative values. For nonzero integer `b`, `a == (a // b) * b + a % b`. A nonzero remainder has the divisor's sign. Use parentheses when an expression's grouping would otherwise be hard to read.

## Convert at the boundary

`input()` returns text. If the user types `12`, `int(text)` makes it numeric; adding text to an integer raises `TypeError`. Invalid numeric text raises `ValueError`. `int("3.5")` fails because that text is not an integer representation. Converting it through `float` and then `int` would change the contract by truncating.

```python
text = "12"
number = int(text)
print(number + 10)   # 22
print(text + "10")   # 1210
```

**Type error versus value error:** the wrong kind of object usually deserves `TypeError`; a valid kind with an unacceptable value usually deserves `ValueError`. The tracker rejects boolean IDs even though booleans are integer instances. Later you will see `type(value) is int` used deliberately for that strict contract.

Try negative operands for `//` and `%`. Explain both the quotient and the remainder using the identity above, rather than memorizing isolated outputs.

Source: `lessons/basics/numbers.py`. References: [R01: Python tutorial: numbers and text](https://docs.python.org/3.14/tutorial/introduction.html), [R07: Built-in functions](https://docs.python.org/3.14/library/functions.html).

---

<a id="page-8"></a>

# Floating point and deliberate comparisons
Section: Values and text

Many decimal fractions have no finite binary representation. A float stores a nearby representable number, so a sequence of operations can accumulate small errors. Formatting makes a result look tidy; it does not change the stored number or make an exact equality comparison reliable.

```python
from decimal import Decimal
from math import isclose

assert 0.1 + 0.2 != 0.3
assert f"{0.1 + 0.2:.2f}" == "0.30"
assert isclose(0.1 + 0.2, 0.3)
assert isclose(0.0, 1e-10, abs_tol=1e-9)
assert Decimal("0.1") + Decimal("0.2") == Decimal("0.3")
```

`math.isclose(a, b)` applies relative and absolute tolerances. A relative tolerance scales with magnitude. An absolute tolerance is especially useful near zero, where a purely relative comparison may reject small errors. Choose tolerances from the problem's acceptable error, not from whatever makes the current test pass.

## Choose representation from the domain

For exact decimal arithmetic, `Decimal` gives decimal semantics with a configurable context. Construct it from decimal strings when those are the source values. `Decimal(0.1)` starts with the already approximated float, so it does not recover the original decimal intent. For exact rational values, `fractions.Fraction` is another standard-library option.

Amounts of money require a rounding rule and a unit as well as a representation. Integer minor units can work when the allowed precision is fixed; decimal values can work when business rules demand decimal arithmetic. Merely changing `float` to `Decimal` does not settle tax rounding, currency conversion or serialization policy.

## A useful test design

Test a typical computation, one near zero and one near a rounding boundary. Compare exact quantities exactly and approximate quantities with an explicit tolerance. Do not round every intermediate value unless the domain requires it: repeated rounding can introduce a different error.

Revision prompt: why can a printout show `0.30` while `value == 0.3` is false? The printout is a representation chosen for readers; equality compares the underlying values.

Run: `python learn.py numbers` and `python learn.py utilities`. References: [R40: Floating-point arithmetic tutorial](https://docs.python.org/3.14/tutorial/floatingpoint.html), [R41: decimal arithmetic](https://docs.python.org/3.14/library/decimal.html).

---

<a id="page-9"></a>

# Operators, precedence and bitwise work
Section: Values and text

An operator's precedence decides grouping when parentheses are absent. It is not the same as evaluation order. Function arguments and most ordinary operands evaluate left to right, while `and`, `or` and conditional expressions can skip work. Use parentheses when a reader would otherwise need to look up a precedence table.

```python
assert 2 + 3 * 4 == 14
assert (2 + 3) * 4 == 20
assert -2**2 == -4
assert (-2)**2 == 4
assert 2**3**2 == 512
assert 5 & 3 == 1
assert 5 | 3 == 7
assert 5 ^ 3 == 6
assert 1 << 3 == 8
assert 8 >> 2 == 2
```

Exponentiation binds more tightly than a unary minus on its left and groups right to left. `**` is power; `^` is bitwise exclusive-or. Bitwise operators work on integer bits: `&` keeps shared set bits, `|` keeps either, `^` keeps differing bits, `~` complements and shifts move bit positions. They are distinct from boolean `and` and `or`, which short circuit and return operands.

## Augmented assignment is an operation plus a binding

```python
items = [1]
alias = items
items += [2]
assert alias == [1, 2]
items = items + [3]
assert items == [1, 2, 3]
assert alias == [1, 2]
```

For a list, `+=` mutates in place and then stores the result back to the target. `+` creates a new list. For immutable integers, `+=` instead computes another integer and rebinds the name. Do not assume augmented assignment is always interchangeable with an ordinary addition assignment when aliases or customized operators exist.

A subtle case is `nested = ([1],)`, then `nested[0] += [2]`: the inner list can be extended before assigning back into the tuple raises `TypeError`. The failure does not imply no mutation happened. Prefer explicit mutation when that is the intended contract.

References: [R02: Built-in types and operations](https://docs.python.org/3.14/library/stdtypes.html), [R06: Python data model](https://docs.python.org/3.14/reference/datamodel.html).

---

<a id="page-10"></a>

# Truthiness, comparisons and short circuiting
Section: Values and text

Conditions evaluate an object's truth value. Common false values are `None`, `False`, numeric zero and empty containers. A nonempty string such as `"False"` or `"0"` is true. Python does not interpret the word inside a string as a boolean declaration.

```python
assert not bool("")
assert bool("False")
assert bool("0")
assert not bool([])
assert ("" or "guest") == "guest"
assert ("ready" and 42) == 42
assert 60 <= 75 < 90
value = 0
chosen = 10 if value is None else value
assert chosen == 0
```

`and` stops after a false operand; `or` stops after a true operand. They return an operand, not necessarily a `bool`. `not` returns a boolean. This explains `name or "guest"`, but also its limitation: it replaces every falsy value, including a valid zero. Use an explicit `is None` test when only absence should trigger a default.

## Protect an operation with a condition

```python
values = []
if values and values[0] > 10:
    print("The first value is large")
```

The subscript is not evaluated when the list is empty. This avoids `IndexError` for this local sequence. It is not a general synchronization guarantee if another thread can modify shared state between operations.

Chained comparisons such as `0 <= score <= 100` are readable and evaluate the middle expression once. Membership uses `in`; a dictionary checks keys by default. Identity uses `is`; equality uses `==`. Keep those questions separate: “same object,” “same value” and “contained here” are different operations.

## Common reasoning errors

`if status == "ready" or "waiting":` always enters because `"waiting"` is truthy. Write `if status in {"ready", "waiting"}:`. Likewise, `a and b` does not compare `a` to `b`. Trace which operands execute before trying to simplify a condition.

Source: `lessons/control_flow/branching_loops.py`. References: [R02: Built-in types and operations](https://docs.python.org/3.14/library/stdtypes.html), [R03: Control flow and function definitions](https://docs.python.org/3.14/tutorial/controlflow.html).

---

<a id="page-11"></a>

# Strings: indexing, slicing and immutability
Section: Values and text

A string is an immutable sequence of Unicode code points. Indexing starts at zero; negative indices count from the end. A slice `text[start:stop:step]` includes the start and excludes the stop. Missing bounds use defaults that depend on the direction of the step.

```python
word = "Python"
assert word[0] == "P"
assert word[-1] == "n"
assert word[1:4] == "yth"
assert word[-2:] == "on"
assert word[::2] == "Pto"
assert word[::-1] == "nohtyP"
assert word[999:] == ""
assert word.upper() == "PYTHON"
assert word == "Python"
```

An invalid single index raises `IndexError`; a slice clips out-of-range bounds. A step of zero raises `ValueError`. An empty input has no first character but supports empty slices, which often simplifies boundary handling.

## Build a new value

`word[0] = "J"` fails because strings do not support item assignment. `"J" + word[1:]` creates a new string. Methods such as `.upper()`, `.replace()` and `.strip()` return results; save or use that result. Calling a method and then ignoring its return is a frequent beginner mistake.

Sequence length counts code points, which need not equal the number of visible characters. A letter plus a combining accent may occupy two positions; an emoji sequence may contain several code points. Reversing with `[::-1]` demonstrates slicing, but is not a universal way to reverse human-readable grapheme clusters.

## Readable string literals

`"line\nnext"` contains a newline; `r"line\nnext"` contains a backslash followed by `n`. `repr()` shows escapes so invisible differences can be inspected. A raw string changes escape processing in the literal; it does not add a separate runtime string type. Triple quotes are useful for multiline text and docstrings.

Predict `"python"[2:2]`, `"python"[-99:2]` and `"python"[4:1:-1]`. Answers: `''`, `'py'` and `'oht'`. Trace the indices before running the strings lesson.

Source: `lessons/basics/strings.py`. References: [R01: Python tutorial: numbers and text](https://docs.python.org/3.14/tutorial/introduction.html), [R02: Built-in types and operations](https://docs.python.org/3.14/library/stdtypes.html).

---

<a id="page-12"></a>

# Text pipelines and formatting
Section: Values and text

Text processing is easier to reason about as a pipeline: clean the boundaries, split into tokens, transform each token and combine the results. Decide which whitespace and punctuation are meaningful before writing the operations.

```python
assert "  red,blue  ".strip().split(",") == ["red", "blue"]
assert "a  b\tc".split() == ["a", "b", "c"]
assert "a,,b".split(",") == ["a", "", "b"]
assert " / ".join(["red", "blue"]) == "red / blue"
assert f"Total: {12.5:.2f}" == "Total: 12.50"
assert "Straße".casefold() == "strasse"
```

`.split()` without a separator collapses runs of whitespace and omits empty edge tokens. An explicit separator preserves empty fields. `.strip("ab")` removes any leading or trailing characters from that set; it does not remove the exact substring `"ab"`. Use `.removeprefix()` or `.removesuffix()` for that intent.

`separator.join(parts)` requires string elements. Convert numbers deliberately with `str()` when appropriate. Accumulating fragments and joining expresses a linear construction; repeatedly concatenating a growing string can do substantially more copying.

## The repository's alternating-case implementation

Repository excerpt: `lessons/basics/strings.py:8`.

```python
def alternating_case(text):
    """Lowercase index 0, uppercase index 1, and keep alternating by position."""
    return "".join(
        character.lower() if index % 2 == 0 else character.upper()
        for index, character in enumerate(text)
    )
```

`enumerate()` supplies each original position and character. The conditional expression chooses the transformation; `join()` consumes the generated fragments. Empty input produces no fragments, so the result is `''`. Spaces still count as input positions. Some Unicode case transformations expand to several code points, so output length is not guaranteed to match input length.

## Formatting is a presentation decision

An f-string evaluates expressions inside braces. `:.2f` displays two decimal places; `!r` requests a debugging representation. Keep untrusted text as data rather than evaluating it as a Python expression. Prefer parameterized database operations over using formatted strings to construct SQL.

Try `alternating_case("a bc")`: the result is `'a bC'`. Explain why the space changes which letter becomes uppercase.

References: [R02: Built-in types and operations](https://docs.python.org/3.14/library/stdtypes.html), [R07: Built-in functions](https://docs.python.org/3.14/library/functions.html).

---

<a id="page-13"></a>

# Text, bytes and encoding boundaries
Section: Values and text

`str` represents Unicode text. `bytes` represents an immutable sequence of byte values from 0 to 255. `bytearray` is a mutable byte sequence. Encode text to bytes when crossing a file, network or external-format boundary; decode bytes to text using the format's declared encoding. These are explicit transformations, not interchangeable representations.

```python
text = "café"
encoded = text.encode("utf-8")
assert encoded == b"caf\xc3\xa9"
assert len(text) == 4 and len(encoded) == 5
assert encoded.decode("utf-8") == text
assert encoded[0] == 99
assert encoded[:1] == b"c"
mutable = bytearray(b"cat")
mutable[0] = ord("b")
assert mutable == b"bat"
```

Indexing bytes returns an integer, while slicing returns bytes. Indexing a string returns a one-code-point string. `str(encoded)` produces a representation such as `"b'...'"`; it is not the same as decoding the content. Combining text and bytes directly normally raises `TypeError`, which helps expose a missing boundary decision.

## Decode deliberately

Wrong or incomplete encoded data can raise `UnicodeDecodeError`. The default strict policy makes the problem visible. `errors="ignore"` silently drops information and `errors="replace"` inserts replacement characters; use them only when lossy handling is an explicit requirement. A byte chunk from a stream can end halfway through a multibyte character, so incremental decoding is needed for arbitrary chunk boundaries.

Binary file modes read bytes; text modes decode and can translate newlines. `encoding="utf-8"` documents that part of the storage format. A UTF-8 file is not a Python string until decoded. The tracker's `read_text()` and `write_text()` make the format explicit.

## Equality and human text

Visually similar strings can contain different code-point sequences. Case folding and Unicode normalization address different questions; neither is a blanket substitute for a documented comparison policy. The alternating-case exercise intentionally works by original code-point positions, not visible grapheme clusters.

References: [R02: Built-in types and operations](https://docs.python.org/3.14/library/stdtypes.html), [R07: Built-in functions](https://docs.python.org/3.14/library/functions.html).

---

<a id="page-14"></a>

# Choose the right container
Section: Containers and references

Choose a data structure from the operations and guarantees you need. A list is useful for an ordered changing sequence; a tuple for a fixed sequence of references; a dictionary for key-based lookup; a set for uniqueness and membership. All can be empty, and each has different constraints.

| Type | Order and duplicates | Mutation | Useful operation |
| --- | --- | --- | --- |
| `list` | Sequence order; duplicates allowed | Yes | Append, index, slice |
| `tuple` | Sequence order; duplicates allowed | No outer mutation | Unpack a fixed record |
| `dict` | Insertion order; unique keys | Yes | Look up a value by key |
| `set` | No order guarantee; unique elements | Yes | Membership and set algebra |
| `frozenset` | No order guarantee; unique elements | No | A hashable set value |

```python
items = [3, 1, 1]
point = (10, 20)
profile = {"name": "Ada"}
tags = {"python", "practice", "python"}
x, y = point
assert (x, y) == (10, 20)
assert len(tags) == 2
assert type({}) is dict
assert type(set()) is set
assert type((10,)) is tuple
assert type((10)) is int
```

Dictionary keys and set elements must be hashable. Hashability means an object can supply a stable hash consistent with its equality behavior. “Immutable” is a helpful first approximation, but not a definition: a tuple is hashable only if all its elements are hashable, while ordinary user-defined instances can be identity-hashable and mutable.

## Ordering is part of a contract

Dictionary insertion order is a language guarantee. Updating an existing key does not move it; deleting and reinserting places it at the end. A set does not promise insertion order. Sort a set for predictable display, as the repo's demonstrations do. Do not assume that a display order observed in one process will recur in another.

When interviewing, explain the operations that justify the choice. “A set makes duplicate removal easy” is incomplete if the caller also requires first-occurrence order or unhashable elements.

References: [R02: Built-in types and operations](https://docs.python.org/3.14/library/stdtypes.html), [R04: Data structures tutorial](https://docs.python.org/3.14/tutorial/datastructures.html), [R06: Python data model](https://docs.python.org/3.14/reference/datamodel.html).

---

<a id="page-15"></a>

# Lists and tuples in practice
Section: Containers and references

Lists store references in sequence. `append(x)` adds one object; `extend(iterable)` adds each produced object. `pop()` removes and returns an item, while `remove(value)` deletes the first equal value and raises `ValueError` if absent. Methods that only mutate the list, such as `sort()`, return `None`.

```python
items = [3, 1, 1]
items.append(4)
assert items.pop() == 4
ordered = sorted(items)
assert ordered == [1, 1, 3]
assert items == [3, 1, 1]
assert items.sort() is None
assert items == [1, 1, 3]
items.extend([8, 9])
assert items[-2:] == [8, 9]
```

`sorted()` accepts any iterable and returns a list. `.sort()` changes a list in place. Both are stable: equal keys retain input order. A `key` callable computes the comparison value, usually more clearly than manually rebuilding records. Do not write `items = items.sort()` unless you intend to replace the binding with `None`.

## Fixed references are not deep immutability

```python
nested = ([1], 2)
nested[0].append(3)
assert nested == ([1, 3], 2)
first, *middle, last = [10, 20, 30, 40]
assert first == 10 and middle == [20, 30] and last == 40
```

The tuple's reference at position zero remains the same list; that list can still mutate. Assigning a new reference to `nested[0]` would fail. The tuple is unhashable because its list element is unhashable.

Unpacking checks the number of values unless a starred target absorbs the remainder. It works on iterables, not just tuples. Use it to make structure visible: `for name, age in people` states that each record has two fields.

## Avoid a common iteration bug

Removing from a list while iterating over it can shift later values past the iterator. Build a filtered list, iterate over a snapshot or write an explicit index-based algorithm whose shifts you have accounted for. The repo favors a fresh filtered list for clarity.

Run: `python learn.py sequences`. References: [R04: Data structures tutorial](https://docs.python.org/3.14/tutorial/datastructures.html), [R02: Built-in types and operations](https://docs.python.org/3.14/library/stdtypes.html).

---

<a id="page-16"></a>

# Aliasing, shallow copies and deep copies
Section: Containers and references

Assignment creates another reference. A shallow copy creates a new outer container and reuses references to its elements. A deep copy recursively copies supported contents and uses a memo to handle cycles and preserve repeated-reference structure within the copy. These are different contracts, not progressively “better” operations.

```python
from copy import deepcopy

original = [[1], [2]]
alias = original
shallow = original.copy()
deep = deepcopy(original)
shallow[0].append(99)
assert alias is original
assert shallow is not original
assert shallow[0] is original[0]
assert original == [[1, 99], [2]]
assert deep == [[1], [2]]
```

Visualize the shallow copy as a second outer box whose arrows lead to the same inner lists. Replacing `shallow[0]` changes only that outer box; appending to `shallow[0]` changes the shared inner object. Ask which object an operation actually changes.

## Repetition duplicates references

```python
shared = [[0] * 2] * 2
shared[0][0] = 7
assert shared == [[7, 0], [7, 0]]
independent = [[0] * 2 for _ in range(2)]
independent[0][0] = 7
assert independent == [[7, 0], [0, 0]]
```

The outer multiplication repeats one row reference. The comprehension evaluates its row expression on each iteration, creating independent rows. Multiplication is fine for a row of immutable zero values; the surprise arises when the repeated item is a mutable row.

## Choose ownership deliberately

Copying everything can hide unclear ownership and add memory cost. A file handle or database connection is not a useful candidate for ordinary deep copying. A function can promise to mutate a caller's list, return a fresh outer list or create a deliberately independent snapshot. State which behavior it provides and test the nested case if independence matters.

Run: `python learn.py sequences`. Reference: [R05: Shallow and deep copying](https://docs.python.org/3.14/library/copy.html).

---

<a id="page-17"></a>

# Dictionaries, sets and hashability
Section: Containers and references

A dictionary maps unique hashable keys to values. `mapping[key]` raises `KeyError` when absent; `.get(key, default)` returns the default without inserting it. `.setdefault()` may insert, while `defaultdict` adds factory behavior for missing bracket lookups. Choose whether a missing key is normal or an error.

```python
profile = {"name": "Ayush", "language": "Python"}
assert profile.get("city", "unknown") == "unknown"
assert "city" not in profile
profile["level"] = "learning"
assert list(profile) == ["name", "language", "level"]
assert dict([("a", 1), ("a", 2)]) == {"a": 2}
assert list(dict.fromkeys([3, 1, 3, 2, 1])) == [3, 1, 2]
assert len({1, True, 1.0}) == 1
```

Equal keys must have equal hashes. `1`, `True` and `1.0` compare equal and collapse to one dictionary or set entry. A hash collision alone does not make two distinct keys equal: the table must still resolve equality. A list cannot be a key, and a tuple containing a list cannot be a key either.

## Sets express relationships

```python
left, right = {1, 2, 3}, {3, 4}
assert left | right == {1, 2, 3, 4}
assert left & right == {3}
assert left - right == {1, 2}
assert left ^ right == {1, 2, 4}
assert {1, 2} <= left
left.discard(99)   # absence is allowed; remove(99) would raise
```

`|` is union, `&` intersection, `-` difference and `^` symmetric difference. `<=` checks a subset. Display `sorted(result)` when a stable order is needed. A set's uniqueness follows equality, not textual appearance or identity.

Do not change dictionary size while iterating over its live views. Iterate over `list(mapping)` when intentional removal is needed, or construct a new dictionary. A `.get()` default expression is evaluated before the call, so `.get(key, expensive())` runs `expensive()` even when the key exists.

Run: `python learn.py mappings`. References: [R02: Built-in types and operations](https://docs.python.org/3.14/library/stdtypes.html), [R04: Data structures tutorial](https://docs.python.org/3.14/tutorial/datastructures.html).

---

<a id="page-18"></a>

# Branches, loops and loop else
Section: Control flow

Indentation defines a block. An `if`/`elif`/`else` chain executes the first matching branch. A `for` loop requests items from an iterable; a `while` loop repeats while a condition is true. A useful loop has a clear invariant and a clear reason it will terminate.

```python
def find_even(values):
    for candidate in values:
        if candidate % 2 == 0:
            return candidate
    return None

assert find_even([1, 3, 4]) == 4
assert find_even([]) is None
assert list(range(5, 0, -2)) == [5, 3, 1]
```

`range(start, stop, step)` excludes the stop. Descending iteration needs a negative step. `range(5, 0)` is empty. `break` exits the nearest loop; `continue` skips the rest of the current iteration; `pass` does nothing and can stand in for an unfinished block.

## Else belongs to the loop

```python
candidates = [1, 3, 5]
for candidate in candidates:
    if candidate % 2 == 0:
        print("Found:", candidate)
        break
else:
    print("No even number found")
# No even number found
```

A loop's `else` runs after normal exhaustion, including an empty iterable; it does not run after `break`. A return or an uncaught exception leaves the construct rather than reaching `else`. Read it as “the search finished without a break.” If a helper function with an early return is clearer, use that instead.

## Reason about progress

For a countdown, the invariant might be “remaining is nonnegative,” and the progress step subtracts one. In a search, previously visited items did not match. Thinking this way catches infinite loops, skipped values and misplaced breaks more reliably than adjusting code until one input works.

An extension in Python 3.10+ is structural pattern matching. `match` compares the shape of data and can bind names; it is not a drop-in equivalent of every `if` chain. Keep the simpler construct when matching a single boolean condition.

Run: `python learn.py loops`. References: [R03: Control flow and function definitions](https://docs.python.org/3.14/tutorial/controlflow.html), [R46: Structural pattern matching specification](https://peps.python.org/pep-0634/).

---

<a id="page-19"></a>

# Iteration helpers and comprehensions
Section: Control flow

Use `enumerate()` when you need an item and its position. Use `zip()` to pair inputs. Use unpacking to reveal each record's structure. These tools avoid manually synchronizing indexes and make a loop's purpose easier to see.

```python
assert list(enumerate("cat", start=1)) == [(1, "c"), (2, "a"), (3, "t")]
assert list(zip(["a", "b"], [10])) == [("a", 10)]
try:
    list(zip(["a", "b"], [10], strict=True))
except ValueError:
    pass
else:
    raise AssertionError("Unequal lengths must fail")
assert [n*n for n in range(6) if n % 2 == 0] == [0, 4, 16]
```

Default `zip()` stops at the shortest input. On Python 3.10+, `strict=True` detects unequal lengths as the iterator is consumed. This is valuable when silent truncation would corrupt a relationship between inputs. Merely creating the zip object does not check the whole input.

## Transform and filter are separate decisions

`[transform(x) for x in values if keep(x)]` includes only selected items. `[a(x) if condition(x) else b(x) for x in values]` produces one result per input. Move the `if` and you change the meaning. A dictionary comprehension creates keys and values; a set comprehension deduplicates results.

```python
rows = [[1, 2], [3, 4]]
assert [value for row in rows for value in row] == [1, 2, 3, 4]
assert ["even" if n % 2 == 0 else "odd" for n in range(3)] == [
    "even", "odd", "even"
]
assert {n: n*n for n in range(3)} == {0: 0, 1: 1, 2: 4}
```

Nested comprehension clauses follow the same order as nested ordinary loops. Rewrite one as loops before compressing it. Prefer a regular loop for several actions, complex branching or side effects. A comprehension builds a result eagerly; a generator expression defers production and is consumed once.

Checkpoint: rewrite `extract_even()` from `lessons/control_flow/comprehensions.py` as a loop. Verify it preserves duplicates, input order and the original input list.

References: [R03: Control flow and function definitions](https://docs.python.org/3.14/tutorial/controlflow.html), [R04: Data structures tutorial](https://docs.python.org/3.14/tutorial/datastructures.html), [R07: Built-in functions](https://docs.python.org/3.14/library/functions.html).

---

<a id="page-20"></a>

# Pattern matching and readable dispatch
Section: Control flow

Extension beyond the repo: Python 3.10's `match` statement selects a branch from the shape and contents of a subject. It is useful for structured alternatives such as parsed commands. It is not required when a short `if` chain already states the rule clearly.

```python
def describe_command(command):
    match command:
        case ["add", title] if isinstance(title, str) and title.strip():
            return f"Add: {title.strip()}"
        case ["done", task_id] if type(task_id) is int and task_id > 0:
            return f"Complete: {task_id}"
        case ["list"]:
            return "List tasks"
        case _:
            raise ValueError("Unsupported command shape")

assert describe_command(["add", "  Read  "]) == "Add: Read"
assert describe_command(["done", 2]) == "Complete: 2"
assert describe_command(["list"]) == "List tasks"
```

Each case combines a structural pattern with an optional guard. Here, sequence patterns enforce two or one positions and literal words; captures bind data; guards enforce additional value rules. Cases are attempted in order. The wildcard `_` matches without retaining a useful binding. The tracker itself uses `argparse` and ordinary branches; this is a teaching alternative for already structured input.

## Captures are not ordinary comparisons

A bare name such as `case status:` captures the subject; it does not compare to a previously assigned local constant. Use a literal or a dotted qualified constant for a value pattern. This difference can make a seemingly selective case match everything. Keep names and guards explicit.

Mapping patterns match selected keys and can allow additional keys unless a stricter rule is added. They do not automatically enforce the tracker's exact-field schema. Likewise, a structural match is not authorization or full runtime validation. Patterns and guards should serve a stated contract, not give a false sense that all invalid data has been rejected.

Checkpoint: add a pending-list command to the example and test an unknown shape. Explain why a string subject is not decomposed by a sequence pattern into its characters here.

References: [R03: Control flow and function definitions](https://docs.python.org/3.14/tutorial/controlflow.html), [R46: Structural pattern matching specification](https://peps.python.org/pep-0634/).

---

<a id="page-21"></a>

# Costs, contracts and choosing an algorithm
Section: Control flow

Correctness comes before speed, but the data structure can determine whether a correct solution scales. Big-O describes growth with input size, not a measured duration. State the implementation and assumptions: the table describes common CPython behavior, with dictionary and set lookup assuming ordinary hash distributions.

| Operation | Typical cost | Practical consequence |
| --- | --- | --- |
| List index or final `pop()` | O(1) | Efficient indexed access or stack |
| List `append()` | Amortized O(1) | Occasional resizing is more expensive |
| List membership or front insertion | O(n) | Scans or shifts elements |
| Dict/set lookup | Average O(1), worst O(n) | Requires hashing and equality |
| Comparison sorting | O(n log n) worst case | Ordered inputs may benefit |
| Shallow list copy | O(n) | New outer storage, shared elements |

```python
def unique_in_order(values):
    seen = set()
    result = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result

assert unique_in_order([3, 1, 3, 2, 1]) == [3, 1, 2]
```

This implementation makes the order contract visible. Expected time is O(n) with ordinary hashing and space is O(k) for k distinct values. A list-only membership check can become O(n²). The shorter `list(dict.fromkeys(values))` expresses the same first-occurrence rule for hashable elements.

## Ask before optimizing

Are values hashable? Should equal values such as `True` and `1` be merged? Must duplicates or input order survive? How large is the input, and can it be streamed? These questions can change the solution more than a micro-optimization.

`range` uses a compact arithmetic representation rather than allocating every integer at creation. A generator can avoid storing output, but still does the work for values you consume. Replacing a list with a generator does not remove an algorithm's fundamental time cost.

Revision task: explain why the tracker uses `max(existing_ids) + 1` rather than `len(tasks) + 1`. Sparse IDs break the latter assumption. The scan is O(n), appropriate for a small local learning project.

References: [R02: Built-in types and operations](https://docs.python.org/3.14/library/stdtypes.html), [R34: Profiling Python programs](https://docs.python.org/3.14/library/profile.html), [R35: timeit](https://docs.python.org/3.14/library/timeit.html).

---

<a id="page-22"></a>

# Functions: contracts, returns and arguments
Section: Functions and scope

A function packages a computation behind a name and an interface. Its contract describes accepted inputs, returned outputs, deliberate mutations and possible failures. `def` creates a function object; calling it executes its body. Parameters are names in the definition; arguments are values supplied by a caller.

Repository excerpt: `lessons/functions/arguments.py:8`.

```python
def add(first, second=5):
    """Return a value so the caller can reuse it; printing is a separate concern."""
    return first + second
```

```python
from lessons.functions.arguments import add

assert add(3) == 8
assert add(second=2, first=3) == 5
answer = add(10, 20)
assert answer * 2 == 60
```

Returning a value lets the caller reuse it. Printing writes a presentation to a stream. A function can print and return, but printing is not an implicit return. Falling off the end, or using bare `return`, returns `None`. A return exits only the current function, with cleanup constructs still honored.

## Argument passing follows the object model

When a call binds a parameter, the parameter refers to the supplied object. Rebinding that parameter does not rebind the caller's name. Mutating a supplied list changes the same list the caller references. This is often described as passing by assignment or object sharing.

```python
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

Run: `python learn.py arguments`. References: [R03: Control flow and function definitions](https://docs.python.org/3.14/tutorial/controlflow.html), [R08: Execution model and name binding](https://docs.python.org/3.14/reference/executionmodel.html).

---

<a id="page-23"></a>

# Parameter kinds and useful interfaces
Section: Functions and scope

An interface can distinguish parameters by how callers supply them. Positional-only parameters precede `/`. Positional-or-keyword parameters follow it. `*args` collects extra positional arguments into a tuple; parameters after `*` are keyword-only. `**kwargs` collects unmatched keyword arguments into a dictionary.

```python
def example(first, /, second=5, *extra, verbose=False, **options):
    return first, second, extra, verbose, options

assert example(1, 2, 3, 4, verbose=True, city="Pune") == (
    1, 2, (3, 4), True, {"city": "Pune"}
)
```

The stars in a definition collect arguments. At a call site, `*values` expands an iterable into positional arguments and `**options` expands a mapping into keyword arguments. Duplicate assignments to a parameter raise `TypeError`; they do not silently choose the last value.

Repository excerpt: `lessons/functions/arguments.py:18`.

```python
def describe_person(name, /, *, language="Python", **details):
    """name is positional-only; language is keyword-only; details is a dict."""
    return {"name": name, "language": language, **details}
```

```python
from lessons.functions.arguments import add, describe_person, sum_args

assert add(*[2, 3]) == 5
assert add(1, **{"second": 4}) == 5
assert sum_args() == 0
assert describe_person("Ayush", city="Pune")["city"] == "Pune"
```

Calling `describe_person(name="Ayush")` fails because the required positional-only argument was not supplied. A keyword named `name` can enter `details` when a positional name is supplied. In this particular implementation `**details` appears last in the returned dictionary, so it can override a prior `name` entry. That is an implementation consequence, not runtime signature enforcement of the returned data.

## Choose flexibility where it helps

Keyword-only flags make calls readable: `save(path, overwrite=False)` communicates more than `save(path, False)`. Excessive `**kwargs` can hide typos and unclear contracts. Prefer explicit parameters for stable public options and reserve forwarding for genuine adapters or decorators.

References: [R03: Control flow and function definitions](https://docs.python.org/3.14/tutorial/controlflow.html), [R07: Built-in functions](https://docs.python.org/3.14/library/functions.html).

---

<a id="page-24"></a>

# Defaults, sentinels and mutation policy
Section: Functions and scope

Default expressions are evaluated when the `def` statement executes. A mutable default therefore belongs to the function object and is reused across calls that omit that argument. It is not recreated at the start of every invocation.

```python
def bad_append(item, items=[]):
    items.append(item)
    return items

assert bad_append("a") == ["a"]
assert bad_append("b") == ["a", "b"]
```

That shared state is occasionally intentional, but usually a hidden bug. In the repository, omission means “create a fresh list,” while an explicitly supplied list means “mutate that list.” Checking identity with `None` preserves that distinction even if the supplied list is empty.

Repository excerpt: `lessons/functions/arguments.py:23`.

```python
def append_item(item, items=None):
    """Create a fresh list only when the caller did not provide one.

    A default such as items=[] would be created once when def executes, so
    successive calls would share the same list. Explicitly supplied lists
    are intentionally mutated and returned.
    """
    if items is None:
        items = []
    items.append(item)
    return items
```

```python
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

References: [R03: Control flow and function definitions](https://docs.python.org/3.14/tutorial/controlflow.html), [R08: Execution model and name binding](https://docs.python.org/3.14/reference/executionmodel.html).

---

<a id="page-25"></a>

# Scope, closures and late binding
Section: Functions and scope

For ordinary name lookup in functions, LEGB means Local, Enclosing function, Global module and Builtins. Assignment normally makes a name local to the current function. Reading it before its local binding exists raises `UnboundLocalError`, even if a global variable has the same name.

Repository excerpt: `lessons/functions/scope.py:10`.

```python
def make_counter(start=0):
    """Return a closure with its own saved count."""
    count = start

    def increment():
        nonlocal count  # rebind the variable in the enclosing function
        count += 1
        return count

    return increment
```

```python
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

Run: `python learn.py scope`. Reference: [R08: Execution model and name binding](https://docs.python.org/3.14/reference/executionmodel.html).

---

<a id="page-26"></a>

# Callables, sorting and functional tools
Section: Functions and scope

Functions are objects: they can be stored, passed and returned. A lambda creates a small function from one expression. It has the same closure rules as `def`; it is not automatically faster or isolated from external state. Name a function when its behavior deserves explanation or reuse.

```python
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

```python
from functools import partial

parse_binary = partial(int, base=2)
assert parse_binary("101") == 5
assert sorted(["Python", "a", "code"], key=len) == ["a", "code", "Python"]
```

`partial()` binds selected arguments and returns a callable. It is useful when an API expects one function with a simpler signature. Avoid adding abstraction when a short direct call is clearer.

Checkpoint: predict what happens if the same `map` object is passed to two consumers. The first consumer advances it; the second receives only what remains. If two independent traversals are required, create fresh iterators from a reusable source or materialize a bounded result intentionally.

Run: `python learn.py functional`. References: [R07: Built-in functions](https://docs.python.org/3.14/library/functions.html), [R11: functools: wraps, caching and partial](https://docs.python.org/3.14/library/functools.html).

---

<a id="page-27"></a>

# Recursion and decomposing a problem
Section: Functions and scope

Extension beyond the repo: recursion means a function calls itself directly or indirectly. A correct recursive design needs a base case, a smaller subproblem and a way to combine the answer. The same reasoning applies to directory trees, nested expressions and hierarchical data.

```python
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

References: [R03: Control flow and function definitions](https://docs.python.org/3.14/tutorial/controlflow.html), [R06: Python data model](https://docs.python.org/3.14/reference/datamodel.html).

---

<a id="page-28"></a>

# Type hints and runtime validation
Section: Functions and scope

Type hints communicate intended interfaces to readers, editors and static analyzers. Python does not normally enforce annotations at call time. `def double(n: int) -> int: return n * 2` can still receive a string and return repeated text if no runtime check prevents it.

```python
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

References: [R15: typing and structural protocols](https://docs.python.org/3.14/library/typing.html), [R14: dataclasses](https://docs.python.org/3.14/library/dataclasses.html).

---

<a id="page-29"></a>

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

```python
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

Run: `python learn.py files`. References: [R07: Built-in functions](https://docs.python.org/3.14/library/functions.html), [R17: pathlib](https://docs.python.org/3.14/library/pathlib.html), [R42: tempfile](https://docs.python.org/3.14/library/tempfile.html).

---

<a id="page-30"></a>

# Paths, streaming and filesystem boundaries
Section: Files, errors and resources

`Path("notes.txt")` describes a path; it does not create a file. Relative paths resolve against the process's current working directory. A path built from `Path(__file__)` is anchored to a module location. The tracker uses the latter to keep its default storage predictable across invocation directories.

```python
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

References: [R17: pathlib](https://docs.python.org/3.14/library/pathlib.html), [R42: tempfile](https://docs.python.org/3.14/library/tempfile.html).

---

<a id="page-31"></a>

# Exceptions and useful failure contracts
Section: Files, errors and resources

An exception carries a failure up the call stack until a matching handler catches it. Syntax errors prevent a code unit from being parsed. Runtime errors occur while executing valid syntax. Catch the failures you can recover from or translate into a clearer boundary error; let unexpected defects retain their traceback.

Repository excerpt: `lessons/files_exceptions/handling_errors.py:8`.

```python
def parse_integer(text):
    """Parse text as int, or raise a helpful ValueError with the original cause."""
    try:
        return int(text)
    except ValueError as error:
        raise ValueError(f"Expected a whole number, got {text!r}") from error
```

```python
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

Run: `python learn.py exceptions`. Reference: [R09: Errors and exceptions tutorial](https://docs.python.org/3.14/tutorial/errors.html).

---

<a id="page-32"></a>

# Context managers and dependable cleanup
Section: Files, errors and resources

A context manager defines entering and leaving a managed operation. `with expression as value` obtains the manager, calls its enter method and binds the returned value. Its exit method receives exception information on failure and runs for normal block exit too. Returning a truthy result from exit suppresses the active exception, so do that only as an intentional contract.

```python
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

References: [R13: contextlib and resource management](https://docs.python.org/3.14/library/contextlib.html), [R06: Python data model](https://docs.python.org/3.14/reference/datamodel.html).

---

<a id="page-33"></a>

# Classes, instances and bound methods
Section: Objects and protocols

A class defines a type and groups related behavior. An instance holds particular state. Calling a normal class creates an instance through `__new__` and initializes it through `__init__`. `__init__` initializes an already created object; it must return `None`.

```python
from lessons.oop.classes import Dog

first = Dog("Labrador", "Jenny")
second = Dog("Husky", "Sammy")
first.tricks.append("sit")
assert first.tricks == ["sit"]
assert second.tricks == []
assert first.bark(10) == Dog.bark(first, 10)
assert first.name == "Jenny"
```

`self` is the conventional first parameter for instance methods. Accessing `first.bark` produces a bound method that supplies `first` when called. It is a conventionally named parameter, not a magic keyword. You still supply the ordinary method arguments, such as the age in this example.

## State belongs at the right level

The repo's `Dog.__init__` assigns breed, name and a new tricks list to each instance. Creating that list on each initialization prevents unrelated dogs from sharing training state. Methods that change state should maintain a coherent invariant; freely assigning attributes is convenient but does not by itself enforce one.

Choose a function for a simple stateless calculation. Choose a class when identity, related state and behavior, a useful protocol or a substitutable implementation makes the model clearer. Turning every helper into a class adds ceremony without necessarily improving design.

## Read a method as a function with context

The method can read `self.name`, use ordinary parameters and return a value. A returned greeting can be printed, tested or sent elsewhere. The repo keeps demonstration printing in `main()` so importing the model does not launch an interactive workflow.

Checkpoint: make two dogs, add a trick to only one and explain why the other is unchanged. Then compare this with a deliberately shared class-level list in a scratch file.

Run: `python learn.py classes`. References: [R10: Classes tutorial](https://docs.python.org/3.14/tutorial/classes.html), [R06: Python data model](https://docs.python.org/3.14/reference/datamodel.html).

---

<a id="page-34"></a>

# Class state, shadowing and method kinds
Section: Objects and protocols

A class attribute is found through attribute lookup when an instance has not supplied its own value. Assigning `instance.attribute` usually creates or updates instance state; it does not generally rewrite the class attribute. Descriptors such as properties can customize this behavior.

```python
from lessons.oop.classes import Dog

first, second = Dog("Lab", "Jenny"), Dog("Husky", "Sammy")
assert Dog.species == first.species == second.species == "mammal"
first.species = "instance override"
assert first.species == "instance override"
assert second.species == Dog.species == "mammal"
```

If a class attribute is a list and an instance executes `self.items.append(x)`, lookup can find the shared class list and mutate it. That differs from rebinding `self.items`. Mutable per-instance state belongs in `__init__` or a dataclass `default_factory`.

## Instance, class and static methods

An instance method receives the instance. A `classmethod` receives the class used to access it and is useful for alternative constructors. A `staticmethod` receives no automatic instance or class argument; it is a function kept in a class namespace.

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    @classmethod
    def origin(cls):
        return cls(0, 0)

    @staticmethod
    def valid_coordinate(value):
        return isinstance(value, (int, float))

point = Point.origin()
assert (point.x, point.y) == (0, 0)
assert Point.valid_coordinate(2.5)
```

Using `cls(...)` in an alternative constructor lets subclasses participate, provided their initialization contract is compatible. A static method can be appropriate for a closely related helper, though a module function is often simpler. The validator above is deliberately permissive and accepts booleans; use a stricter rule if the domain rejects them.

References: [R07: Built-in functions](https://docs.python.org/3.14/library/functions.html), [R10: Classes tutorial](https://docs.python.org/3.14/tutorial/classes.html), [R16: Descriptor how-to](https://docs.python.org/3.14/howto/descriptor.html).

---

<a id="page-35"></a>

# Special methods and Python protocols
Section: Objects and protocols

Special methods let objects participate in language operations. `__str__` serves a readable display; `__repr__` serves debugging and should be unambiguous when practical. `__len__` supports `len()`. A meaningful protocol is better than adding a special method only because the syntax is available.

```python
from lessons.oop.classes import Dog

dog = Dog("Labrador", "Jenny")
assert str(dog) == "Dog named Jenny"
assert repr(dog) == "Dog(breed='Labrador', name='Jenny')"
assert len(dog) == 5
assert bool(dog)
assert not bool(Dog("Lab", ""))
```

The repository uses name length as a deliberately small protocol demonstration. Since `Dog` has no `__bool__`, truth testing falls back to `__len__`. An empty name makes the dog falsy. In a real domain model that may be misleading, which is a reason to avoid a length protocol when no natural length exists.

## Equality and hashing must agree

`__eq__` can define value equality. If two hashable objects compare equal, their hashes must be equal. Mutating a field used by hashing while an object is a dictionary key can make future lookup inconsistent. Python typically makes a class that defines equality but no hash unhashable; do not restore hashing without a stable policy.

Return `NotImplemented` from an unsupported comparison so Python can try the other operand's implementation or its fallback. It is a special value, distinct from raising `NotImplementedError` for an unfinished method.

## Protocols support polymorphism

A `for` loop needs an iteration interface; `with` needs resource-management methods. The object need not inherit from a particular application class if it provides the required behavior. Many implicit special-method lookups are performed on the type, so assigning a special method to one instance does not necessarily change operators for that instance.

Revision prompt: explain why overriding `__repr__` does not create a serialization format. A debugging string is for inspection; persistence needs a stable, validated contract.

References: [R06: Python data model](https://docs.python.org/3.14/reference/datamodel.html), [R02: Built-in types and operations](https://docs.python.org/3.14/library/stdtypes.html).

---

<a id="page-36"></a>

# Inheritance, super and composition
Section: Objects and protocols

Inheritance models a substitutable “is a” relationship. Composition stores a collaborator to model “has a.” The repository's `Cat` specializes `Animal`; its `Owner` holds a pet. Both techniques reuse behavior, but they create different dependencies and extension points.

Repository excerpt: `lessons/oop/inheritance.py:21`.

```python
class Cat(Animal):
    def __init__(self, name, indoor=True):
        super().__init__(name)
        self.indoor = indoor

    def speak(self):
        return f"{self.name} meows"
```

```python
from lessons.oop.inheritance import Animal, Cat, Owner

cat = Cat("Milo")
assert isinstance(cat, Animal)
assert cat.speak() == "Milo meows"
assert cat.indoor is True
assert Owner("Ayush", cat).introduce() == "Ayush's pet says: Milo meows"
```

`super()` delegates according to the method resolution order, or MRO. In this simple example it reaches `Animal.__init__`. In multiple inheritance it means the next implementation in the MRO, which may not be a single intuitively chosen “parent.” Cooperative methods need compatible calling conventions.

## Substitution is a behavioral promise

A derived object should support the expectations of code written for the base abstraction. If a subtype unexpectedly rejects valid base inputs or breaks promised outcomes, the inheritance relationship is questionable even if `isinstance()` returns true. Reuse alone is not sufficient justification.

Composition can replace a storage adapter, formatter or clock without building a deep class hierarchy. In the tracker, storage and domain functions are already separate modules; an adapter object becomes useful when several interchangeable storage implementations actually exist.

## Duck typing

The `Owner` annotation says `Animal`, but runtime execution calls `pet.speak()` without enforcing that annotation. Another object with a suitable `speak()` method may work. Static typing can describe this structural requirement with a protocol. Runtime success still depends on behavior, not merely the method's name.

Try adding another speaking object to the lesson's animal list. Explain which operations require actual inheritance and which only need the interface.

Run: `python learn.py inheritance`. References: [R10: Classes tutorial](https://docs.python.org/3.14/tutorial/classes.html), [R15: typing and structural protocols](https://docs.python.org/3.14/library/typing.html).

---

<a id="page-37"></a>

# Dataclasses and explicit invariants
Section: Objects and protocols

A dataclass generates routine methods from declared fields, usually including initialization, representation and equality. It saves repetitive code; it is not an input-validation engine. Equality compares field values using those fields' own equality behavior.

Repository excerpt: `projects/task_tracker/model.py:6`.

```python
@dataclass
class Task:
    id: int
    title: str
    done: bool = False
```

```python
from dataclasses import asdict, dataclass, field
from projects.task_tracker.model import Task

@dataclass
class Notebook:
    title: str
    notes: list[str] = field(default_factory=list)

first, second = Notebook("A"), Notebook("B")
first.notes.append("revision")
assert second.notes == []
assert Task(1, "Read") == Task(1, "Read", False)
assert asdict(Task(1, "Read")) == {"id": 1, "title": "Read", "done": False}
```

`default_factory=list` creates a separate list per instance. An ordinary shared mutable default is unsuitable. `asdict()` converts fields into a dictionary recursively, with deep copying for other values; do not assume it is a cheap zero-copy view of a large object graph.

## Construction and later mutation

`__post_init__` can check values after generated initialization. That check does not automatically intercept later assignments. A property, an immutable design or validation at every state-changing operation may be needed if an invariant must always hold.

`frozen=True` prevents ordinary field assignment but does not recursively freeze nested objects. A frozen dataclass containing a list still refers to a mutable list and may not be hashable. `slots=True`, available at the guide's Python 3.10 baseline, can reduce per-instance attribute overhead and restrict ordinary new attributes; it is not a privacy mechanism.

The tracker's storage validates records before constructing `Task` objects. The model expects valid domain objects and deliberately does not recheck every possible direct Python construction. Understand that boundary before reusing the model as a general-purpose public API.

References: [R14: dataclasses](https://docs.python.org/3.14/library/dataclasses.html), [R15: typing and structural protocols](https://docs.python.org/3.14/library/typing.html).

---

<a id="page-38"></a>

# Properties, descriptors and encapsulation
Section: Objects and protocols

Extension beyond the repo: a property provides attribute syntax with controlled access. It is useful when a value needs validation or computation while callers use an ordinary attribute interface. A leading underscore marks an implementation detail by convention; it does not prevent access.

```python
class PageCount:
    def __init__(self, pages):
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if type(value) is not int:
            raise TypeError("pages must be an integer")
        if value < 0:
            raise ValueError("pages must be non-negative")
        self._pages = value

book = PageCount(120)
book.pages = 0
assert book.pages == 0
```

This validates ordinary assignment both during initialization and afterward. The backing `_pages` remains accessible; encapsulation communicates a supported interface rather than building a security boundary. Double-leading-underscore names are name-mangled mainly to reduce accidental collisions in inheritance, not to encrypt or hide data.

## The descriptor connection

A descriptor is an object with methods such as `__get__`, `__set__` or `__delete__` that customize attribute access when used on a class. Properties are descriptors. Functions also implement descriptor behavior, which is how accessing a function through an instance creates a bound method.

For ordinary lookup, a data descriptor on the class takes precedence over an instance dictionary entry; non-data descriptors can be shadowed by instance attributes. `__getattribute__` participates in every normal attribute access, while `__getattr__` is a fallback for missing attributes. Overriding these broadly can create recursion and obscure behavior.

Use the smallest mechanism that expresses the rule: a plain attribute, then a property, then a reusable descriptor if several fields share a meaningful pattern. Advanced machinery should reduce duplicated rules rather than conceal simple ones.

References: [R16: Descriptor how-to](https://docs.python.org/3.14/howto/descriptor.html), [R06: Python data model](https://docs.python.org/3.14/reference/datamodel.html).

---

<a id="page-39"></a>

# Abstract interfaces and structural protocols
Section: Objects and protocols

Extension beyond the repo: interfaces let code depend on a required behavior instead of a concrete implementation. An abstract base class can define a nominal family and prevent construction until required methods are implemented. A typing `Protocol` describes structural compatibility for static analysis.

```python
from typing import Protocol

class Speaker(Protocol):
    def speak(self) -> str:
        ...

class Bell:
    def speak(self) -> str:
        return "ring"

def announce(speaker: Speaker) -> str:
    return speaker.speak()

assert announce(Bell()) == "ring"
```

`Bell` does not inherit from `Speaker`. Its shape satisfies the interface for a type checker. Python still executes the method call normally; the annotation does not validate it at runtime. An interface must also have a semantic contract, such as “returns a string without mutating the caller's state.” A matching method name alone cannot guarantee that.

## Choose the lightest useful boundary

The repo already uses plain functions effectively. You do not need to retrofit every lesson into a hierarchy. A storage protocol can become useful when JSON and SQLite adapters must share a tested contract. Until then, module functions and dependency injection may be enough.

An abstract base class is suitable when shared behavior or explicit enrollment in a family matters. A protocol is suitable when independently developed objects should work by shape. Runtime-checkable protocols support limited checks and do not become full runtime schema validation.

## Test substitutability

Run the same contract tests against every implementation: missing storage, valid round-trip, malformed input, stable IDs and failure preservation. If one adapter silently returns an empty list on corruption while another raises, the apparent interface hides a real behavioral mismatch.

Checkpoint: describe the minimum interface a read-only tracker report needs. It may only require a sequence of task-like records, not permission to save or mutate storage. Smaller interfaces narrow accidental capabilities and simplify tests.

References: [R15: typing and structural protocols](https://docs.python.org/3.14/library/typing.html), [R10: Classes tutorial](https://docs.python.org/3.14/tutorial/classes.html).

---

<a id="page-40"></a>

# Iterables, iterators and exhaustion
Section: Iterators and decorators

An iterable can supply an iterator through `iter()`. An iterator tracks progress, supplies the next value through `next()` and raises `StopIteration` when exhausted. An iterator's `iter()` returns itself. A list is reusable; a particular iterator over that list is consumed as it advances.

```python
values = [10, 20, 30]
iterator = iter(values)
assert iter(iterator) is iterator
assert next(iterator) == 10
assert list(iterator) == [20, 30]
assert list(iterator) == []
assert next(iterator, "done") == "done"
assert list(values) == [10, 20, 30]
assert list(iter(values)) == [10, 20, 30]
```

A `for` loop obtains an iterator and repeatedly requests values until exhaustion. It does not need indexes or a known length. That is why the same loop can process a list, an open file, a `map` or a generator. A second traversal needs a new iterator from a reusable source, not another reference to the consumed iterator.

## Laziness changes timing

Iterator construction may do little work; errors may occur during consumption. A function promising an iterable should document whether it can be consumed repeatedly. A function accepting an iterable must avoid secretly requiring two passes unless it deliberately materializes it or narrows the accepted interface.

```python
squares = (number * number for number in range(4))
assert next(squares) == 0
assert sum(squares) == 14
assert sum(squares) == 0
```

The second sum is zero because there are no remaining values, not because the original mathematical series changed. This is a common bug in logging, validation and test code that consumes an iterator before the real computation.

Checkpoint: what happens if you call `list(stream)` for debugging before the processing loop? For an open file it advances to the end. Reopen it, rewind when supported or inspect without consuming the whole pipeline.

References: [R06: Python data model](https://docs.python.org/3.14/reference/datamodel.html), [R07: Built-in functions](https://docs.python.org/3.14/library/functions.html), [R12: itertools: iterator building blocks](https://docs.python.org/3.14/library/itertools.html).

---

<a id="page-41"></a>

# Implement an iterator protocol
Section: Iterators and decorators

Extension beyond the repo: implementing an iterator once makes the protocol concrete. An iterator's `__iter__` returns itself; `__next__` returns the next item or raises `StopIteration`. A reusable iterable should instead supply a fresh iterator when independent traversals are requested.

```python
class Countdown:
    def __init__(self, start):
        if type(start) is not int:
            raise TypeError("start must be an integer")
        if start < 0:
            raise ValueError("start must be non-negative")
        self.remaining = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.remaining == 0:
            raise StopIteration
        value = self.remaining
        self.remaining -= 1
        return value

countdown = Countdown(3)
assert iter(countdown) is countdown
assert next(countdown) == 3
assert list(countdown) == [2, 1]
assert list(countdown) == []
```

The object combines data and progress, so a second `for` loop over the same object continues rather than restarts. Once exhausted, this iterator keeps raising `StopIteration`. Resetting it implicitly in `__iter__` would make nested or repeated consumers interfere in surprising ways.

## Separate the collection from the cursor

A reusable countdown description could store only the starting value and have `__iter__` return a new `Countdown(start)` each time. Two loops would then have separate cursors. The distinction mirrors a list and an iterator over that list.

A generator function usually expresses the same production logic with less boilerplate and automatically retains local state. A custom iterator class is useful when progress needs an explicit public object, additional methods or integration with another protocol. Choose it because that state model helps, not to avoid the `yield` keyword.

References: [R06: Python data model](https://docs.python.org/3.14/reference/datamodel.html), [R07: Built-in functions](https://docs.python.org/3.14/library/functions.html).

---

<a id="page-42"></a>

# Generator functions and suspended state
Section: Iterators and decorators

A function containing `yield` is a generator function. Calling it returns a generator object; execution of its body begins when a value is requested. At each yield, local state is suspended and later resumed. Reaching the end exhausts the generator.

Repository excerpt: `lessons/advanced/generators.py:16`.

```python
def fibonacci(count):
    """Yield count Fibonacci values, starting with 1, 1. Negative counts fail.

    Because this is a generator function, validation happens on iteration,
    not when fibonacci(count) creates the generator object.
    """
    if count < 0:
        raise ValueError("count must be non-negative")
    first, second = 1, 1
    for _ in range(count):
        yield first
        first, second = second, first + second
```

```python
from lessons.advanced.generators import fibonacci

iterator = fibonacci(6)
assert next(iterator) == 1
assert next(iterator) == 1
assert list(iterator) == [2, 3, 5, 8]
assert list(iterator) == []
bad = fibonacci(-1)   # body has not executed yet
try:
    next(bad)
except ValueError:
    pass
else:
    raise AssertionError("Negative count must fail on iteration")
```

The simultaneous assignment computes both right-hand expressions from the previous values before rebinding `first` and `second`. Updating `first` and then using that new value for `second` would change the sequence.

## Validation timing is part of the API

If invalid arguments must fail at construction time, make an ordinary outer function validate and return a nested generator. A generator's own body cannot validate before it begins executing. The repo deliberately tests the lazy timing of the negative-count error.

A generator can retain referenced objects for its lifetime. It avoids storing every produced value, but can still hold a large input or external resource. Prefer structured resource ownership when a consumer may stop early. `yield from other` delegates iteration and generator interactions rather than requiring a hand-written forwarding loop.

Run: `python learn.py generators`. References: [R06: Python data model](https://docs.python.org/3.14/reference/datamodel.html), [R12: itertools: iterator building blocks](https://docs.python.org/3.14/library/itertools.html).

---

<a id="page-43"></a>

# Streaming pipelines and iterator tools
Section: Iterators and decorators

Compose small stages to process data incrementally: read an item, filter it, transform it and reduce it. Laziness can lower peak memory and provide an early result. It also moves failures later and makes repeated traversal less automatic.

```python
from itertools import accumulate, chain, islice
from lessons.advanced.generators import cubes

assert list(islice(cubes(1_000_000), 3)) == [0, 1, 8]
assert list(chain([1, 2], [3])) == [1, 2, 3]
assert list(accumulate([2, -1, 3])) == [2, 1, 4]

def running_totals(values):
    total = 0
    for value in values:
        total += value
        yield total

assert list(running_totals(iter([2, -1, 3]))) == [2, 1, 4]
```

`islice` consumes only the relevant portion of an iterator, though reaching its starting point still requires consuming earlier values. `chain` visits inputs sequentially. `accumulate` provides running reductions. These tools can replace repeated indexing or eager intermediate lists.

## Know which tools buffer

`itertools.tee()` creates independent traversal positions by buffering items needed by slower consumers. If one consumer races far ahead, that buffer can grow significantly. It is not a free independent copy of an arbitrary stream and is not a general cross-thread handoff mechanism.

`groupby()` groups adjacent equal keys, not all matching values in the whole dataset. Its group iterators share the underlying source. Sort first only when global grouping is required and the ordering cost and memory fit the task; otherwise use a dictionary-based accumulation with a clear memory bound.

## A pipeline's contract includes failure

Specify what happens if parsing fails after earlier results were emitted. A caller cannot pretend no work happened if it has already acted on those results. For large imports, consider bounded batches, rejected-record reporting and transactional commit units.

Checkpoint: a generator processes ten million lines using little intermediate memory, but the caller finishes with `list(results)`. Explain which memory benefit remains and which disappears.

References: [R12: itertools: iterator building blocks](https://docs.python.org/3.14/library/itertools.html), [R06: Python data model](https://docs.python.org/3.14/reference/datamodel.html).

---

<a id="page-44"></a>

# Decorators: replacing a callable safely
Section: Iterators and decorators

A decorator receives a callable and returns its replacement. `@announce` above a definition means `greet = announce(greet)` after the function is created. Decoration occurs when the definition executes; the wrapper's body runs when the replacement is called.

Repository excerpt: `lessons/advanced/decorators.py:10`.

```python
def announce(function):
    """Log before/after a call while preserving its result and metadata."""

    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Before {function.__name__}")
        result = function(*args, **kwargs)
        print(f"After {function.__name__}")
        return result

    return wrapper
```

```python
from contextlib import redirect_stdout
from io import StringIO
from lessons.advanced.decorators import greet

output = StringIO()
with redirect_stdout(output):
    result = greet("Ayush", punctuation=".")
assert result == "Hello, Ayush."
assert output.getvalue().splitlines() == ["Before greet", "After greet"]
assert greet.__name__ == "greet"
assert greet.__wrapped__("Ada") == "Hello, Ada!"
```

The wrapper forwards positional and keyword arguments, returns the original result and lets exceptions propagate. `wraps()` copies useful metadata and adds `__wrapped__`, which supports inspection and access to the original function. It does not automatically make every wrapper behavior identical to the original.

## Observe the failure path

In this implementation, an exception skips the `After` print. If the after-action must always run, put it in `finally`. If it means “successful completion,” the existing placement is appropriate. Naming the meaning of a log entry helps avoid misleading telemetry.

Two decorators stack from the inside out: `@outer` above `@inner` produces `outer(inner(function))`. Call order and side effects depend on that nesting. A synchronous wrapper also does not automatically await an async function or finish consuming a generator; specialized wrappers need the correct execution model.

Run: `python learn.py decorators`. References: [R11: functools: wraps, caching and partial](https://docs.python.org/3.14/library/functools.html), [R03: Control flow and function definitions](https://docs.python.org/3.14/tutorial/controlflow.html).

---

<a id="page-45"></a>

# Configurable decorators, caching and effects
Section: Iterators and decorators

A parameterized decorator has three layers: configuration, decoration and invocation. Validate configuration once, capture it in a closure and keep call forwarding explicit. The repository's repeat exercise uses this pattern.

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

@repeat(3)
def double(number):
    return number * 2

assert double(4) == [8, 8, 8]
```

Zero repetitions return an empty list and never invoke the wrapped function. An exception stops later repetitions. Repetition repeats side effects too: decorating a payment, file append or task creation is not equivalent to repeating a pure arithmetic calculation.

## Caching changes the contract

`functools.lru_cache` can reuse results for hashable argument keys and bound memory by entry count. It suits repeatable computations whose relevant inputs are captured by the key. Mutable global state, stale external data and cached mutable results complicate correctness. If a returned list is cached, callers may mutate the shared cached value.

Cache synchronization protects internal structure but does not guarantee only one computation on simultaneous misses. A cache also needs an invalidation policy, memory budget and visibility into hit rate. Do not use caching to hide an inefficient algorithm before measuring it.

Practice: create a pure recursive Fibonacci function with caching and compare it to the repo's iterative generator. Explain the difference between computing one indexed value repeatedly and streaming the first n values.

References: [R11: functools: wraps, caching and partial](https://docs.python.org/3.14/library/functools.html), [R12: itertools: iterator building blocks](https://docs.python.org/3.14/library/itertools.html).

---

<a id="page-46"></a>

# Modules, packages and import behavior
Section: Modules and environments

A module is a namespace containing Python definitions and statements. A regular package groups modules and normally contains `__init__.py`; namespace packages are an intentional exception. An import finds a module, initializes it when necessary and binds a name in the importing namespace.

```python
from lessons.modules.sample_package import greetings
from lessons.modules.sample_package.reports.summary import report

assert greetings.greet("Ayush") == "Hello from a module, Ayush!"
assert report([2, 4, 6]) == "Count: 3, total: 12"
```

The package tree gives meaning to the dotted names. `from module import name` binds the current referenced object locally; it is not a permanent live alias to every later rebinding of `module.name`. Mutations of a shared object can still be visible, following the ordinary object model.

## Import is execution

Python normally caches initialized modules in `sys.modules` for the interpreter session. Reimporting usually reuses the module rather than executing its top level again. Definitions, decorator application and class bodies still run during the initial import. A main guard only protects statements inside that guard.

Avoid prompts, file writes and demonstration output at import time. The repository tests that course and project modules import quietly. Imports that require a running service or hidden local file make reusable helpers harder to test and inspect.

## Circular imports signal a dependency question

If A imports B while B imports A, one may observe the other before initialization is complete. Move shared concepts into a lower-level module or restructure responsibilities. A local import can solve a narrow timing need, but should not conceal an unclear dependency graph.

Do not name a local file `json.py`, `random.py` or `typing.py` if it shadows the standard library module you intend to import. Inspect a module's `__file__` when the imported implementation is surprising.

Run: `python learn.py imports`. Reference: [R27: Modules tutorial](https://docs.python.org/3.14/tutorial/modules.html).

---

<a id="page-47"></a>

# Entry points and command-line behavior
Section: Modules and environments

When a file is executed as the top-level program, its `__name__` is `"__main__"`. When imported, it normally has its module name. A main guard separates reusable definitions from an executable demonstration.

```python
def main(argv=None):
    # Parse arguments or call a small demonstration here.
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
```

`python -m package.module` locates a module through the import system and executes it as a program. `python -m projects.task_tracker` executes the package's `__main__.py`. This avoids treating a deeply nested file as an isolated script with a different import context.

## Parse once at the boundary

The tracker accepts `main(argv=None)` so tests can supply an argument list directly. `argparse` builds help text, validates command structure and converts integer IDs. Domain functions never parse command-line strings themselves.

```console
python -m projects.task_tracker --help
python -m projects.task_tracker --file .practice/demo.json add "Read"
python -m projects.task_tracker --file .practice/demo.json list
```

The global `--file` option goes before the subcommand in this parser. Quote a title containing spaces so the shell sends it as one argument. The explicit file in this example is persistent practice storage, unlike the disposable lesson files.

## Three output channels

Standard output carries normal results. Standard error carries diagnostics. The process exit status lets another program detect success or failure without scraping messages. The tracker uses 0 for success, 1 for handled storage/domain failures and 2 for argument errors.

Returning an integer from `main()` makes it testable; `raise SystemExit(main())` at the program boundary translates that result into a process status. Exiting deep inside a model function would remove that control from callers.

References: [R27: Modules tutorial](https://docs.python.org/3.14/tutorial/modules.html), [R29: argparse](https://docs.python.org/3.14/library/argparse.html).

---

<a id="page-48"></a>

# Environments, style and project hygiene
Section: Modules and environments

The maintained course requires only the standard library. For projects that add packages, a virtual environment isolates a project's installed dependencies from other projects. It does not isolate the operating system or make arbitrary code trustworthy.

```console
python -m venv .venv
# Windows PowerShell, if activation is allowed:
.venv\Scripts\Activate.ps1
# You can also call the environment interpreter directly:
.venv\Scripts\python.exe -m pip --version
```

On POSIX shells, activation is normally `source .venv/bin/activate`. Activation is optional; using the environment's interpreter directly works too. `python -m pip` ties package installation to the selected interpreter, reducing the common mismatch between a `pip` executable and the Python used to run code.

## Readable code is part of the contract

Use descriptive `snake_case` functions and variables, `PascalCase` classes and clear constants. A docstring states purpose and important contract details. A comment explains why a surprising choice exists. Good naming and short functions reduce the need for comments that merely restate each line.

The repo's optional Ruff configuration targets Python 3.10 and basic error checks. Its tests use `unittest`. Formatting and linting catch different issues from tests: a clean style report does not establish correct behavior, while passing examples do not establish readability or complete coverage.

## Preparing a reusable package

Extension beyond the repo: distribution metadata, a build system, version policy and installation tests matter when code is shipped as a package. The existing `pyproject.toml` contains lint configuration; do not assume that alone makes the repo a configured distributable project. Consult the official packaging tutorial before adding a build configuration.

Keep generated caches and local environments out of version control. Keep the archived notes unchanged and update the maintained lesson, its exercise and its answer together when a behavior contract changes.

References: [R28: Virtual environments tutorial](https://docs.python.org/3.14/tutorial/venv.html), [R38: PEP 8: Python style](https://peps.python.org/pep-0008/), [R45: Packaging Python projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/).

---

<a id="page-49"></a>

# Counter, defaultdict, namedtuple and deque
Section: Standard-library toolbox

Specialized containers make common intentions explicit. `Counter` counts hashable values. `defaultdict` supplies a missing value through a factory. `namedtuple` gives names to fixed tuple positions. `deque` supports efficient appends and pops at both ends and is a better queue than repeatedly removing a list's first element.

```python
from collections import Counter, defaultdict, deque, namedtuple

counts = Counter("Python python code".casefold().split())
assert counts["python"] == 2
assert counts["missing"] == 0
assert "missing" not in counts
groups = defaultdict(list)
groups["fruit"].append("apple")
assert groups.get("missing") is None
assert "missing" not in groups
assert groups["missing"] == []
assert "missing" in groups
Point = namedtuple("Point", "x y")
point = Point(10, 20)
assert point.x == point[0] == 10
assert point._replace(x=5) == Point(5, 20)
queue = deque(["first", "second"])
assert queue.popleft() == "first"
```

Missing bracket access on a `Counter` returns zero without inserting the key. Missing bracket access on a `defaultdict` calls its factory and inserts the result. `.get()` does not trigger that factory. A read that uses brackets can therefore mutate a `defaultdict`; that is significant in reports and tests.

## Count what the contract calls a word

The exercise counts whitespace-separated tokens after `.casefold()`. `"code"` and `"code!"` remain distinct. A different tokenizer may be sensible, but silently stripping punctuation changes the exercise's specified behavior. Similar care is needed with Unicode normalization and language-specific word boundaries.

A named tuple's positions cannot be reassigned, but a field can still reference a mutable object. Its generated `_replace()` returns a new tuple-like value. Choose a dataclass when a domain record benefits from mutable state or generated methods with more customization.

Run: `python learn.py collections`. Reference: [R19: collections](https://docs.python.org/3.14/library/collections.html).

---

<a id="page-50"></a>

# Dates, durations and time zones
Section: Standard-library toolbox

`date` represents a calendar date; `time` a time of day; `datetime` combines them; `timedelta` represents a duration. Calendar validity is checked by constructors and parsers. Fixed examples make the repo's date lesson repeatable regardless of the day you run it.

```python
from datetime import date, datetime, timedelta, timezone

start = date(2024, 2, 28)
assert (date(2024, 3, 1) - start).days == 2
assert date.fromisoformat("2024-11-03") == date(2024, 11, 3)
duration = timedelta(days=1, seconds=30)
assert duration.seconds == 30
assert duration.total_seconds() == 86430.0
utc = datetime(2024, 1, 1, 12, 0, tzinfo=timezone.utc)
india = timezone(timedelta(hours=5, minutes=30))
assert utc.astimezone(india).isoformat() == "2024-01-01T17:30:00+05:30"
```

The `.seconds` attribute is the remaining seconds after whole days, not the duration's total length. Use `.total_seconds()` for that. `2025-02-29` is invalid because 2025 is not a leap year. `timedelta(days=30)` means thirty days, not a universally defined calendar month.

## An instant versus a wall-clock value

A naive datetime lacks usable timezone information; an aware datetime includes it. Ordering a naive datetime against an aware one raises `TypeError`. `.astimezone()` converts an instant to another zone. Merely replacing `tzinfo` attaches an interpretation and is not the same conversion.

For regional daylight-saving rules use `zoneinfo.ZoneInfo`, with IANA timezone data installed or available from the system. The repo uses a fixed Indian offset to keep the example independent of timezone-data setup. A recurring local appointment needs a regional zone and a policy for ambiguous or nonexistent wall times, not just a stored UTC offset.

Measure elapsed performance with a monotonic performance clock such as `time.perf_counter()`, rather than subtracting wall-clock readings that may be adjusted. Inject a clock into time-sensitive code to make boundary tests deterministic.

Run: `python learn.py dates`. References: [R20: datetime](https://docs.python.org/3.14/library/datetime.html), [R21: zoneinfo](https://docs.python.org/3.14/library/zoneinfo.html).

---

<a id="page-51"></a>

# JSON and data-boundary validation
Section: Standard-library toolbox

JSON is a data interchange format, not a snapshot of arbitrary Python objects. `dumps` encodes to text and `loads` decodes text. `dump` and `load` work with file-like objects. JSON booleans are `true` and `false`; the decoded Python values are `True` and `False`.

```python
import json

encoded = json.dumps({"name": "Ayush", "active": True}, sort_keys=True)
assert encoded == '{"active": true, "name": "Ayush"}'
assert json.loads(encoded)["active"] is True
assert json.loads(json.dumps((1, 2))) == [1, 2]
assert json.loads(json.dumps({1: "value"})) == {"1": "value"}
```

Tuples become arrays and decode as lists. Object keys become strings. Sets and ordinary custom instances are unsupported by the default encoder. `ensure_ascii=False` keeps non-ASCII text readable; it does not replace the file's encoding choice. A stable exchange schema needs more than successful encoding.

## Parsing is the first gate

Valid JSON can still have the wrong top-level type, missing fields, duplicate domain IDs or values such as `"false"` where a boolean is expected. The tracker validates all of these before constructing domain objects. It checks exact key sets because an unexpected field may signal a misspelling or incompatible schema.

The default JSON decoder can accept nonstandard floating values such as NaN, and duplicate object keys generally keep the last value. Strict interoperability may require explicit options or hooks. Set size limits before parsing untrusted large documents; data formats can still cause resource exhaustion without executing code.

## Choose persistence by the required guarantees

JSON is readable and convenient for this small single-process project. It provides neither transactions nor access control by itself. Never replace JSON with `eval()` for convenience. `pickle` can reconstruct arbitrary Python objects, but unpickling untrusted data can execute code and is inappropriate at that boundary.

Run: `python learn.py utilities`. References: [R18: JSON encoding and decoding](https://docs.python.org/3.14/library/json.html), [R44: pickle security warning](https://docs.python.org/3.14/library/pickle.html).

---

<a id="page-52"></a>

# Regular expressions and precise text rules
Section: Standard-library toolbox

A regular expression describes a text pattern. Use a plain string operation when it states the requirement more directly. `.startswith()`, `.split()` and membership often express a simple rule more clearly than a pattern. Use regex when the shape is genuinely variable.

```python
import re

assert re.findall(r"\d+", "lesson 12, page 34") == ["12", "34"]
assert re.fullmatch(r"[A-Za-z]+", "Python") is not None
assert re.fullmatch(r"[A-Za-z]+", "Python3") is None
assert re.search(r"\d+", "page 34").group() == "34"
assert re.fullmatch(r"[0-9]+", "123") is not None
```

`search()` finds a match anywhere; `match()` starts at the beginning; `fullmatch()` requires the whole string. `findall()` collects matches, though capturing groups can change its return shape. `finditer()` yields match objects lazily. Check for `None` before accessing a match's groups.

## Two interpreters see the pattern

A normal Python string processes escapes, then the regex engine interprets the resulting pattern. Raw strings such as `r"\d+"` usually reduce backslash confusion. The regex language still treats the backslash specially; raw notation does not make a pattern literal. Use `re.escape(text)` when literal user text becomes part of a pattern.

`\d` matches Unicode decimal digits by default, which is broader than ASCII `[0-9]`. Similarly, case-insensitive and word-character rules can be broader than a simplistic English-only assumption. Choose the intended alphabet explicitly when validating a machine identifier.

## Keep validation bounded

Some ambiguous patterns with nested repetition can take excessive time on crafted input. Bound input sizes, prefer simple patterns and avoid granting users arbitrary regex execution unless that is an explicit feature with suitable controls. Regex is also a poor substitute for a parser when nested structured syntax is required.

Checkpoint: why does `re.search(r"[A-Za-z]+", "Python3")` succeed while the full match fails? Search only needs a matching region; full match must account for the final digit too.

References: [R22: Regular expressions](https://docs.python.org/3.14/library/re.html).

---

<a id="page-53"></a>

# Randomness, paths and small useful tools
Section: Standard-library toolbox

`random` is for simulation and ordinary randomized choices. A local `Random(seed)` object avoids changing global random state. `secrets` is the appropriate standard-library choice for unpredictable tokens and other security-sensitive random values.

```python
import random
from pathlib import Path

generator = random.Random(7)
cards = [1, 2, 3, 4]
assert generator.shuffle(cards) is None
assert sorted(cards) == [1, 2, 3, 4]
assert generator.choice(cards) in cards
path = Path("notes") / "chapter.txt"
assert path.name == "chapter.txt"
assert path.suffix == ".txt"
```

`shuffle()` mutates its list and returns `None`, like `list.sort()`. A seed helps reproduce an experiment, but do not assume every higher-level random operation has identical output across all interpreter releases. Tests should normally assert the actual required property, such as a permutation, rather than one unnecessary shuffle order.

## The repo's filesystem tour

`paths_os.py` creates a temporary source file, makes a destination directory, copies metadata where supported, moves the copy and deletes only the temporary results. It sorts discovered names before printing them so demonstration output is stable. Path discovery and path mutation are separate operations; a path object alone does nothing to the filesystem.

`math.isclose()` addresses approximate numeric comparison; `itertools.chain()` joins iterables without first building a combined list; `islice()` consumes a selected range. Prefer established standard-library behavior when it precisely matches the problem, then explain its important edge cases.

## A selection habit

Ask “does a standard tool already express this operation?” before writing a utility framework. Count with `Counter`, queue with `deque`, parse arguments with `argparse`, create isolated files with `tempfile` and test with `unittest`. Use a dependency when it provides needed capability, but keep its installation and version policy explicit.

Run: `python learn.py paths` and `python learn.py utilities`. References: [R17: pathlib](https://docs.python.org/3.14/library/pathlib.html), [R23: random](https://docs.python.org/3.14/library/random.html), [R24: secrets](https://docs.python.org/3.14/library/secrets.html).

---

<a id="page-54"></a>

# Tests that distinguish correct behavior
Section: Testing and debugging

A useful test can fail for a plausible wrong implementation. A single lowercase word does not distinguish `.capitalize()` from `.title()`; a multiword input does. The repo's text function explicitly rejects non-text input and follows `str.capitalize()`, which capitalizes the first character and lowercases the rest.

Repository excerpt: `lessons/testing/text_tools.py:4`.

```python
def capitalize_text(text):
    """Capitalize the first character and lowercase the remaining characters.

    This is str.capitalize(), not title case. Reject non-text input explicitly.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return text.capitalize()
```

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

result = unittest.TextTestRunner().run(
    unittest.defaultTestLoader.loadTestsFromTestCase(CapitalizeContractTests)
)
assert result.wasSuccessful()
```

Each test documents a different part of the contract. The first catches a tempting substitution, the second checks a boundary and the third checks rejected input. Exact error-message matching is useful when wording is part of a public interface; otherwise it can couple tests to harmless editorial changes.

## Assertions and validation

Plain `assert` is useful for internal invariants and teaching checks, but can be removed by `python -O`. Never rely on it to reject external input. Use explicit exceptions for that. `unittest` assertion methods remain active under optimization.

Run: `python -m unittest tests.test_text_tools -v`. Reference: [R25: unittest](https://docs.python.org/3.14/library/unittest.html).

---

<a id="page-55"></a>

# Isolation, failure injection and integration
Section: Testing and debugging

Tests should be repeatable and independent of personal files, current dates and previous test order. The tracker tests use `TemporaryDirectory` and cleanup registration. CLI tests capture standard output and standard error, pass arguments directly and assert return codes.

```python
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch
from projects.task_tracker.model import Task
from projects.task_tracker.storage import load_tasks, save_tasks

with TemporaryDirectory() as directory:
    path = Path(directory) / "tasks.json"
    save_tasks(path, [Task(1, "Original")])
    with patch.object(Path, "replace", side_effect=OSError("replace failed")):
        try:
            save_tasks(path, [Task(2, "New")])
        except OSError:
            pass
        else:
            raise AssertionError("Replacement should fail")
    assert load_tasks(path) == [Task(1, "Original")]
    assert not path.with_suffix(".json.tmp").exists()
```

This failure injection tests a meaningful guarantee: an unsuccessful replacement preserves old data and cleans up staging. It does not merely assert which helper was called. A real temporary filesystem is more useful than mocking every operation when the requirement is a storage round-trip.

## Patch where a dependency is used

If code imports a function into its own module namespace, patch that module's binding. Patching the original provider may leave the copied binding unchanged. Mock external services or hard-to-trigger failures; prefer real domain objects for deterministic in-memory behavior.

Unit tests isolate a small contract. Integration tests check that layers work together. The repo also launches real module entry points in subprocesses to catch import and exit-status errors that a direct function test might miss. Use timeouts so a broken command cannot hang the suite indefinitely.

Source: `tests/test_task_tracker.py`, `tests/test_runner.py`. References: [R25: unittest](https://docs.python.org/3.14/library/unittest.html), [R26: unittest.mock: where to patch](https://docs.python.org/3.14/library/unittest.mock.html#where-to-patch).

---

<a id="page-56"></a>

# Read tracebacks and diagnose deliberately
Section: Testing and debugging

A traceback gives the exception type, message and the chain of active calls. Start with the final exception, then inspect the relevant frame in your code and the values that reached it. The place that detects an invalid value is not always the place that created it.

```text
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

This message suggests a type-boundary issue, not a need to catch every exception. Trace the input path, confirm whether text-to-number conversion belongs there and add a regression case for the intended behavior. Printing `repr(value)` can reveal hidden whitespace and escape characters; `type(value)` can confirm a mistaken assumption.

## A practical investigation sequence

- Reproduce the failure with the smallest useful input.
- State the expected behavior and identify the first violated invariant.
- Inspect values with a temporary log or `breakpoint()` near that point.
- Correct the cause, then verify the original failure and a nearby valid case.
- Remove noisy diagnostic output or replace it with intentional logging.

Avoid catching `Exception` and returning an empty result merely to make a failing test green. An empty result can be a valid business answer, so it can hide lost data. The tracker deliberately distinguishes missing storage from corrupt storage.

## What this repository verifies

The checked suite has 34 tests covering lesson behavior, quiet imports, every registered lesson, text contracts, model operations, storage validation and CLI workflows. A configured CI matrix is a plan for compatibility checks; a local run is not evidence that remote CI ran. Test counts describe the reviewed snapshot and can change later.

```console
python -m unittest discover -s tests -v
python learn.py all
python -m compileall -q learn.py lessons projects tests
```

Syntax compilation catches parse failures; it does not run functions or prove the answers are correct. Coverage measures executed code, not the quality of assertions. Prefer a missing boundary test that could detect a real bug over an extra test that only repeats the implementation.

References: [R09: Errors and exceptions tutorial](https://docs.python.org/3.14/tutorial/errors.html), [R25: unittest](https://docs.python.org/3.14/library/unittest.html), [R37: logging](https://docs.python.org/3.14/library/logging.html).

---

<a id="page-57"></a>

# Task tracker: trace a complete workflow
Section: Capstone implementation

The capstone combines the course into a persistent command-line tool. Its layers are intentionally small: the model changes tasks, storage translates JSON and the CLI parses arguments and presents results. None needs a web server or external package.

| Layer | Main responsibility | Important boundary |
| --- | --- | --- |
| `model.py` | Add, complete and summarize tasks | Expects valid domain objects |
| `storage.py` | Load, validate and save JSON | Reject corrupt external records |
| `cli.py` | Parse commands and print results | Translate expected failures to status 1 |
| `__main__.py` | Execute the package | Turn return code into process status |

```console
python -m projects.task_tracker --file .practice/book-demo.json add "Revise"
python -m projects.task_tracker --file .practice/book-demo.json list
python -m projects.task_tracker --file .practice/book-demo.json done 1
python -m projects.task_tracker --file .practice/book-demo.json summary
```

```text
Added #1: Revise
[ ] 1: Revise
Completed #1: Revise
Total: 1 | Done: 1 | Pending: 0
```

These outputs assume the chosen file is initially absent or empty. Repeating the commands adds another task, so use a fresh practice file to reproduce the initial state. Every command loads current data. Only add and done save; list and summary leave missing storage absent and existing storage unchanged.

## Follow one add command

`argparse` provides a title string and a path. Storage loads validated tasks or returns an empty list for a missing file. `add_task()` trims the title, assigns an ID and mutates the list. `save_tasks()` writes the new records. The CLI prints success only after saving succeeds.

The model does not print. That lets a future GUI, test or service reuse the same behavior with a different presentation. The separation also makes it possible to ask exactly where a failure belongs and what data should survive it.

Source: `projects/task_tracker/README.md`. References: [R29: argparse](https://docs.python.org/3.14/library/argparse.html), [R18: JSON encoding and decoding](https://docs.python.org/3.14/library/json.html).

---

<a id="page-58"></a>

# Task tracker: model operations and identity
Section: Capstone implementation

The domain model represents a task with an integer ID, title and completion flag. A task's ID is distinct from its position in a list. Removing or reordering tasks should not redefine the identities of the remaining tasks.

Repository excerpt: `projects/task_tracker/model.py:13`.

```python
def add_task(tasks, title):
    """Add a task in place, assigning an ID above every existing ID."""
    title = title.strip()
    if not title:
        raise ValueError("Task title cannot be empty")
    next_id = max((task.id for task in tasks), default=0) + 1
    task = Task(next_id, title)
    tasks.append(task)
    return task
```

Repository excerpt: `projects/task_tracker/model.py:24`.

```python
def complete_task(tasks, task_id):
    """Complete the matching task; repeating this operation is harmless."""
    for task in tasks:
        if task.id == task_id:
            task.done = True
            return task
    raise ValueError(f"No task with ID {task_id}")
```

```python
from projects.task_tracker.model import Task, add_task, complete_task, summarize

tasks = [Task(2, "Read"), Task(9, "Practice")]
new = add_task(tasks, "  Revise  ")
assert (new.id, new.title) == (10, "Revise")
assert complete_task(tasks, 2).done is True
assert complete_task(tasks, 2).done is True
assert summarize(tasks) == {"total": 3, "done": 1, "pending": 2}
```

`max(..., default=0)` handles an empty collection. `len(tasks) + 1` would be wrong for sparse IDs. This strategy is unique relative to currently stored IDs; it is not a durable global sequence after every possible deletion or concurrent update.

Completion is idempotent in this model: completing an already completed task leaves the same final state. Adding is not idempotent; repeating it creates another task. This distinction becomes important when a command may be retried after an uncertain result.

The model deliberately mutates the supplied list and task objects. Its callers must understand that ownership contract. `summarize()` reads without mutation and assumes actual booleans, so `sum(task.done ...)` counts completed values. External validation establishes that assumption.

Reference: [R14: dataclasses](https://docs.python.org/3.14/library/dataclasses.html).

---

<a id="page-59"></a>

# Task tracker: validate before constructing
Section: Capstone implementation

Storage is the boundary between untrusted serialized data and trusted domain operations. `load_tasks()` first reads UTF-8 text, then parses JSON, then validates shape and field rules, then constructs `Task` objects. A successful earlier stage does not remove the need for later checks.

```json
[
  {"id": 1, "title": "Revise dictionaries", "done": true},
  {"id": 2, "title": "Practice generators", "done": false}
]
```

## The actual validation policy

- The top-level value must be a list; every member must be a dictionary.
- Each record must have exactly `id`, `title` and `done` keys.
- IDs must be positive values whose exact type is `int`, and must be unique.
- Titles must be strings with at least one non-whitespace character.
- Completion values must have exact type `bool`.

`True` is an integer instance, so `isinstance(True, int)` is insufficient for IDs. The explicit type check rejects it. A `seen_ids` set catches duplicates as the loader traverses records. Only after all checks for a record does `Task(**record)` bind its fields.

```python
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from projects.task_tracker.storage import load_tasks

with TemporaryDirectory() as directory:
    path = Path(directory) / "tasks.json"
    assert load_tasks(path) == []
    assert not path.exists()
    path.write_text(json.dumps([
        {"id": True, "title": "Read", "done": False}
    ]), encoding="utf-8")
    try:
        load_tasks(path)
    except ValueError:
        pass
    else:
        raise AssertionError("Boolean IDs must be rejected")
```

A missing file means a new workspace. Invalid JSON means existing storage cannot safely be interpreted. Treating both as empty would let the next save erase evidence of corruption. The CLI reports the error and preserves the original file instead.

Source: `projects/task_tracker/storage.py:load_tasks`. Reference: [R18: JSON encoding and decoding](https://docs.python.org/3.14/library/json.html).

---

<a id="page-60"></a>

# Task tracker: replacement and its limits
Section: Capstone implementation

Saving directly into the destination can leave a truncated document if writing fails midway. The tracker prepares JSON, writes a neighboring staging file and replaces the destination after the write finishes. Cleanup removes leftover staging on ordinary exit paths.

Repository excerpt: `projects/task_tracker/storage.py:43`.

```python
def save_tasks(path, tasks):
    """Write beside the destination, then replace it to avoid partial JSON files.

    This simple learning project supports one process at a time. A fixed staging
    path and a read/modify/write flow do not provide concurrent-update safety.
    """
    path = Path(path)
    content = json.dumps([asdict(task) for task in tasks], indent=2, ensure_ascii=False)
    path.parent.mkdir(parents=True, exist_ok=True)
    staging = path.with_name(path.name + ".tmp")
    try:
        staging.write_text(content + "\n", encoding="utf-8")
        staging.replace(path)
    finally:
        staging.unlink(missing_ok=True)
```

## What this design provides

The old destination is not intentionally truncated during staging. If replacement raises in the tested case, the previous data remains and staging is cleaned. Keeping staging beside the destination avoids the usual cross-filesystem rename problem. Encoding is explicit, and non-ASCII titles remain readable in JSON.

## What requires a stronger design

The fixed `.tmp` name lets simultaneous writers interfere. Even unique staging names would not prevent a lost update: two processes can read the same old list and each replace it with a different new list. Replacement does not make the entire read/modify/write sequence transactional.

Atomic visibility also differs from crash durability. Strong power-loss guarantees can require flushing data and directory metadata with platform-specific care. Cleanup itself can fail and potentially mask an earlier error. For this learning application, the documented scope is one process at a time; concurrent use calls for a deliberate transaction or locking design.

Source: `tests/test_task_tracker.py` verifies failed replacement and round-trip behavior. References: [R17: pathlib](https://docs.python.org/3.14/library/pathlib.html), [R33: sqlite3 and transaction control](https://docs.python.org/3.14/library/sqlite3.html).

---

<a id="page-61"></a>

# Task tracker: rebuild, test and extend
Section: Capstone implementation

Rebuild the application in a scratch package in this order: model, in-memory tests, storage, temporary-file tests, CLI and subprocess workflow. The completed code is a reference; the tests describe observable behavior. Keep the original package available for comparison.

## A complete extension exercise

Add `rename <id> <title>`. Decide that titles are trimmed and blank titles fail. Add a model operation that raises on an unknown ID and changes only the matching task. Expose the command through `argparse`, save only after a successful change and print a clear result.

Test a valid rename, trimming, a blank title, an unknown ID, Unicode and a corrupt storage file. For rejected commands, compare the file's bytes before and after. Check the process status and standard error as well as the in-memory value. Update help and documentation so the behavior can be discovered without reading the code.

## Preserve boundaries as scope grows

For `list --pending`, filtering belongs in an explicit query or presentation path; it must not delete completed records. For due dates, define whether a missing date is permitted, how dates are serialized and how old files migrate. The loader's exact-key policy means adding a field requires a format decision, not just a dataclass edit.

For several simultaneous users, a JSON replacement helper is no longer the central problem. You need transactions, identity policy, authorization if exposed over a network and a way to resolve conflicting updates. Architect questions at the end explore those changes without pretending they already exist here.

## Explain the project in an interview

Describe one concrete workflow, then one failure path. A strong example is “invalid JSON is reported without overwriting the file,” supported by a test. Another is “list does not create storage.” Use measured or tested claims; do not invent adoption, production use or performance gains.

```console
python -m unittest tests.test_task_tracker -v
python -m projects.task_tracker --help
```

References: [R25: unittest](https://docs.python.org/3.14/library/unittest.html), [R29: argparse](https://docs.python.org/3.14/library/argparse.html), [R33: sqlite3 and transaction control](https://docs.python.org/3.14/library/sqlite3.html).

---

<a id="page-62"></a>

# CPython memory, references and measurement
Section: Deeper Python extensions

Extension beyond the repo: CPython commonly uses reference counting together with cyclic garbage collection. Losing a binding through `del name` removes that reference; it does not command every Python implementation to destroy the object at that instant. Other references or cycles may keep objects alive.

An unreachable cycle can need the cyclic collector even after external references disappear. A weak reference can observe an object without owning its lifetime, but only supported objects allow weak references. Resource release should still use a context manager rather than relying on collection timing.

## Memory size is a graph question

`sys.getsizeof(container)` normally reports the container's own allocation, not the total recursively retained graph. Shared subobjects make naive summing inaccurate: you can count the same object twice. Generator frames and closures can retain references long after the creating function returns.

```python
import gc
import tracemalloc

tracemalloc.start()
before = tracemalloc.take_snapshot()
values = [str(number) for number in range(1000)]
after = tracemalloc.take_snapshot()
differences = after.compare_to(before, "lineno")
assert values[0] == "0"
assert differences
tracemalloc.stop()
del values
gc.collect()
```

This shows a measurement workflow, not a portable byte-count benchmark. `tracemalloc` observes traced Python allocations; native libraries can allocate memory outside that view. Resident process memory, reachable Python allocations and allocator-reserved memory answer different questions.

## Avoid implementation folklore

Object IDs may be reused after an object dies. Integer and string reuse is not an equality contract. Reference counts observed through diagnostic functions include temporary references. Do not build application behavior around these incidental observations.

Practice: retain a large object in a closure, remove the original name and explain why memory can remain reachable. Then release the closure and measure again with an appropriate tool.

References: [R06: Python data model](https://docs.python.org/3.14/reference/datamodel.html), [R36: tracemalloc](https://docs.python.org/3.14/library/tracemalloc.html).

---

<a id="page-63"></a>

# Concurrency, parallelism and the GIL
Section: Deeper Python extensions

Concurrency means work can make progress over overlapping periods. Parallelism means work executes simultaneously. Choose a mechanism from the workload and shared-state requirements, not from a blanket claim that one model is always fastest.

| Mechanism | Useful starting case | Main cost or concern |
| --- | --- | --- |
| Threads | Blocking I/O with shared process state | Synchronization and bounded workers |
| Processes | CPU-heavy Python work | Startup, serialization and separate memory |
| Async I/O | Many cooperative I/O operations | Blocking the event loop; cancellation |

In a conventional GIL-enabled CPython build, one thread executes Python bytecode at a time. I/O and some native operations can release the GIL. That does not make a multi-step business operation atomic: “check, then update” can still race. Protect the invariant with a lock or a transactional storage mechanism.

## Version-specific detail

Free-threaded CPython builds introduced in 3.13 can run Python threads in parallel. Python 3.14 gives free threading supported status under PEP 779; it remains a distinct configuration rather than a promise that every installation has the GIL disabled. Extensions can affect whether the GIL is enabled. Verify the deployed build and dependency compatibility rather than repeating an unconditional GIL slogan.

## Async is cooperative

An `async def` call returns a coroutine object. It progresses when awaited or scheduled. Awaiting an operation that suspends lets the loop run other tasks; `await` does not automatically move CPU work to another core. A blocking file, network or CPU call can still stall the event loop.

Bound task counts and queues. Define timeouts, cancellation cleanup and error propagation. A pool with unlimited submissions can exhaust memory even if each task is small. For processes, use importable worker functions and guard program startup with `if __name__ == "__main__":`, especially under spawn-based execution.

The tracker is synchronous and assumes one writer. Adding threads around it does not create a concurrent storage contract.

References: [R30: CPython free-threading guide](https://docs.python.org/3.14/howto/free-threading-python.html), [R31: concurrent.futures](https://docs.python.org/3.14/library/concurrent.futures.html), [R32: asyncio overview](https://docs.python.org/3.14/library/asyncio.html), [R39: PEP 779: supported free-threaded Python](https://peps.python.org/pep-0779/), [R43: Thread synchronization and locks](https://docs.python.org/3.14/library/threading.html).

---

<a id="page-64"></a>

# Performance, observability and robustness
Section: Deeper Python extensions

Extension beyond the repo: optimize a measured bottleneck under a representative workload. A profiler identifies where execution time accumulates; a microbenchmark compares a narrow operation; allocation tracing investigates retained memory. Each tool answers a different question.

```console
python -m cProfile -s cumulative learn.py all
python -m timeit "sum(range(1000))"
```

The first command is a demonstration of profiling mechanics; the small course runner is not a production workload. For meaningful results, include realistic data size, repeated measurements, interpreter version, warmup assumptions and external I/O behavior. A faster isolated expression can make no visible difference to the whole application.

## Improve the algorithm before tiny expressions

Avoid nested linear membership scans when a set is valid. Avoid repeatedly parsing unchanged data. Stream large bounded transformations where output does not need to be materialized. Choose caching only when keys, invalidation and memory are understood. Preserve error behavior and verify the same contract after an optimization.

## Make failures explainable

Use module loggers with useful event context rather than printing every internal value. Configure logging at an application boundary. Include identifiers that help correlate work; avoid secrets and unnecessary personal data. Record success only after the persistence step succeeds.

For a service, latency percentiles, error categories, queue depth and resource use may expose problems an average hides. A retry policy needs a deadline, retryable error classes and idempotency rules. Retrying invalid input does not help; retrying a successful-but-unacknowledged add can duplicate it.

## Separate kinds of guarantees

Input validation, thread safety, transaction isolation, crash durability and authorization are distinct. A passing unit test for one does not establish the others. State what the application promises, test that boundary and strengthen the design when the requirements change.

Checkpoint: propose one realistic tracker optimization only after naming a measured bottleneck and a dataset large enough to reveal it. Otherwise, prioritize clarity and correctness.

References: [R34: Profiling Python programs](https://docs.python.org/3.14/library/profile.html), [R35: timeit](https://docs.python.org/3.14/library/timeit.html), [R36: tracemalloc](https://docs.python.org/3.14/library/tracemalloc.html), [R37: logging](https://docs.python.org/3.14/library/logging.html).

---

<a id="page-65"></a>

# Practice workbook · values and functions
Section: Practice workbook

Attempt these exercises without the solution pages. Write down the input contract first, then implementation and checks. The tasks come from `docs/exercises.md`; examples below preserve the repository's intended behavior. Aim to explain the result, not just produce matching text.

## Exercise 1 · Alternating text

Implement `alternating_case(text)` so characters at even original indices are lowercase and those at odd indices are uppercase. Spaces count as positions. Expected: `"ayush"` becomes `"aYuSh"`, `"PYTHON"` becomes `"pYtHoN"`, `"a bc"` becomes `"a bC"` and `""` stays empty. Use `enumerate()` and a final join. Explain why Unicode casing can change output length.

## Exercise 2 · Unique values in order

Implement `unique_in_order(values)` for hashable values. Preserve each value's first appearance without changing the input. `[3, 1, 3, 2, 1]` becomes `[3, 1, 2]`; an empty input returns `[]`. Explain why `list(set(values))` cannot satisfy the ordering contract. Decide what happens to `[1, True, 1.0]` and to nested lists.

## Exercise 3 · Even squares

Return squares of even integers, preserving order and duplicates. `[3, -2, 0, 4, 4]` becomes `[4, 0, 16, 16]`; `[1, 3]` becomes `[]`. Transform only after testing the original value. Show both a loop and a comprehension, and verify neither mutates the input.

## Exercise 4 · Independent counters

Implement `make_counter(start=0)`, returning a function that increments and returns its own count. With start 10, the first two results are 11 and 12. A new default counter begins with 1, independent of the first. Explain why `nonlocal` is needed for rebinding but would not be needed merely to append to an enclosing list.

## A useful submission format

For each exercise, provide the function, three ordinary or boundary checks and a short explanation of its time and space behavior. A test should capture a requirement rather than every intermediate implementation choice. Save your practice separately so the maintained examples remain a reliable reference.

Source: `docs/exercises.md:1–4`. References: [R02: Built-in types and operations](https://docs.python.org/3.14/library/stdtypes.html), [R04: Data structures tutorial](https://docs.python.org/3.14/tutorial/datastructures.html), [R08: Execution model and name binding](https://docs.python.org/3.14/reference/executionmodel.html).

---

<a id="page-66"></a>

# Practice workbook · resources and objects
Section: Practice workbook

These tasks combine a useful contract with failure behavior. Name the exception type deliberately. Use a temporary directory for files and test rejected values as carefully as accepted ones.

## Exercise 5 · Load nonempty lines

Implement `load_nonempty_lines(path)`: read UTF-8 text, strip leading and trailing whitespace from each line and retain only nonempty results. `"  Python  \n\n Practice\n"` must produce `["Python", "Practice"]`. An empty file returns `[]`; a missing file raises `FileNotFoundError`. Do not silently invent empty content when a read fails.

Test a normal file, an empty file and a missing file. Explain whether the input is streamed and whether the returned output is fully materialized. Show why the stream is closed even if processing raises.

## Exercise 6 · A Book class

Create `Book(title, pages)`. For `Book("Python Notes", 120)`, `str(book)` must be `"Python Notes (120 pages)"` and `len(book)` must be 120. Pages must have exact type `int` and be nonnegative. Reject negative values with `ValueError`; reject non-integers and booleans with `TypeError`.

Zero pages is valid. Predict `bool(Book("Empty", 0))` and justify it through the protocol lookup. Explain whether validating initialization also prevents later `book.pages = -1`, and propose a property if continuous enforcement is required.

## Exercise 7 · A repeatable decorator

Implement `repeat(times)` so `@repeat(3)` invokes a function three times, forwards arguments and returns a list of results. A decorated doubling function called with 4 returns `[8, 8, 8]`. Preserve name and docstring. Reject a negative integer with `ValueError` and a boolean or non-integer count with `TypeError`.

Zero repetitions returns `[]` without calling the original. If an invocation raises, let the failure propagate and stop later repetitions. Test a keyword-only parameter, zero calls and one failing call. Explain when configuration validation runs and why repeated side effects make this decorator unsuitable for some operations.

Source: `docs/exercises.md:5–7`. References: [R13: contextlib and resource management](https://docs.python.org/3.14/library/contextlib.html), [R06: Python data model](https://docs.python.org/3.14/reference/datamodel.html), [R11: functools: wraps, caching and partial](https://docs.python.org/3.14/library/functools.html).

---

<a id="page-67"></a>

# Practice workbook · iteration and testing
Section: Practice workbook

These tasks check whether you understand consumption, data contracts and tests that can detect a plausible mistake. Avoid reading the answer until you have a concrete implementation and at least one edge-case check.

## Exercise 8 · Lazy running totals

Implement `running_totals(values)`, yielding each cumulative sum. `[2, -1, 3]` must yield 2, 1, 4. Empty input yields nothing. Accept an iterator as well as a list, and do not convert the input into a list first.

Use an input generator that records when it is advanced. Verify constructing `running_totals(source)` does not consume the body of that generator, and requesting one result consumes only one input. Compare the behavior with `itertools.accumulate()`.

## Exercise 9 · Word counts

Implement `word_counts(text)` with `Counter`. Tokens are separated by whitespace and compared without case. `"Python python code"` gives counts `python: 2` and `code: 1`. An empty input gives an empty counter. `"code code!"` has two keys: punctuation remains part of each token.

Explain the difference between changing the algorithm and changing the tokenizer's specification. Describe why `.casefold()` is useful for case-insensitive matching and why it is not a complete policy for every language or normalization need.

## Exercise 10 · Test the capitalization contract

Write `unittest` cases for `capitalize_text()` that fail if it is replaced with `.title()`. Include empty input and rejected non-string input. A single lowercase word is insufficient because both implementations can pass that case.

Save a test module beginning with `test_` in your scratch test directory and run discovery. Read one deliberately caused failure, including the actual and expected values, then restore the correct implementation.

## Final independent challenge

Add one tracker feature completely: pending-only listing, rename or due dates. Describe the command syntax, model behavior, storage implications, failures and checks before coding. Reuse the capstone extension page's boundary checklist. A partial happy-path function is not a finished feature.

Source: `docs/exercises.md:8–10`. References: [R12: itertools: iterator building blocks](https://docs.python.org/3.14/library/itertools.html), [R19: collections](https://docs.python.org/3.14/library/collections.html), [R25: unittest](https://docs.python.org/3.14/library/unittest.html).

---

<a id="page-68"></a>

# Workbook answers · exercises 1–4
Section: Practice workbook

Compare the ownership and ordering rules, not just the visual similarity of your implementation. These are complete definitions adapted from `docs/solutions.md`.

```python
def alternating_case(text):
    return "".join(
        character.lower() if index % 2 == 0 else character.upper()
        for index, character in enumerate(text)
    )

def unique_in_order(values):
    return list(dict.fromkeys(values))

def even_squares(values):
    return [number**2 for number in values if number % 2 == 0]

def make_counter(start=0):
    count = start
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

assert alternating_case("a bc") == "a bC"
assert alternating_case("") == ""
assert unique_in_order([3, 1, 3, 2, 1]) == [3, 1, 2]
assert unique_in_order([1, True, 1.0]) == [1]
assert even_squares([3, -2, 0, 4, 4]) == [4, 0, 16, 16]
first, second = make_counter(10), make_counter()
assert (first(), first(), second()) == (11, 12, 1)
```

## Reasoning and complexity

Alternating case visits each input position and joins fragments; space scales with the produced text. Dictionary keys retain first-insertion order, but require hashable values and merge values that compare equal with matching hashes. Expected deduplication time is O(n) with ordinary hashing; worst-case collision behavior can be worse.

The even-squares filter tests the original integer. Zero and negative even values follow the same rule. The returned list is new and the original order and duplicates survive. The closure stores a separate binding per factory call and each increment is constant-time under ordinary bounded-value reasoning; arbitrary-size integer arithmetic can grow with the count's size.

For nested unhashable values, the short deduplication function raises `TypeError`. Supporting them requires a new equality/key policy or a potentially slower scan, not a silent conversion that changes meaning.

References: [R04: Data structures tutorial](https://docs.python.org/3.14/tutorial/datastructures.html), [R08: Execution model and name binding](https://docs.python.org/3.14/reference/executionmodel.html).

---

<a id="page-69"></a>

# Workbook answers · exercises 5–7
Section: Practice workbook

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

class Book:
    def __init__(self, title, pages):
        if type(pages) is not int:
            raise TypeError("pages must be an integer")
        if pages < 0:
            raise ValueError("pages must be non-negative")
        self.title, self.pages = title, pages

    def __str__(self):
        return f"{self.title} ({self.pages} pages)"

    def __len__(self):
        return self.pages

assert str(Book("Python Notes", 120)) == "Python Notes (120 pages)"
assert len(Book("Empty", 0)) == 0
assert not Book("Empty", 0)
```

The loader returns a materialized result but does not read the entire input text in one call. Missing-file failures propagate. The `with` closes the stream before a return completes. The Book check deliberately rejects booleans; it enforces initial values only. Use the earlier PageCount property pattern to enforce later ordinary assignments too.

## Repeat decorator solution

The complete implementation is on “Configurable decorators, caching and effects.” Its three nested functions are `repeat(times)`, `decorate(function)` and `wrapper(*args, **kwargs)`. Validate `times` in the outer layer, apply `@wraps(function)` to the wrapper and return a list comprehension over `range(times)`.

That comprehension executes no calls when times is zero. If a call raises, Python abandons the comprehension and propagates the exception. A partially constructed list is not returned. Tests should confirm metadata, keyword argument forwarding and that later calls do not occur after failure. The repo's `docs/solutions.md` also contains the full definition.

References: [R11: functools: wraps, caching and partial](https://docs.python.org/3.14/library/functools.html), [R13: contextlib and resource management](https://docs.python.org/3.14/library/contextlib.html), [R06: Python data model](https://docs.python.org/3.14/reference/datamodel.html).

---

<a id="page-70"></a>

# Workbook answers · exercises 8–10
Section: Practice workbook

```python
from collections import Counter

def running_totals(values):
    total = 0
    for value in values:
        total += value
        yield total

def word_counts(text):
    return Counter(text.casefold().split())

assert list(running_totals(iter([2, -1, 3]))) == [2, 1, 4]
assert list(running_totals([])) == []
assert word_counts("Python python code") == {"python": 2, "code": 1}
assert word_counts("code code!") == {"code": 1, "code!": 1}
assert not word_counts("")
```

Running totals consumes one item per requested output and keeps one accumulator. Empty input never reaches a yield. `itertools.accumulate()` is the standard-library equivalent for ordinary addition. Counting retains O(k) distinct keys; the simple `.split()` implementation also materializes all tokens, so its peak memory is not limited to the counter alone.

## Capitalization tests

The complete runnable `unittest` example appears on “Tests that distinguish correct behavior.” The three essential checks are:

```python
from lessons.testing.text_tools import capitalize_text

assert capitalize_text("HELLO WORLD") == "Hello world"
assert capitalize_text("") == ""
try:
    capitalize_text(123)
except TypeError:
    pass
else:
    raise AssertionError("Non-text input must fail")
```

Use `self.assertEqual()` and `self.assertRaises()` in the actual test module so failures report useful context. The multiword expected value rejects a `.title()` implementation; the empty and type checks document separate boundaries. `" hello"` is another useful case: `.capitalize()` acts on the first character, so leading whitespace does not trigger capitalization of the next word.

## Reflect before moving on

For each exercise, write one sentence naming the assumption most likely to be forgotten: hashability, original positions, exact integer type, one-shot consumption or punctuation policy. Rebuild one solution from memory a day later. If you cannot explain the edge case, rerun a smaller example and trace it.

References: [R12: itertools: iterator building blocks](https://docs.python.org/3.14/library/itertools.html), [R19: collections](https://docs.python.org/3.14/library/collections.html), [R25: unittest](https://docs.python.org/3.14/library/unittest.html).

---

<a id="page-71"></a>

# Revision map and a practical study plan
Section: Revision desk

Use ten sessions plus a capstone, following `docs/study_plan.md`. A session can take 30–60 minutes, but understanding is the checkpoint. If a topic is unfamiliar, split it into several shorter sessions. Revision means predicting and explaining code, not reading faster.

| Session | Main focus | Explain without the book |
| --- | --- | --- |
| 1 | Values and text | Floor division, slicing, truthiness |
| 2 | Containers | Aliasing versus shallow/deep copies |
| 3 | Control flow | Loop else and comprehension ordering |
| 4 | Functions | Parameter kinds, defaults and closure state |
| 5 | Files and errors | Encoding, cleanup and specific handlers |
| 6 | Objects | Instance state, class lookup and protocols |
| 7 | Lazy code | Generator timing and decorator replacement |
| 8 | Modules | Import execution, main guard and module runs |
| 9 | Standard library | Select tools for counts, dates and JSON |
| 10 | Testing | A discriminating edge case and failure path |
| 11–12 | Tracker | Trace add, corrupt data and failed save |

## Choose a revision route

**One hour:** names and references; safe defaults; generator exhaustion; file modes; the tracker workflow; then two questions from your interview level. Predict an output before checking each page.

**One day:** run all 21 lessons, complete one exercise from each major area and explain one storage failure. Review questions that exposed a missing concept rather than rereading every page equally.

**One week:** alternate new learning with retrieval. Rebuild a helper on day one, explain it without notes on day two, vary its inputs on day four and use it in a small feature on day seven. Keep a short list of mistaken assumptions.

## Readiness check

Can you modify a contract and update the implementation, tests and explanation together? Can you distinguish a language guarantee from a CPython detail? Can you state which requirements the tracker does not yet meet? Those abilities transfer better than memorized trick answers.

Source: `docs/study_plan.md`, `docs/quick_reference.md`.

---

<a id="page-72"></a>

# The pitfalls checklist
Section: Revision desk

| Surprise | Correct explanation or response |
| --- | --- |
| `bool("False")` is true | Nonempty text is truthy; parse a boolean policy explicitly |
| `-7 // 2` is -4 | Floor is toward negative infinity; int truncates toward zero |
| `0.1 + 0.2 != 0.3` | Binary approximation; choose a meaningful tolerance |
| `a = b` shares changes | Assignment binds a reference; it does not copy |
| `.copy()` shares nested lists | Only the outer container is new |
| `[[0]] * 3` shares rows | Repetition repeats references; build rows independently |
| `items = items.sort()` loses list | In-place sorting returns None |
| A tuple's inner list mutates | Fixed outer references are not deep immutability |
| `{}` is not an empty set | Use `set()` |
| Dict/set merge 1 and True | Equal keys with equal hashes share an entry |
| A default list grows between calls | Defaults are evaluated when def executes |
| Lambdas all see final index | Closures look up the binding when called |
| A second list(iterator) is empty | The same iterator is exhausted |
| Bad generator arguments fail later | Its body starts during iteration |
| The decorator loses a result | Forward arguments and return the original result |
| An after-log is missing on failure | Use finally only if it must run on every exit |
| Opening with w loses old contents | Truncation occurs on opening |
| Returning in finally hides an error | Cleanup should not replace pending control flow |
| An annotation accepts bad runtime data | Add validation at the external boundary |
| A read of defaultdict changes it | Missing bracket lookup calls and stores the factory value |
| timedelta.seconds ignores days | Use total_seconds() for a full duration |
| A main guard makes import inert | Other top-level code and decorators still execute |
| Replacing a file loses another update | Atomic replacement is not a transaction |
| The GIL proves thread safety | Protect multi-step shared invariants explicitly |

For any surprising output, ask: which object changed, which binding was looked up, when did execution occur and what did the contract promise? Those four questions explain most of the repo's deliberate traps.

References: [R02: Built-in types and operations](https://docs.python.org/3.14/library/stdtypes.html), [R05: Shallow and deep copying](https://docs.python.org/3.14/library/copy.html), [R08: Execution model and name binding](https://docs.python.org/3.14/reference/executionmodel.html), [R09: Errors and exceptions tutorial](https://docs.python.org/3.14/tutorial/errors.html), [R30: CPython free-threading guide](https://docs.python.org/3.14/howto/free-threading-python.html).

---

<a id="page-73"></a>

# Reference library · language and data
Section: Official reference library

These primary sources were checked while preparing this edition. Links are pinned to Python 3.14 to keep one documentation baseline; check version notes before using a newer API in a Python 3.10 project. The guide's explanations and examples are original teaching material built around the supplied repository; links provide deeper specifications and API details.

- [R01: Python tutorial: numbers and text](https://docs.python.org/3.14/tutorial/introduction.html) — First steps with numeric and text values.
- [R02: Built-in types and operations](https://docs.python.org/3.14/library/stdtypes.html) — Truth testing, containers, strings and standard operations.
- [R03: Control flow and function definitions](https://docs.python.org/3.14/tutorial/controlflow.html) — Branches, loops, signatures, defaults and annotations.
- [R04: Data structures tutorial](https://docs.python.org/3.14/tutorial/datastructures.html) — Lists, tuples, dictionaries and comprehensions.
- [R05: Shallow and deep copying](https://docs.python.org/3.14/library/copy.html) — Assignment, shallow copying and deep copying.
- [R06: Python data model](https://docs.python.org/3.14/reference/datamodel.html) — Identity, protocols, special methods and object behavior.
- [R07: Built-in functions](https://docs.python.org/3.14/library/functions.html) — Builtins such as iter, next, sorted, property and open.
- [R08: Execution model and name binding](https://docs.python.org/3.14/reference/executionmodel.html) — Binding, scope, free variables and name lookup.
- [R09: Errors and exceptions tutorial](https://docs.python.org/3.14/tutorial/errors.html) — Handling, raising, chaining and cleanup.
- [R10: Classes tutorial](https://docs.python.org/3.14/tutorial/classes.html) — Classes, namespaces, inheritance and iteration.
- [R11: functools: wraps, caching and partial](https://docs.python.org/3.14/library/functools.html) — Wrappers, caches, partial application and metadata.
- [R12: itertools: iterator building blocks](https://docs.python.org/3.14/library/itertools.html) — Composing and consuming iterators.
- [R13: contextlib and resource management](https://docs.python.org/3.14/library/contextlib.html) — Context-manager adapters and ExitStack.
- [R14: dataclasses](https://docs.python.org/3.14/library/dataclasses.html) — Generated record methods and field options.
- [R15: typing and structural protocols](https://docs.python.org/3.14/library/typing.html) — Hints, unions, generics and structural interfaces.
- [R16: Descriptor how-to](https://docs.python.org/3.14/howto/descriptor.html) — Properties, bound methods and attribute lookup.
- [R17: pathlib](https://docs.python.org/3.14/library/pathlib.html) — Path objects and concrete filesystem operations.
- [R18: JSON encoding and decoding](https://docs.python.org/3.14/library/json.html) — Serialization limits, hooks and decoder behavior.
- [R19: collections](https://docs.python.org/3.14/library/collections.html) — Counters, queues, defaults and named records.
- [R20: datetime](https://docs.python.org/3.14/library/datetime.html) — Calendar values, durations and aware datetimes.
- [R21: zoneinfo](https://docs.python.org/3.14/library/zoneinfo.html) — Regional IANA time-zone rules and data availability.
- [R22: Regular expressions](https://docs.python.org/3.14/library/re.html) — Pattern syntax, match objects and text-search APIs.
- [R23: random](https://docs.python.org/3.14/library/random.html) — Pseudorandom simulation tools and reproducibility.

## How to read a reference page

Start with the exact operation and its return type. Check mutability, exceptions, accepted inputs and version notes. Then build a five-line experiment. A reference is most useful when you bring a concrete question, such as whether a missing lookup inserts a value or when an iterator raises an error.

---

<a id="page-74"></a>

# Reference library · engineering and tooling
Section: Official reference library

- [R24: secrets](https://docs.python.org/3.14/library/secrets.html) — Unpredictable tokens and security-sensitive randomness.
- [R25: unittest](https://docs.python.org/3.14/library/unittest.html) — Test cases, assertions, discovery and fixtures.
- [R26: unittest.mock: where to patch](https://docs.python.org/3.14/library/unittest.mock.html#where-to-patch) — Patch a dependency in the namespace that uses it.
- [R27: Modules tutorial](https://docs.python.org/3.14/tutorial/modules.html) — Packages, imports, module search and program execution.
- [R28: Virtual environments tutorial](https://docs.python.org/3.14/tutorial/venv.html) — Isolated environments and package installation.
- [R29: argparse](https://docs.python.org/3.14/library/argparse.html) — Argument parsing, help and subcommands.
- [R30: CPython free-threading guide](https://docs.python.org/3.14/howto/free-threading-python.html) — Free-threaded builds, compatibility and shared state.
- [R31: concurrent.futures](https://docs.python.org/3.14/library/concurrent.futures.html) — Thread and process pools, futures and shutdown.
- [R32: asyncio overview](https://docs.python.org/3.14/library/asyncio.html) — Coroutines, event loops and asynchronous I/O.
- [R33: sqlite3 and transaction control](https://docs.python.org/3.14/library/sqlite3.html) — Embedded databases and explicit transaction behavior.
- [R34: Profiling Python programs](https://docs.python.org/3.14/library/profile.html) — Profilers and interpreting cumulative time.
- [R35: timeit](https://docs.python.org/3.14/library/timeit.html) — Repeated microbenchmarks and measurement caveats.
- [R36: tracemalloc](https://docs.python.org/3.14/library/tracemalloc.html) — Python allocation snapshots and comparisons.
- [R37: logging](https://docs.python.org/3.14/library/logging.html) — Loggers, handlers, configuration and severity.
- [R38: PEP 8: Python style](https://peps.python.org/pep-0008/) — Naming, layout and readable code conventions.
- [R39: PEP 779: supported free-threaded Python](https://peps.python.org/pep-0779/) — Python 3.14 supported free-threading status.
- [R40: Floating-point arithmetic tutorial](https://docs.python.org/3.14/tutorial/floatingpoint.html) — Representation error and approximate arithmetic.
- [R41: decimal arithmetic](https://docs.python.org/3.14/library/decimal.html) — Decimal contexts, arithmetic and rounding.
- [R42: tempfile](https://docs.python.org/3.14/library/tempfile.html) — Temporary files and directory lifetime.
- [R43: Thread synchronization and locks](https://docs.python.org/3.14/library/threading.html) — Threads, synchronization primitives and locks.
- [R44: pickle security warning](https://docs.python.org/3.14/library/pickle.html) — Python object serialization and untrusted-data risks.
- [R45: Packaging Python projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/) — Build metadata and distributing a Python package.
- [R46: Structural pattern matching specification](https://peps.python.org/pep-0634/) — Structural pattern matching in Python 3.10.

## Repository reading order

Start with `README.md`, use each `lessons/*/README.md` beside the runnable module, then read `docs/exercises.md` before `docs/solutions.md`. For implementation review, follow `projects/task_tracker/model.py`, `storage.py`, `cli.py` and `tests/test_task_tracker.py`. The quick reference is an index for recall, not a substitute for tracing the examples.

## Keeping the PDF current

The source chapters live in `docs/python_guide/`; the builder extracts marked functions from the maintained source files and records source hashes in a build manifest. After a contract changes, update the relevant prose and expected outputs, run repository tests and rebuild. Extracting current code prevents one kind of drift; it cannot automatically correct an explanation that describes an obsolete rule.

The final section is the mock interview workbook. Its scenarios progress from language behavior to system boundaries, with answers, follow-up prompts and evaluation cues.

---

<a id="page-75"></a>

# Mock interviews: format and scoring
Section: Mock interview · instructions

This section contains **48 answered questions**: 12 each for fresher, mid-level, senior and architect candidates. Levels describe the expected depth, not a universal number of years. The answers are a foundation for discussion rather than scripts to memorize. A strong candidate states assumptions and can adapt the answer when the interviewer changes one requirement.

## Run a realistic session

For a fresher, allow 35–45 minutes: three explanation questions, two output predictions and one small coding exercise. For mid-level, allow 45–60 minutes: two language questions, one bug diagnosis, one implementation and a test-design discussion. For senior or architect, allow 60–75 minutes: choose fewer questions and explore failure cases, requirements and tradeoffs in depth.

Have one person ask, or record your own explanation. Read only the question first and cover the answer. Use a scratch file for code. After answering, compare the reasoning, not the exact phrasing. Choose the next question from the weakness the discussion exposed.

## A simple per-question rubric

| Score | Evidence |
| --- | --- |
| 0 | Incorrect behavior or no usable model |
| 1 | Recalls a definition but cannot apply it |
| 2 | Explains the central behavior with a valid example |
| 3 | Handles edge cases and proposes a meaningful check |
| 4 | States boundaries, tradeoffs and a suitable alternative |

A fresher can do well by consistently reaching 2 and showing sound learning habits. A mid-level developer should connect behavior to implementation and tests. A senior should anticipate ownership, failure timing, concurrency and compatibility. An architect should clarify requirements, locate guarantees and design an incremental path with measurable acceptance criteria.

## Avoid trick-question theater

When predicting output, explain the rule: binding, mutation, laziness or control flow. For design questions there may be several acceptable answers. Score consistency with requirements and treatment of failure; do not reward technology names without a concrete contract. If an assumption changes, revise the design openly.

The question pages link back to official references and name relevant repository files. Revisit the implementation after a weak answer, then try again without notes.

---

<a id="page-76"></a>

# Fresher · objects, equality and arithmetic
Section: Mock interview · fresher

## F01 · What does assignment copy? How do == and is differ?

**Answer:** ordinary assignment binds a name to an object; it does not copy the object. `==` compares values through equality behavior, while `is` checks identity. Two equal lists can be distinct objects. Two names referring to one list observe the same mutation. Rebinding one name later does not redirect the other name.

```python
a = [1, 2]
b = [1, 2]
c = a
assert a == b and a is not b
assert c is a
c.append(3)
assert a == [1, 2, 3] and b == [1, 2]
c = []
assert a == [1, 2, 3]
```

Use `is None` for the singleton sentinel. Do not compare string or number values using identity: incidental object reuse can make a bad test seem correct. For a custom class, equality can be overridden, but identity still asks the same single-object question.

**Follow-up answered:** `a.copy()` creates a new outer list, so top-level appends are independent. Nested mutable elements remain shared. A strong answer distinguishes mutation from rebinding and can draw the references.

## F02 · Explain /, //, %, int() and floating-point equality.

**Answer:** `/` performs true division, so `7 / 2` is `3.5`. `//` floors: `-7 // 2` is `-4`. `int(-3.9)` truncates toward zero and gives `-3`, which is a different operation. For nonzero integer `b`, quotient and remainder satisfy `a == (a // b) * b + a % b`; `-7 % 2` is `1`.

Floats approximate many decimal values in binary, so `0.1 + 0.2 == 0.3` is false. Formatting the sum to two decimals changes its display, not its stored value. Use a domain-appropriate tolerance with `math.isclose()`, including an absolute tolerance near zero when needed. Exact decimal requirements can justify `Decimal` constructed from strings, with an explicit rounding policy.

**Follow-up answered:** `int("3.5")` raises `ValueError`; it does not parse and silently truncate decimal text. A strong answer explains the negative quotient rather than memorizing only positive examples.

Repo: `lessons/basics/numbers.py`. References: [R06: Python data model](https://docs.python.org/3.14/reference/datamodel.html), [R01: Python tutorial: numbers and text](https://docs.python.org/3.14/tutorial/introduction.html), [R40: Floating-point arithmetic tutorial](https://docs.python.org/3.14/tutorial/floatingpoint.html).

---

<a id="page-77"></a>

# Fresher · text and container choice
Section: Mock interview · fresher

## F03 · How do slicing and string methods behave?

**Answer:** strings are immutable Unicode sequences. Indexing returns one code point; a slice returns a new string and excludes its stop. With `word = "Python"`, `word[1:4]` is `'yth'`, `word[-2:]` is `'on'` and `word[::-1]` is `'nohtyP'`. `word[999]` raises `IndexError`, but `word[999:]` is empty. A step of zero raises `ValueError`.

Calling `word.upper()` returns a transformed value and leaves `word` unchanged. `strip()` cleans the ends, `split()` produces tokens and `join()` combines strings. No-separator splitting treats runs of whitespace differently from splitting on a literal comma. `repr()` is useful when newline escapes or spaces make output ambiguous.

**Follow-up answered:** `len(text)` counts Unicode code points, not universally visible characters. Some case operations expand text, so a function such as alternating case works by original input positions without promising equal input/output length. A strong answer uses a small slice trace and states immutability clearly.

## F04 · When would you choose list, tuple, dict or set?

**Answer:** choose a list for an ordered mutable sequence, a tuple for fixed references or an immutable record shape, a dictionary for key/value lookup and a set for uniqueness and membership. Lists and tuples preserve sequence order and duplicates. Dictionaries preserve insertion order with unique keys. Sets have no order guarantee.

Dictionary keys and set elements must be hashable. A tuple containing a list is not hashable, even though the tuple's slots cannot be reassigned. A tuple's inner list can still mutate. `{}` creates a dictionary; `set()` creates an empty set. `(10,)` is a tuple; `(10)` is the integer 10.

**Implementation example:** to deduplicate hashable values while preserving first appearance, `list(dict.fromkeys(values))` is suitable. `list(set(values))` does not meet the order contract. Values such as `1`, `True` and `1.0` merge because equality and hashing treat them as the same key.

**Follow-up answered:** use a `deque` rather than repeated `list.pop(0)` for an ordinary queue. A strong answer ties each choice to the required operations and avoids claiming every immutable container is automatically hashable.

Repo: `strings.py`, `sequences.py`, `mappings_sets.py`. References: [R02: Built-in types and operations](https://docs.python.org/3.14/library/stdtypes.html), [R04: Data structures tutorial](https://docs.python.org/3.14/tutorial/datastructures.html), [R19: collections](https://docs.python.org/3.14/library/collections.html).

---

<a id="page-78"></a>

# Fresher · copying and control flow
Section: Mock interview · fresher

## F05 · Why can a copied list still change the original?

**Answer:** a shallow copy allocates a new outer list and reuses references to its elements. Appending to the copy's outer list is independent; mutating an inner shared list affects both views. A deep copy recursively copies supported contents and tracks already visited objects. Use it when an independent object graph is actually required, not as an automatic fix for unclear ownership.

```python
from copy import deepcopy

original = [[1], [2]]
copy = original.copy()
independent = deepcopy(original)
copy[0].append(9)
assert original == [[1, 9], [2]]
assert independent == [[1], [2]]
```

**Follow-up answered:** `[[0]] * 3` repeats the same inner list reference. `[[0] for _ in range(3)]` creates three lists. A strong answer states which object is new and which references remain shared. It also recognizes that copying live resources such as connections is not a general-purpose independence strategy.

## F06 · Explain break, continue, pass and a loop's else.

**Answer:** `break` exits the nearest loop; `continue` skips the remaining statements of the current iteration; `pass` performs no operation. A loop's `else` runs when the loop finishes without a break, including when its iterable is empty. An early return or uncaught exception leaves the construct rather than proceeding to its else.

In a search, loop else can represent “no match caused a break.” For `[1, 3, 4]`, breaking on the first even number skips the else. For `[1, 3]`, it runs. A helper function that returns on a match and returns a missing sentinel afterward can sometimes express the same idea more clearly.

**Follow-up answered:** removing elements from a list while iterating over it can skip shifted items. Construct a filtered list or iterate over an intentional snapshot. `range(5, 0, -2)` produces 5, 3, 1 because the stop is excluded. A strong answer predicts both the empty-loop and break cases.

Repo: `sequences.py`, `branching_loops.py`. References: [R05: Shallow and deep copying](https://docs.python.org/3.14/library/copy.html), [R03: Control flow and function definitions](https://docs.python.org/3.14/tutorial/controlflow.html).

---

<a id="page-79"></a>

# Fresher · functions and defaults
Section: Mock interview · fresher

## F07 · What is the difference between print and return?

**Answer:** `print()` writes a representation to a stream for a reader or another process. `return` supplies a value to the caller and ends the function's current execution. A function with no explicit returned value returns `None`. Printing a total does not let the caller multiply that total unless the function also returns it.

The repo's `add(first, second=5)` returns a reusable result. `sum_args(*numbers)` collects extra positional values in a tuple and returns their sum, including zero for no arguments. `**details` collects extra keyword values in a dictionary. At a call, `*` and `**` expand values rather than collect them.

**Follow-up answered:** Python binds parameter names to supplied objects. If a function appends to a supplied list, the caller sees it. If it then rebinds its parameter to another list, the caller's binding is unchanged. A strong answer avoids the inaccurate split between “mutable by reference” and “immutable by value.”

## F08 · Why is a list default dangerous? Show a correction.

**Answer:** default expressions are evaluated when `def` executes. An omitted list argument can therefore reuse one list across many calls. If that list is mutated, later calls inherit earlier results. Use a sentinel such as `None` and create a new list inside the call when omission means “fresh state.”

```python
def append_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

assert append_item("a") == ["a"]
assert append_item("b") == ["b"]
supplied = []
assert append_item("c", supplied) is supplied
```

**Follow-up answered:** `items or []` would replace an explicitly supplied empty list, breaking this function's mutation contract. If `None` is meaningful data, use a unique `object()` sentinel instead. Time-dependent defaults have the same definition-time issue. A strong test calls the function repeatedly and also passes an empty list explicitly.

Repo: `lessons/functions/arguments.py`. References: [R03: Control flow and function definitions](https://docs.python.org/3.14/tutorial/controlflow.html), [R08: Execution model and name binding](https://docs.python.org/3.14/reference/executionmodel.html).

---

<a id="page-80"></a>

# Fresher · files and failures
Section: Mock interview · fresher

## F09 · Why use with when opening a file? Explain its modes.

**Answer:** `with` closes the file when its block exits normally, returns or raises. It gives the resource an explicit lifetime instead of relying on finalization. `r` reads an existing file; `w` creates or truncates; `a` appends; `x` creates exclusively and fails if a file already exists. Binary modes operate on bytes, while text modes use strings and an encoding.

Specify `encoding="utf-8"` for a UTF-8 format. Reading advances the cursor, so a second complete read can return an empty string. `seek(0)` rewinds a supported stream. For large files, line iteration can avoid reading the entire text in one call, although accumulating every result still uses output-sized memory.

**Follow-up answered:** `Path("notes.txt")` does not create a file and resolves relative to the current working directory when used. An existence check does not guarantee a later read will succeed. A strong answer uses a temporary file example and knows that truncation happens on opening in `w`.

## F10 · Explain try, except, else, finally and raise.

**Answer:** `try` contains an operation that can fail. `except` handles matching exceptions. `else` runs if the try block completes without an exception and keeps success work out of the handler's protected region. `finally` runs on the construct's normal control-flow exits and is used for cleanup. `raise` reports or propagates failure.

Catch a specific failure you can handle. A bare `except` also catches interruption and exit signals. In `parse_integer()`, invalid numeric text becomes a helpful `ValueError` chained from the original error. A `TypeError` caused by an unsupported input type is not accidentally treated as numeric text failure.

**Follow-up answered:** returning from `finally` can override an earlier return or suppress an exception. Avoid that pattern. An error from resource cleanup can also affect the final outcome, so cleanup is not conceptually incapable of failure. A strong answer distinguishes “handle a known bad input” from “hide every error and keep going.”

Repo: `reading_writing.py`, `handling_errors.py`. References: [R07: Built-in functions](https://docs.python.org/3.14/library/functions.html), [R09: Errors and exceptions tutorial](https://docs.python.org/3.14/tutorial/errors.html), [R13: contextlib and resource management](https://docs.python.org/3.14/library/contextlib.html).

---

<a id="page-81"></a>

# Fresher · objects, modules and tests
Section: Mock interview · fresher

## F11 · What are self, instance attributes and class attributes?

**Answer:** `self` is the conventional instance parameter of an instance method. Accessing the method through an instance binds that instance automatically. Instance attributes store state for one object; class attributes provide values through class lookup and can be shared when not shadowed.

In `Dog`, `species` is a class attribute. `breed`, `name` and a new `tricks` list are assigned per instance. Appending to one dog's tricks should not affect another. Assigning `first.species = "override"` shadows the class value for that instance; it leaves `Dog.species` and the other instance's lookup unchanged.

**Follow-up answered:** `__str__` is a readable display, `__repr__` a debugging representation and `__len__` participates in length and, without `__bool__`, truth testing. The lesson's dog with an empty name is falsy because its length is zero. A strong answer distinguishes an illustrative protocol from a sensible real-world domain rule.

## F12 · Why use a main guard, and how would you test a helper?

**Answer:** `if __name__ == "__main__":` protects the program-entry call so importing the module makes its definitions available without running the demonstration. It does not stop other top-level statements or decorator application from executing. A package can expose `__main__.py` for `python -m package` execution.

For `capitalize_text()`, use `unittest` to check `"HELLO WORLD"` becomes `"Hello world"`, empty text remains empty and a non-string raises `TypeError`. The multiword case catches a wrong `.title()` implementation that a single-word test would miss. Keep tests independent of personal files and avoid interactive input.

**Follow-up answered:** run `python -m unittest discover -s tests -v` from the repository root. Use temporary directories for file behavior. Plain `assert` is useful for examples but can be disabled by optimization; external validation needs explicit exceptions. A strong answer can explain what realistic bug each test catches.

Repo: `classes.py`, `imports.py`, `tests/test_text_tools.py`. References: [R10: Classes tutorial](https://docs.python.org/3.14/tutorial/classes.html), [R27: Modules tutorial](https://docs.python.org/3.14/tutorial/modules.html), [R25: unittest](https://docs.python.org/3.14/library/unittest.html).

---

<a id="page-82"></a>

# Mid-level · signatures and closures
Section: Mock interview · mid-level

## M01 · Design a signature with positional-only and keyword-only inputs.

**Answer:** use `/` to end positional-only parameters and `*` to start keyword-only parameters. A signature such as `def export(records, /, path, *, overwrite=False): ...` lets the positional data argument keep an internal name without callers depending on it, while the flag is explicit at every call. `path` remains positional-or-keyword.

`*args` and `**kwargs` are useful for genuine forwarding, but overly broad acceptance can conceal misspellings. Repeated assignment to one ordinary parameter raises `TypeError`. At a call, iterable and mapping expansion follow the same binding rules as ordinary arguments.

**Repo nuance:** `describe_person("Ada", name="Grace")` places the keyword `name` in `details`, since the positional-only name is already supplied. Its final dictionary expansion can then override the earlier name value. If that override violates the intended data contract, reject the key or merge in a different order rather than assuming the signature prevents it.

**Follow-up answered:** omission differs from an explicit `None` only with a separate sentinel. Strong design explains why each restriction improves caller clarity and includes an invalid-call test.

## M02 · Diagnose late-bound callbacks and UnboundLocalError.

**Answer:** callbacks created in a loop can close over one binding that later changes. When `[lambda: i for i in range(3)]` is called after construction, each lambda sees the final `i` and returns 2. Capture each current value with `[lambda i=i: i for i in range(3)]` or use a factory that creates a fresh enclosing binding.

`UnboundLocalError` occurs when a function reads a local binding before assignment. `count += 1` both reads and assigns, so an inner counter function needs `nonlocal count` to rebind an enclosing function's count. `global` would target the module instead and would change the ownership model.

**Follow-up answered:** calling the factory twice gives two independent counters; merely assigning a second name to one returned counter does not. A strong answer tests independence and recognizes that a mutable object captured as a default can still be shared and changed later.

Repo: `arguments.py`, `scope.py`. References: [R03: Control flow and function definitions](https://docs.python.org/3.14/tutorial/controlflow.html), [R08: Execution model and name binding](https://docs.python.org/3.14/reference/executionmodel.html).

---

<a id="page-83"></a>

# Mid-level · laziness and decorators
Section: Mock interview · mid-level

## M03 · When does a generator validate, and how would you change it?

**Answer:** a generator function's body begins during iteration, not when the generator object is constructed. The repo's `fibonacci(-1)` therefore returns an object; its first `next()` raises `ValueError`. Once exhausted, that same object cannot be rewound by calling `iter()` or `list()` again.

To reject invalid counts immediately, use a normal outer function that validates and returns an inner generator. The outer function itself must not contain a yield. Keep the validation policy unchanged and test the time at which the error appears, not just its type.

```python
def checked_cubes(count):
    if type(count) is not int:
        raise TypeError("count must be an integer")
    if count < 0:
        raise ValueError("count must be non-negative")
    return (number**3 for number in range(count))

assert list(checked_cubes(3)) == [0, 1, 8]
```

**Follow-up answered:** a generator can retain its input and open resources, so “lazy” does not mean “no memory ownership.” A strong answer explains the caller's early-stop behavior and resource lifetime.

## M04 · What must a transparent decorator preserve?

**Answer:** forward positional and keyword arguments, return the original result and propagate failures unless a changed error contract is intentional. Use `functools.wraps` for useful metadata and `__wrapped__`. Preserve the callable's execution model too: a synchronous wrapper around an async function returns a coroutine rather than waiting for its completion.

In `announce()`, the before message appears first, then the original executes, then the after message appears only on success. Move an always-required action into `finally`; do not label a cleanup event as successful completion. Stacked decorators apply inside out and can change caching, retry or logging semantics depending on order.

**Follow-up answered:** a retry or repetition decorator can duplicate side effects. It requires an explicit retryable-error policy, deadline and idempotency assumptions rather than merely a loop. A strong test covers return values, keyword-only arguments, metadata and an exception path.

Repo: `generators.py`, `decorators.py`. References: [R06: Python data model](https://docs.python.org/3.14/reference/datamodel.html), [R11: functools: wraps, caching and partial](https://docs.python.org/3.14/library/functools.html).

---

<a id="page-84"></a>

# Mid-level · hashing and domain objects
Section: Mock interview · mid-level

## M05 · What makes a valid dictionary key? Why is 1 like True here?

**Answer:** a key must be hashable and maintain a hash consistent with equality. Equal hashable objects must have equal hashes, but the converse is not required; collisions are resolved with equality checks. The hash must stay stable while the key is stored. A changing value-based hash can make a key effectively unreachable through normal lookup.

`1`, `True` and `1.0` compare equal and have matching hashes, so a set stores one such value and a dictionary treats them as the same key. A tuple containing a list is unhashable because its element is unhashable. An ordinary custom instance can instead use identity equality and hashing even if its attributes change, so immutability alone is not the formal definition.

**Follow-up answered:** defining `__eq__` without a compatible hash normally makes the class unhashable. A mutable dataclass commonly behaves this way. Do not apply `unsafe_hash` merely to silence an error; first establish stable equality semantics. A strong answer can explain both collisions and mutation hazards without conflating them.

## M06 · When is a dataclass enough, and when do you add validation?

**Answer:** a dataclass is useful for record-like domain state because it generates initialization, representation and value-based equality. It does not enforce annotated types. The tracker's `Task` is enough for validated internal records, but `Task(True, "", "false")` can still be constructed directly unless checks are added.

Use `__post_init__` for construction invariants, a property or controlled operations for invariants that must survive later mutation, and a `default_factory` for independent mutable fields. `frozen=True` blocks ordinary reassignment but does not recursively freeze a nested list. Generated equality relies on each field's equality, which can still be identity-based for a custom collaborator.

**Follow-up answered:** validation of JSON belongs before constructing trusted tasks. If the same class becomes a public library API, consider strengthening its construction contract and documenting the compatibility impact. A strong answer separates a convenience feature from a complete domain and schema policy.

Repo: `mappings_sets.py`, `model.py`, `storage.py`. References: [R06: Python data model](https://docs.python.org/3.14/reference/datamodel.html), [R14: dataclasses](https://docs.python.org/3.14/library/dataclasses.html), [R18: JSON encoding and decoding](https://docs.python.org/3.14/library/json.html).

---

<a id="page-85"></a>

# Mid-level · error boundaries and imports
Section: Mock interview · mid-level

## M07 · How should a library translate failures without hiding defects?

**Answer:** catch only errors the layer understands. Add domain context when it improves the caller's ability to act, and chain the original cause with `raise NewError(...) from error`. Keep the protected try block narrow so a programming error in later success code is not mislabeled as a parsing failure.

The tracker returns empty data only for a missing file, not for malformed JSON. Its CLI catches expected data and filesystem errors, prints to standard error and returns 1. Unexpected defects should retain useful tracebacks during development. A library helper should not call process exit merely because the CLI would eventually return an error status.

**Follow-up answered:** returning from `finally` can suppress a pending exception, and a cleanup failure can mask an original failure. A context manager gives a structured lifetime but must still avoid unintended suppression. Strong tests assert old data survives a failed write and the failure remains visible.

## M08 · Why can an import be quiet yet still perform work?

**Answer:** the first import executes top-level statements: definitions, class bodies, default expressions and decorator calls. A main guard protects the demonstration call, not the rest of the module. “Quiet” means no unexpected output or prompt, not zero initialization cost.

Initialized modules are normally cached in `sys.modules`, so reimporting in one interpreter reuses them. `from source import value` binds the current object locally; a later rebind of `source.value` does not automatically rebind that imported name. A shared mutable object can still expose mutations through both references.

Circular imports can encounter partially initialized modules. Reduce the cycle by moving shared concepts into a lower-level module or changing dependency direction. Local imports can be justified for optional or timing-sensitive behavior, but should not be a default patch for tangled architecture.

**Follow-up answered:** module reload is not equivalent to restarting the process: existing references can keep old objects. A strong answer uses `python -m` for package execution and investigates shadowing with `module.__file__` before changing import paths.

Repo: `handling_errors.py`, `imports.py`, `tests/test_runner.py`. References: [R09: Errors and exceptions tutorial](https://docs.python.org/3.14/tutorial/errors.html), [R27: Modules tutorial](https://docs.python.org/3.14/tutorial/modules.html).

---

<a id="page-86"></a>

# Mid-level · testing and malformed data
Section: Mock interview · mid-level

## M09 · Design tests for a persistence function, including failures.

**Answer:** first state observable guarantees: a missing file starts empty, valid tasks round-trip, invalid data raises, failed replacement preserves prior content and read-only commands do not create files. Use a fresh temporary directory for each test. Include Unicode, empty storage, duplicate IDs, wrong fields and wrong types.

Use real small files for encoding and replacement behavior. Inject an `OSError` for the replacement step to reach the otherwise uncommon failure path, then assert both the old destination and staging cleanup. A test that only verifies a method call does not prove data preservation.

Mock dependencies where the tested module looks them up. Direct CLI tests can pass an argument list and capture stdout/stderr. Add a small real subprocess workflow to verify package execution, argument parsing and exit codes. Keep timeouts and avoid writing into personal `.practice` data.

**Follow-up answered:** line coverage cannot prove the assertions distinguish correct behavior. An intentionally wrong `.title()` implementation is a good mental mutation for evaluating the text tests. A strong answer identifies a plausible bug for each case.

## M10 · Why isn't successful JSON decoding enough for the tracker?

**Answer:** syntactically valid JSON can be a number instead of a list or contain records with blank titles, string completion flags, duplicate IDs or unexpected fields. Parsing establishes syntax, not the domain schema. Validate top-level structure, exact record keys, field types, allowed ranges and uniqueness before constructing trusted objects.

IDs require exact integer type so `True` does not become ID 1. A title must be nonempty after whitespace checking, and done must be a real boolean. The loader currently preserves a valid title's original whitespace while add trims a new title; that difference should be understood before changing normalization policy.

**Follow-up answered:** catching every loader error and returning `[]` could cause a later save to overwrite corrupt original data. Preserve the file and report a clear error instead. A strong answer also recognizes schema evolution: the exact-key policy means a new field needs an explicit migration or compatibility rule.

Repo: `tests/test_task_tracker.py`, `storage.py`. References: [R25: unittest](https://docs.python.org/3.14/library/unittest.html), [R26: unittest.mock: where to patch](https://docs.python.org/3.14/library/unittest.mock.html#where-to-patch), [R18: JSON encoding and decoding](https://docs.python.org/3.14/library/json.html).

---

<a id="page-87"></a>

# Mid-level · time and streaming performance
Section: Mock interview · mid-level

## M11 · How would you implement a due date and a timestamp correctly?

**Answer:** separate a date-only deadline from an exact instant. A task due on a calendar day can use `date` and an ISO `YYYY-MM-DD` representation. A completion timestamp needs an aware datetime and an explicit zone/UTC policy. Do not silently treat a naive value as UTC or server-local time without a contract.

Use `astimezone()` for conversion. Merely assigning a new `tzinfo` can reinterpret the same wall-clock fields rather than preserve the instant. Regional schedules need `ZoneInfo` and a policy for ambiguous or nonexistent daylight-saving times. Persist the local scheduling intent and zone when recurrence depends on them.

The loader's exact-field check means adding either value requires a schema change. Decide whether old records receive `None`, how dates are validated and how rollback behaves. Inject a clock for repeatable “overdue” tests. Use `.total_seconds()` rather than `.seconds` for full elapsed durations.

**Follow-up answered:** performance timing belongs on a monotonic clock, not a business wall-clock timestamp. Strong design treats date-only and instant fields as different domain concepts.

## M12 · Make a large-file transform efficient without breaking its contract.

**Answer:** identify the required result before changing allocation. If the caller needs a list, the output must ultimately be stored somewhere. You can still avoid reading all input and several intermediate collections at once. If the caller accepts a stream, yield results from bounded parsing and transformation stages.

Define resource ownership, validation timing and error behavior. Returning a generator from inside a completed file `with` can leave it trying to read a closed stream. Owning the `with` inside a generator keeps it open during consumption, but early abandonment then needs an explicit close/lifetime plan. A caller-owned stream or context-managed iterator can make that responsibility clearer.

Measure realistic peak memory and end-to-end time. Avoid repeated list membership when a hashable-key set is valid. Do not blindly materialize a generator to log it before use.

**Follow-up answered:** a terminal `list(results)` removes the benefit of streaming the output, though intermediate memory can still be lower. A strong answer names both the retained references and the first point an error can reach the caller.

Repo: `dates_times.py`, `reading_writing.py`, `generators.py`. References: [R20: datetime](https://docs.python.org/3.14/library/datetime.html), [R21: zoneinfo](https://docs.python.org/3.14/library/zoneinfo.html), [R12: itertools: iterator building blocks](https://docs.python.org/3.14/library/itertools.html).

---

<a id="page-88"></a>

# Senior · memory ownership and object design
Section: Mock interview · senior

## S01 · A process grows in memory although objects are deleted. Diagnose it.

**Answer:** first distinguish rising resident memory from growing reachable Python allocations. `del` removes a binding, not every reference. Inspect caches, closure cells, generator frames, queues, event handlers and container graphs that may still retain objects. Cycles may require cyclic collection in CPython; native libraries and allocator reuse complicate process-memory interpretation.

Reproduce with a bounded representative workload. Take `tracemalloc` snapshots before and after repeated operations and compare allocation sites. Start tracing before the suspected allocations. Correlate with process metrics if native allocations matter. `sys.getsizeof()` is shallow and cannot by itself measure a retained graph; shared references also make naive recursive sums inaccurate.

Remove the unintended owner, bound a cache/queue or shorten a resource lifetime. Verify memory reaches an acceptable steady state after repeated workloads. Do not simply insert `gc.collect()` in a hot loop without evidence: it cannot free an object that remains reachable and can add latency.

**Follow-up answered:** a generator can hold a large source even after yielding one small result. Exhausting or deliberately closing it can release frame references, depending on remaining owners. Strong diagnosis identifies what retains data and measures the fix rather than inferring a leak from one process-memory reading.

## S02 · Design a mutable domain object with reliable equality and hashing.

**Answer:** decide whether equality represents entity identity or complete value equality. For a task entity, a stable identifier may define identity, while title and done are mutable state. For a value object, equality may use all fields, favoring immutable contents. Document cross-type behavior and return `NotImplemented` for unsupported comparisons where appropriate.

Never derive a stored dictionary key's hash from fields that can change. A mutable value-equal dataclass is normally unhashable, which prevents this hazard. Prefer an immutable stable key such as a validated task ID for indexes, or an immutable value object with hashable fields when value hashing is required. `frozen=True` alone does not make nested objects immutable or every instance hashable.

**Follow-up answered:** `Task` currently has generated field equality and no durable cross-process identity semantics beyond its stored integer ID. If introducing entity equality, update tests and callers that rely on current value comparison. A strong answer considers migration of behavior and avoids `unsafe_hash=True` as a superficial workaround.

Repo: `generators.py`, `model.py`. References: [R06: Python data model](https://docs.python.org/3.14/reference/datamodel.html), [R14: dataclasses](https://docs.python.org/3.14/library/dataclasses.html), [R36: tracemalloc](https://docs.python.org/3.14/library/tracemalloc.html).

---

<a id="page-89"></a>

# Senior · profiling and cache correctness
Section: Mock interview · senior

## S03 · A Python data transform is slow. What do you measure and change?

**Answer:** define a representative workload and a target: throughput, tail latency or memory. Record Python implementation/build, data distribution and I/O conditions. Profile the end-to-end path to distinguish parsing, computation, waiting and output. Use repeated microbenchmarks only after identifying a narrow candidate; a tiny faster expression may not affect total runtime.

Look for algorithmic causes first: nested membership scans, repeated sorting, repeated serialization or unnecessary copies. A set index can replace linear membership if hashability and equality meet the contract. A generator can reduce intermediate allocation, but it does not eliminate consumed work and may shift errors. Include data sizes large enough to expose growth behavior.

Verify the same output, ordering, mutation and exception contracts after the change. Report a measured comparison with uncertainty rather than a universal speed claim. If the bottleneck is external I/O, reducing Python arithmetic may have no meaningful effect.

**Follow-up answered:** compare cumulative profiler time to understand expensive call subtrees, but account for instrumentation overhead. Strong answers describe how they would reject an optimization when representative measurements show no worthwhile benefit.

## S04 · What can go wrong with lru_cache on a useful helper?

**Answer:** a cache is correct only when its key represents every relevant input and results remain valid for the intended lifetime. Hidden global configuration, file contents or current time can make cached results stale. Arguments must be hashable; returned mutable objects may be shared across callers. Bound entry count does not bound bytes when value sizes vary widely.

Define invalidation, maximum memory, hit-rate goals and ownership of returned values. For mutable results, return immutable representations or intentional copies if that cost is acceptable. For methods, cache keys can retain instances. Concurrent misses can compute more than once even when cache bookkeeping is synchronized, so side effects still need a separate policy.

Do not cache tracker file loads without a reliable change/version signal; otherwise another process's updates can be hidden. For pure expensive calculations, standard caching may be ideal. Measure hit rate and compute cost to confirm the tradeoff.

**Follow-up answered:** caching exceptions or transient failures requires an explicit policy and expiry; a normal result cache is not automatically a negative-cache strategy. Strong answers explain both correctness and operational visibility.

References: [R34: Profiling Python programs](https://docs.python.org/3.14/library/profile.html), [R35: timeit](https://docs.python.org/3.14/library/timeit.html), [R11: functools: wraps, caching and partial](https://docs.python.org/3.14/library/functools.html).

---

<a id="page-90"></a>

# Senior · concurrency and cancellation
Section: Mock interview · senior

## S05 · Does the GIL make a shared counter or tracker update safe?

**Answer:** no. In conventional GIL-enabled CPython, the GIL limits simultaneous Python bytecode execution, but a multi-step invariant can still be interleaved. A read/check/compute/write sequence is not made transactional by the GIL. Native operations can release it, and free-threaded builds change the execution model further.

Use a lock around the complete shared-memory invariant, not merely the last assignment. For several processes updating a file, a thread lock is insufficient. Even an interprocess lock must cover read, validate, modify and commit, with all writers participating. A database transaction is often clearer when concurrent persistent updates are a real requirement.

State the interpreter configuration. Free-threaded CPython began in 3.13 and has supported status in 3.14 under PEP 779, but the runtime build and extension ecosystem matter. Test shared-state assumptions on the deployed build rather than asserting “Python cannot run threads in parallel.”

**Follow-up answered:** atomicity of a single container operation does not establish correctness of a business sequence. Strong answers locate the invariant, its owners and the scope over which synchronization must hold.

## S06 · How do you keep an async pipeline bounded and cancellable?

**Answer:** use asynchronous libraries for I/O that actually cooperate with the event loop. Bound concurrent tasks and queue sizes so an input spike cannot create unlimited retained work. Apply deadlines and propagate cancellation through task ownership. Use `try/finally` or async context managers to release resources; do not swallow cancellation as an ordinary retryable error.

Blocking calls stall the loop even when placed inside `async def`. Move suitable blocking I/O to a controlled thread executor or use an async API. For CPU-heavy Python work, consider a process pool or a verified free-threaded/native strategy, accounting for serialization and deployment constraints. Offloading does not make the underlying operation instantly cancellable.

**Follow-up answered:** a client timeout can occur after a persistent change committed. Cancellation therefore needs an operation/result contract, not just task cleanup. Use idempotency or a way to query the outcome when retries can duplicate work. Strong answers distinguish stopping a waiter from reversing an external side effect.

References: [R30: CPython free-threading guide](https://docs.python.org/3.14/howto/free-threading-python.html), [R39: PEP 779: supported free-threaded Python](https://peps.python.org/pep-0779/), [R43: Thread synchronization and locks](https://docs.python.org/3.14/library/threading.html), [R31: concurrent.futures](https://docs.python.org/3.14/library/concurrent.futures.html), [R32: asyncio overview](https://docs.python.org/3.14/library/asyncio.html).

---

<a id="page-91"></a>

# Senior · persistence and schema evolution
Section: Mock interview · senior

## S07 · Why doesn't the tracker's file replacement prevent lost updates?

**Answer:** replacement only concerns publishing one prepared file. Suppose A and B both load version 1. A adds task X and replaces the file with its result. B adds task Y to its stale copy and replaces the file, erasing X. Unique staging filenames prevent staging collisions but do not resolve the stale-read conflict.

For the existing single-writer scope, document the limitation. If retaining files under concurrent writers, use a robust interprocess lock covering the full operation and define lock failure and crash behavior. For growing requirements, use a transactional database with generated unique IDs and explicit constraints. Optimistic version checks need an atomic compare-and-commit mechanism; comparing a version in user code before an unrelated write is still racy.

Crash durability is separate from lost-update prevention and atomic visibility. Define whether a successful response must survive process failure, host restart or power loss, then choose commit and flush behavior accordingly.

**Follow-up answered:** the current fixed staging path can also let writers delete or replace each other's staging. Strong answers separate these two races and identify which guarantee each proposed change actually adds.

## S08 · Add an optional due date without silently breaking old files.

**Answer:** first choose a schema policy. The current loader requires exactly three keys, so old and new records cannot be mixed casually. One approach is a versioned envelope with a records list and a migration from legacy lists to the new schema. Another is a carefully documented backward-compatible optional field rule. Choose deliberately rather than weakening all validation.

Represent a date-only deadline as an ISO date or null; reject impossible dates and wrong types. Parse into a domain value before use. Define whether saving old data upgrades the format and whether downgrade/rollback is supported. Preserve a recoverable original and make repeated migration idempotent.

Test a legacy file, a new file with null, a valid date, an invalid leap day, a malformed envelope and a future unsupported version. Keep migration separate from ordinary domain operations so callers can inspect what changed.

**Follow-up answered:** adding a dataclass default does not update the loader's exact-key check or the persisted schema. Strong answers trace every affected layer and define user-visible recovery if migration fails.

Repo: `storage.py`, `tests/test_task_tracker.py`. References: [R17: pathlib](https://docs.python.org/3.14/library/pathlib.html), [R18: JSON encoding and decoding](https://docs.python.org/3.14/library/json.html), [R20: datetime](https://docs.python.org/3.14/library/datetime.html), [R33: sqlite3 and transaction control](https://docs.python.org/3.14/library/sqlite3.html).

---

<a id="page-92"></a>

# Senior · test strategy and compatibility
Section: Mock interview · senior

## S09 · How do you test a storage abstraction without overmocking?

**Answer:** write contract tests for the behavior all adapters must share: fresh storage, valid round-trip, stable identity, invalid input, no silent corruption and failure reporting. Run the same cases against JSON and any future database adapter. Use a real temporary filesystem or real disposable database for persistence semantics; mocks cannot prove those systems behave as assumed.

Keep fast pure model tests for business rules. Inject failures at meaningful boundaries such as commit or replacement, then assert preserved data and visible error outcomes. Add a small number of subprocess workflows for the installed/module command. Make concurrency tests coordinate a specific race with barriers rather than relying on arbitrary sleeps.

Property-oriented tests can check invariants such as `done + pending == total` across many valid task collections. Such tests supplement targeted examples; they do not replace explicit expectations about corruption or exit codes.

**Follow-up answered:** a perfectly mocked repository may pass while encoding, transaction or import behavior fails in reality. Strong answers keep test doubles narrow, independently manage fixtures and distinguish deterministic evidence from broad confidence claims.

## S10 · Support Python 3.10+ while using modern features responsibly.

**Answer:** define an explicit supported-version range and run tests on those interpreters in CI. Use syntax and standard-library APIs available at the minimum version or provide a justified compatibility path. A successful run on a newer interpreter does not prove the code parses or behaves the same on the minimum one.

The repo's `zip(strict=True)`, union annotations and dataclass slots fit the 3.10 baseline. `asyncio.TaskGroup`, newer type-parameter syntax and later annotation semantics require version-aware treatment if introduced. Check official version notes rather than assuming all documentation examples apply to the baseline.

Separate language behavior from CPython internals, especially memory management, bytecode and threading assumptions. Test quiet imports and module entry points. If distributing, validate installation in a clean environment as well as execution from the source checkout.

**Follow-up answered:** feature detection can help with optional runtime APIs, but cannot make unsupported syntax parse. Strong answers define deprecation and release policies and keep documentation honest about which matrix runs actually completed.

References: [R25: unittest](https://docs.python.org/3.14/library/unittest.html), [R26: unittest.mock: where to patch](https://docs.python.org/3.14/library/unittest.mock.html#where-to-patch), [R28: Virtual environments tutorial](https://docs.python.org/3.14/tutorial/venv.html), [R45: Packaging Python projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/).

---

<a id="page-93"></a>

# Senior · interfaces, retries and failure semantics
Section: Mock interview · senior

## S11 · When would you choose composition, a protocol or inheritance?

**Answer:** begin with the behavior the caller needs. Use composition when an object owns or delegates to a collaborator that can vary, such as storage or a clock. A structural protocol documents the required shape without forcing independently developed implementations into one hierarchy. Use inheritance when substitutability and shared behavior form a coherent, stable abstraction.

Avoid deep hierarchies created only to share a few lines. In multiple inheritance, `super()` follows the MRO; cooperative implementations need compatible signatures and consistent delegation. A subtype that rejects ordinary base inputs or violates promised outcomes is not behaviorally substitutable simply because `isinstance()` succeeds.

For the tracker, plain model functions remain sensible. A storage protocol earns its place once there are actual interchangeable adapters and common contract tests. Keep methods specific enough to express transactions; a generic “load everything, save everything” interface can make a database adapter preserve a weak concurrency model.

**Follow-up answered:** runtime protocol checks do not verify every method's semantic contract. Strong answers use types for communication and tests/design for behavior, rather than claiming either is a complete substitute for the other.

## S12 · Design a retry decorator for a state-changing operation.

**Answer:** first ask whether retry is safe. Classify transient failures, set a total deadline, bound attempts and use backoff with jitter where appropriate. Preserve arguments, result, metadata and the original failure information. Do not retry validation failures or all exceptions indiscriminately.

If the operation can commit before the caller sees an error, retries can duplicate it. Require an idempotency key or an operation-specific reconciliation strategy. Store the key and outcome atomically with the change; a process-local dictionary is insufficient across workers or restarts. Define what happens when the same key arrives with different inputs.

A synchronous decorator is not automatically correct for coroutines or generators. Cancellation should normally propagate; a retry policy should not silently restart work after the caller's deadline. Emit attempts and final outcomes without logging sensitive payloads.

**Follow-up answered:** completing a task is state-idempotent in the sample, but adding is not. Even repeated completion could produce duplicate notifications if notifications are added later. Strong answers define idempotency over the entire observable operation, not only one field assignment.

References: [R15: typing and structural protocols](https://docs.python.org/3.14/library/typing.html), [R10: Classes tutorial](https://docs.python.org/3.14/tutorial/classes.html), [R11: functools: wraps, caching and partial](https://docs.python.org/3.14/library/functools.html), [R37: logging](https://docs.python.org/3.14/library/logging.html).

---

<a id="page-94"></a>

# Architect · requirements and persistence
Section: Mock interview · architect

## A01 · Turn the local tracker into a team tool. Where do you start?

**Answer:** establish requirements before choosing a server or database. Ask how many users act concurrently, whether access is local or remote, whether edits must be immediately consistent, how tasks are owned and which failures must be recoverable. Define data sensitivity, latency, expected volume, offline needs and operational ownership.

Preserve the useful domain vocabulary but review the contract. Local integer IDs, one-writer files and unrestricted functions are not automatically suitable for a shared service. Introduce an application boundary that accepts a validated command plus caller context, authorizes it, performs a transactional change and returns a stable result. Keep presentation separate from these operations.

Choose the smallest persistence model that meets the requirements. A local multi-process tool may fit SQLite; a remotely accessed multi-user deployment may justify a database service and authentication boundary. Do not add distributed workers merely because the word “team” appears.

**Acceptance evidence:** contract tests, concurrent-update tests, restore drills, authorization checks and measured workload behavior. Roll out behind an adapter or limited migration with a recoverable source. A strong answer names assumptions, identifies changed guarantees and proposes a staged implementation rather than a technology shopping list.

## A02 · Replace JSON with SQLite while preserving meaningful behavior.

**Answer:** map task IDs to a primary key and express feasible invariants with constraints: non-null title, a nonblank-title rule and a constrained completion representation. Define transaction ownership at the application operation boundary. Insert and ID allocation must be coordinated by the database rather than `max(existing_ids) + 1` in separate reads.

Use parameterized SQL, explicit commit/rollback behavior and deterministic connection lifetime. Configure transaction semantics deliberately for the supported Python versions; newer `sqlite3` transaction APIs do not automatically exist at the 3.10 baseline. Understand SQLite's concurrent-writer limits before selecting it for the expected workload.

Expose operations such as add or complete through the adapter so transactions can span the necessary work. Retaining only a load-all/save-all interface can recreate lost updates on top of a better storage engine. Migrate with validation, backups and a clear cutover rule; compare record counts and identities before accepting success.

**Follow-up answered:** `with connection` manages transaction outcomes but should not be confused with a universal promise to close the connection. Strong answers verify exact API semantics and run the same behavioral contracts against old and new adapters.

References: [R33: sqlite3 and transaction control](https://docs.python.org/3.14/library/sqlite3.html), [R18: JSON encoding and decoding](https://docs.python.org/3.14/library/json.html), [R25: unittest](https://docs.python.org/3.14/library/unittest.html).

---

<a id="page-95"></a>

# Architect · concurrent edits and idempotency
Section: Mock interview · architect

## A03 · Two users edit one task. Prevent an unexplained lost update.

**Answer:** first define the conflict policy. For a task rename, optimistic concurrency can attach a version to the record. A command includes the version the user saw. An update checks ID and expected version atomically, increments the version on success and reports a conflict when no row matches. The caller can reload, present the competing edit or apply a domain-approved merge.

```sql
UPDATE tasks
SET title = ?, version = version + 1
WHERE id = ? AND version = ?;
```

This is an implementation sketch: validate and authorize before execution, and interpret the affected-row count inside the appropriate transaction. Distinguish a missing task from a stale version if the user contract needs that detail. Do not implement the check as a separate unprotected read followed by an unconditional update.

For highly contended multi-record invariants, evaluate transaction isolation and locking instead. Define bounded retries and avoid holding locks while waiting for a user's decision. Add tests that force two actors to use one starting version and verify exactly the chosen conflict behavior.

**Follow-up answered:** last-writer-wins can be a valid explicit policy for some data, but it should not be an accidental consequence of file replacement. Strong answers choose conflict semantics from the domain rather than defaulting to silent overwrite.

## A04 · A client times out after add. How can it retry safely?

**Answer:** use a client-supplied idempotency key with a defined scope, such as actor and operation. Persist the key, a fingerprint of validated input and the result in the same transaction as task creation. A repeated matching request returns the original outcome; reuse with a different input is rejected. A unique constraint coordinates concurrent submissions using the same key.

Define retention and behavior after expiry, treatment of in-progress operations and recovery from uncertain outcomes. Do not label the system exactly-once merely because a cache deduplicates requests. Network delivery and external side effects have separate failure modes.

**Follow-up answered:** a notification sent after commit can still duplicate or be lost around a crash. An outbox stored with the transaction plus an idempotent consumer can bridge that boundary with explicit delivery semantics. Strong answers trace “committed, response lost” and “committed, publisher crashed” separately and explain the evidence clients can query.

References: [R33: sqlite3 and transaction control](https://docs.python.org/3.14/library/sqlite3.html), [R37: logging](https://docs.python.org/3.14/library/logging.html).

---

<a id="page-96"></a>

# Architect · workload and streaming design
Section: Mock interview · architect

## A05 · Choose threads, processes or async for a new Python workload.

**Answer:** characterize the work: CPU versus I/O, existing library interfaces, expected concurrency, latency targets and state sharing. For blocking I/O with modest concurrency, bounded threads may be simplest. For many cooperative network operations, async can reduce the overhead of many waiting threads but demands compatible I/O and disciplined task ownership. For CPU-heavy Python work on a conventional GIL build, processes are a common starting point.

Account for process startup, serialization, memory duplication and import-safe workers. A free-threaded CPython build or native code that releases the GIL can change the choice, but requires verified compatibility and measurement. Do not infer runtime behavior from the language name alone.

Bound submitted work and define backpressure, timeouts, cancellation and shutdown. Choose where errors are observed and which work can safely retry. Measure realistic end-to-end latency and resource use, including queueing. A library API that blocks cannot be made cooperative just by calling it inside `async def`.

**Follow-up answered:** switching the tracker to async does not fix persistent concurrent updates. That guarantee belongs in the storage/application transaction design. Strong answers separate execution scheduling from consistency and keep the simplest mechanism that meets the measured requirement.

## A06 · Import a dataset much larger than memory, with malformed records.

**Answer:** define the input framing and error policy first. A line-delimited format can be parsed one record at a time more easily than one enormous JSON array with the standard decoder. Decide whether one invalid record aborts the whole import, rejects only that record or stops the current batch. Report locations and counts without exposing sensitive payloads.

Build a bounded read/parse/validate/transform/write pipeline. Bound queues and batch sizes; commit at a documented unit so partial progress is understandable. Use stable source identifiers or checkpoints for restart, and make resumed writes idempotent. Keep a recoverable input and record schema/version information with outcomes.

Sorting the whole dataset or collecting every rejected record in memory defeats streaming. Use external sorting, bounded diagnostics or durable reject output when required. `tee()` can silently buffer unbounded lag between consumers; prefer explicit fan-out with limits.

**Follow-up answered:** a successful checkpoint must correspond to committed output, not merely parsed input, or restart can skip unwritten work. Strong answers trace a failure between processing and commit and define what a restart repeats.

References: [R30: CPython free-threading guide](https://docs.python.org/3.14/howto/free-threading-python.html), [R31: concurrent.futures](https://docs.python.org/3.14/library/concurrent.futures.html), [R32: asyncio overview](https://docs.python.org/3.14/library/asyncio.html), [R12: itertools: iterator building blocks](https://docs.python.org/3.14/library/itertools.html), [R18: JSON encoding and decoding](https://docs.python.org/3.14/library/json.html).

---

<a id="page-97"></a>

# Architect · plugins and trust boundaries
Section: Mock interview · architect

## A07 · Design a Python plugin boundary for alternative storage/reporting.

**Answer:** define a small versioned contract around actual use cases. A storage plugin may need transactional operations and query interfaces; a reporting plugin may only need read-only records. Use protocols or an abstract base where they improve communication, with semantic documentation for ordering, ownership, failure types and resource lifetime.

Load plugins at an explicit application boundary rather than letting arbitrary imports launch work. Keep optional dependencies isolated and report compatibility errors clearly. Provide contract tests for each implementation. Decide lifecycle rules for initialization, cleanup and configuration, and an error policy when a plugin fails halfway through an operation.

Trusted in-process plugins execute with the host process's privileges and can mutate shared state. A protocol or a restricted-looking Python object is not a security sandbox. If plugins are untrusted, use an isolation boundary designed for that threat model, with a constrained communication schema and resource controls.

**Follow-up answered:** importing a plugin in a subprocess can isolate crashes and state, but is not automatically a complete permission sandbox. Strong answers distinguish extensibility, fault isolation and hostile-code containment and avoid unnecessary plugin machinery when only one implementation exists.

## A08 · Which checks protect a Python service at its input boundary?

**Answer:** parse a bounded format, validate shape and types, authorize the actor for the requested object/operation and enforce domain invariants transactionally. These are separate checks. Type hints do not validate JSON; valid JSON does not establish permission; permission does not make a state transition valid.

Use explicit schemas and limits for sizes, counts, nesting and expensive operations. Avoid `eval()` and untrusted pickle. Parameterize SQL and define a filesystem path policy when user input selects files. Use `secrets` for security-sensitive random tokens and keep secrets out of logs. A general regex validator should not introduce an unbounded computational path.

At the application boundary, turn expected failures into stable error categories without exposing internal paths or stack details unnecessarily. Preserve diagnostic causes in controlled logs. Use least capability in plugin and adapter interfaces where practical.

**Follow-up answered:** rejecting unknown fields can reveal typos and incompatible clients, but versioning may call for a documented tolerant policy. Strong answers choose the compatibility rule explicitly and test both malformed and well-formed-but-unauthorized cases.

References: [R15: typing and structural protocols](https://docs.python.org/3.14/library/typing.html), [R27: Modules tutorial](https://docs.python.org/3.14/tutorial/modules.html), [R18: JSON encoding and decoding](https://docs.python.org/3.14/library/json.html), [R24: secrets](https://docs.python.org/3.14/library/secrets.html), [R44: pickle security warning](https://docs.python.org/3.14/library/pickle.html).

---

<a id="page-98"></a>

# Architect · recovery and evolution
Section: Mock interview · architect

## A09 · Define a migration and recovery plan before changing storage.

**Answer:** begin with recovery objectives: acceptable data loss, acceptable downtime and which failures must be recoverable. Inventory the old schema and invalid records. Design a deterministic migration with an explicit source/target version, validation report and recoverable original. A backup is useful only if a restore procedure works.

For a small local app, a maintenance-window conversion may be safer and simpler than dual writes. For a live service, choose staged schema changes compatible with old and new code, then a controlled cutover. Dual-write approaches create reconciliation problems unless atomicity and divergence recovery are designed.

Verify counts, IDs, required invariants and representative content. Rehearse on realistic data and inject interruption around checkpoints. Define whether rerunning resumes, safely repeats or refuses partial state. Keep rollback expectations honest: once new-format writes occur, restoring the old code alone may not restore compatibility.

**Follow-up answered:** atomic rename does not provide backup history or prove power-loss durability. Strong answers identify where source truth lives during migration, who can write at each stage and how recovery is tested rather than assumed.

## A10 · How would you govern Python versions and dependencies over time?

**Answer:** publish the supported interpreter range and implementation assumptions, test it in automation and make upgrades deliberate. Track syntax/API requirements separately from dependency compatibility. A Python 3.10 baseline cannot use later syntax behind an ordinary runtime `if`; the file must parse before the condition executes.

Build and test the installed artifact in clean environments, not only the source tree. Keep dependency declarations clear, use a repeatable resolution strategy appropriate to the deployment and test optional adapters independently. Evaluate new interpreter builds with representative workloads, native extensions and concurrency tests before switching production behavior.

Define deprecation windows, release notes and rollback criteria. Pinning every component forever trades update risk for accumulated maintenance risk; unbounded automatic upgrades trade predictability for freshness. Choose a managed cadence with evidence and ownership.

**Follow-up answered:** free-threaded CPython changes extension and thread-safety assumptions, so it is a deployment choice requiring verification rather than merely changing a version string. Strong answers describe a compatibility matrix, real completed results and a staged rollout with observable success criteria.

References: [R18: JSON encoding and decoding](https://docs.python.org/3.14/library/json.html), [R33: sqlite3 and transaction control](https://docs.python.org/3.14/library/sqlite3.html), [R28: Virtual environments tutorial](https://docs.python.org/3.14/tutorial/venv.html), [R39: PEP 779: supported free-threaded Python](https://peps.python.org/pep-0779/), [R45: Packaging Python projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/).

---

<a id="page-99"></a>

# Architect · operations and design synthesis
Section: Mock interview · architect

## A11 · Design observability that helps diagnose Python failures.

**Answer:** start from questions operators must answer: which operation failed, for whom or which object, before or after commit, and whether a retry is safe. Emit structured events with correlation IDs, operation IDs, outcome categories and durations. Configure logs at the application boundary and avoid secret or excessive payload logging.

Measure latency distributions, throughput, failure rates, queue depth, retry counts and resource consumption. Add storage-specific indicators such as conflict rate, commit failures and recovery attempts. Correlate symptoms with deployed version and configuration. An average can hide severe tail latency, while a count without a denominator can mislead.

Define actionable alerts around user impact and saturation rather than every exception. Include a runbook for corruption, failed migration and uncertain operation outcomes. Use sampling or bounded diagnostics to avoid turning an incident into a logging outage. Test that error paths emit useful context without accidentally reporting success.

**Follow-up answered:** profiling is usually a diagnostic tool, not a replacement for production metrics. Strong answers connect each signal to an operational decision and state retention/privacy rules for diagnostic data.

## A12 · Propose an incremental architecture for the evolved tracker.

**Answer:** keep domain rules small and independent of the interface. Add an application layer with explicit commands and transaction boundaries. Put validation and authorization at the appropriate ingress, use typed domain values where they clarify invariants and place persistence behind operations that can preserve those invariants atomically.

Start with one deployable application and a transactional store if that meets the requirements. Add optimistic versions for competing edits and idempotency records for retryable creates. Use an outbox only if reliable external side effects are required. Introduce queues or separate services when workload or ownership evidence justifies their operational cost.

Preserve fast model tests, add shared adapter contracts and test actual concurrent/failed workflows. Migrate in reversible stages with a known source of truth, measurable acceptance criteria and a restore plan. Document what remains outside the guarantee, such as offline conflict merging or multi-region failover, until it is explicitly designed.

**Follow-up answered:** a successful architecture review ends with a concrete next change and verification plan. For this repo, a sensible first step may simply be a complete rename feature; for confirmed concurrent writers, it may be a transactional SQLite adapter. Strong judgment matches complexity to a stated requirement and revisits the decision as evidence changes.

References: [R37: logging](https://docs.python.org/3.14/library/logging.html), [R33: sqlite3 and transaction control](https://docs.python.org/3.14/library/sqlite3.html), [R15: typing and structural protocols](https://docs.python.org/3.14/library/typing.html), [R25: unittest](https://docs.python.org/3.14/library/unittest.html).
