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

<!-- page -->
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

References: [[R27]], [[R28]].

<!-- page -->
# Names, objects and the execution model
Section: Values and text

A name is a binding to an object. Objects have identity, type and value. Assignment changes a binding; it does not automatically copy the object. Dynamic typing means a name can later refer to an object of a different type. The object still has a type, and that type determines which operations it supports.

```python verify
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

Run: `python learn.py numbers`. References: [[R06]], [[R08]].

<!-- page -->
# Numeric types, operators and conversion
Section: Values and text

Use `int` for whole numbers, `float` for approximate binary fractions and `complex` when real and imaginary parts are needed. Python integers have arbitrary precision within available memory; they are not fixed 32-bit machine integers. `bool` has the values `True` and `False` and is a subclass of `int`, which matters at validation boundaries.

```python verify
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

Source: `lessons/basics/numbers.py`. References: [[R01]], [[R07]].

<!-- page -->
# Floating point and deliberate comparisons
Section: Values and text

Many decimal fractions have no finite binary representation. A float stores a nearby representable number, so a sequence of operations can accumulate small errors. Formatting makes a result look tidy; it does not change the stored number or make an exact equality comparison reliable.

```python verify
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

Run: `python learn.py numbers` and `python learn.py utilities`. References: [[R40]], [[R41]].

<!-- page -->
# Operators, precedence and bitwise work
Section: Values and text

An operator's precedence decides grouping when parentheses are absent. It is not the same as evaluation order. Function arguments and most ordinary operands evaluate left to right, while `and`, `or` and conditional expressions can skip work. Use parentheses when a reader would otherwise need to look up a precedence table.

```python verify
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

```python verify
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

References: [[R02]], [[R06]].

<!-- page -->
# Truthiness, comparisons and short circuiting
Section: Values and text

Conditions evaluate an object's truth value. Common false values are `None`, `False`, numeric zero and empty containers. A nonempty string such as `"False"` or `"0"` is true. Python does not interpret the word inside a string as a boolean declaration.

```python verify
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

Source: `lessons/control_flow/branching_loops.py`. References: [[R02]], [[R03]].

<!-- page -->
# Strings: indexing, slicing and immutability
Section: Values and text

A string is an immutable sequence of Unicode code points. Indexing starts at zero; negative indices count from the end. A slice `text[start:stop:step]` includes the start and excludes the stop. Missing bounds use defaults that depend on the direction of the step.

```python verify
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

Source: `lessons/basics/strings.py`. References: [[R01]], [[R02]].

<!-- page -->
# Text pipelines and formatting
Section: Values and text

Text processing is easier to reason about as a pipeline: clean the boundaries, split into tokens, transform each token and combine the results. Decide which whitespace and punctuation are meaningful before writing the operations.

```python verify
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

{{code:lessons/basics/strings.py:alternating_case}}

`enumerate()` supplies each original position and character. The conditional expression chooses the transformation; `join()` consumes the generated fragments. Empty input produces no fragments, so the result is `''`. Spaces still count as input positions. Some Unicode case transformations expand to several code points, so output length is not guaranteed to match input length.

## Formatting is a presentation decision

An f-string evaluates expressions inside braces. `:.2f` displays two decimal places; `!r` requests a debugging representation. Keep untrusted text as data rather than evaluating it as a Python expression. Prefer parameterized database operations over using formatted strings to construct SQL.

Try `alternating_case("a bc")`: the result is `'a bC'`. Explain why the space changes which letter becomes uppercase.

References: [[R02]], [[R07]].

<!-- page -->
# Text, bytes and encoding boundaries
Section: Values and text

`str` represents Unicode text. `bytes` represents an immutable sequence of byte values from 0 to 255. `bytearray` is a mutable byte sequence. Encode text to bytes when crossing a file, network or external-format boundary; decode bytes to text using the format's declared encoding. These are explicit transformations, not interchangeable representations.

```python verify
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

References: [[R02]], [[R07]].

<!-- page -->
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

```python verify
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

References: [[R02]], [[R04]], [[R06]].

<!-- page -->
# Lists and tuples in practice
Section: Containers and references

Lists store references in sequence. `append(x)` adds one object; `extend(iterable)` adds each produced object. `pop()` removes and returns an item, while `remove(value)` deletes the first equal value and raises `ValueError` if absent. Methods that only mutate the list, such as `sort()`, return `None`.

```python verify
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

```python verify
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

Run: `python learn.py sequences`. References: [[R04]], [[R02]].

<!-- page -->
# Aliasing, shallow copies and deep copies
Section: Containers and references

Assignment creates another reference. A shallow copy creates a new outer container and reuses references to its elements. A deep copy recursively copies supported contents and uses a memo to handle cycles and preserve repeated-reference structure within the copy. These are different contracts, not progressively “better” operations.

```python verify
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

```python verify
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

Run: `python learn.py sequences`. Reference: [[R05]].

<!-- page -->
# Dictionaries, sets and hashability
Section: Containers and references

A dictionary maps unique hashable keys to values. `mapping[key]` raises `KeyError` when absent; `.get(key, default)` returns the default without inserting it. `.setdefault()` may insert, while `defaultdict` adds factory behavior for missing bracket lookups. Choose whether a missing key is normal or an error.

```python verify
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

```python verify
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

Run: `python learn.py mappings`. References: [[R02]], [[R04]].

<!-- page -->
# Branches, loops and loop else
Section: Control flow

Indentation defines a block. An `if`/`elif`/`else` chain executes the first matching branch. A `for` loop requests items from an iterable; a `while` loop repeats while a condition is true. A useful loop has a clear invariant and a clear reason it will terminate.

```python verify
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

Run: `python learn.py loops`. References: [[R03]], [[R46]].

<!-- page -->
# Iteration helpers and comprehensions
Section: Control flow

Use `enumerate()` when you need an item and its position. Use `zip()` to pair inputs. Use unpacking to reveal each record's structure. These tools avoid manually synchronizing indexes and make a loop's purpose easier to see.

```python verify
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

```python verify
rows = [[1, 2], [3, 4]]
assert [value for row in rows for value in row] == [1, 2, 3, 4]
assert ["even" if n % 2 == 0 else "odd" for n in range(3)] == [
    "even", "odd", "even"
]
assert {n: n*n for n in range(3)} == {0: 0, 1: 1, 2: 4}
```

Nested comprehension clauses follow the same order as nested ordinary loops. Rewrite one as loops before compressing it. Prefer a regular loop for several actions, complex branching or side effects. A comprehension builds a result eagerly; a generator expression defers production and is consumed once.

Checkpoint: rewrite `extract_even()` from `lessons/control_flow/comprehensions.py` as a loop. Verify it preserves duplicates, input order and the original input list.

References: [[R03]], [[R04]], [[R07]].

<!-- page -->
# Pattern matching and readable dispatch
Section: Control flow

Extension beyond the repo: Python 3.10's `match` statement selects a branch from the shape and contents of a subject. It is useful for structured alternatives such as parsed commands. It is not required when a short `if` chain already states the rule clearly.

```python verify
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

References: [[R03]], [[R46]].

<!-- page -->
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

```python verify
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

References: [[R02]], [[R34]], [[R35]].
