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

Source: `docs/exercises.md:1–4`. References: [[R02]], [[R04]], [[R08]].

<!-- page -->
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

Source: `docs/exercises.md:5–7`. References: [[R13]], [[R06]], [[R11]].

<!-- page -->
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

Source: `docs/exercises.md:8–10`. References: [[R12]], [[R19]], [[R25]].

<!-- page -->
# Workbook answers · exercises 1–4
Section: Practice workbook

Compare the ownership and ordering rules, not just the visual similarity of your implementation. These are complete definitions adapted from `docs/solutions.md`.

```python verify
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

References: [[R04]], [[R08]].

<!-- page -->
# Workbook answers · exercises 5–7
Section: Practice workbook

```python verify
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

References: [[R11]], [[R13]], [[R06]].

<!-- page -->
# Workbook answers · exercises 8–10
Section: Practice workbook

```python verify
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

```python verify
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

References: [[R12]], [[R19]], [[R25]].

<!-- page -->
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

<!-- page -->
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

References: [[R02]], [[R05]], [[R08]], [[R09]], [[R30]].

<!-- page -->
# Reference library · language and data
Section: Official reference library

These primary sources were checked while preparing this edition. Links are pinned to Python 3.14 to keep one documentation baseline; check version notes before using a newer API in a Python 3.10 project. The guide's explanations and examples are original teaching material built around the supplied repository; links provide deeper specifications and API details.

- [[R01]] — First steps with numeric and text values.
- [[R02]] — Truth testing, containers, strings and standard operations.
- [[R03]] — Branches, loops, signatures, defaults and annotations.
- [[R04]] — Lists, tuples, dictionaries and comprehensions.
- [[R05]] — Assignment, shallow copying and deep copying.
- [[R06]] — Identity, protocols, special methods and object behavior.
- [[R07]] — Builtins such as iter, next, sorted, property and open.
- [[R08]] — Binding, scope, free variables and name lookup.
- [[R09]] — Handling, raising, chaining and cleanup.
- [[R10]] — Classes, namespaces, inheritance and iteration.
- [[R11]] — Wrappers, caches, partial application and metadata.
- [[R12]] — Composing and consuming iterators.
- [[R13]] — Context-manager adapters and ExitStack.
- [[R14]] — Generated record methods and field options.
- [[R15]] — Hints, unions, generics and structural interfaces.
- [[R16]] — Properties, bound methods and attribute lookup.
- [[R17]] — Path objects and concrete filesystem operations.
- [[R18]] — Serialization limits, hooks and decoder behavior.
- [[R19]] — Counters, queues, defaults and named records.
- [[R20]] — Calendar values, durations and aware datetimes.
- [[R21]] — Regional IANA time-zone rules and data availability.
- [[R22]] — Pattern syntax, match objects and text-search APIs.
- [[R23]] — Pseudorandom simulation tools and reproducibility.

## How to read a reference page

Start with the exact operation and its return type. Check mutability, exceptions, accepted inputs and version notes. Then build a five-line experiment. A reference is most useful when you bring a concrete question, such as whether a missing lookup inserts a value or when an iterator raises an error.

<!-- page -->
# Reference library · engineering and tooling
Section: Official reference library

- [[R24]] — Unpredictable tokens and security-sensitive randomness.
- [[R25]] — Test cases, assertions, discovery and fixtures.
- [[R26]] — Patch a dependency in the namespace that uses it.
- [[R27]] — Packages, imports, module search and program execution.
- [[R28]] — Isolated environments and package installation.
- [[R29]] — Argument parsing, help and subcommands.
- [[R30]] — Free-threaded builds, compatibility and shared state.
- [[R31]] — Thread and process pools, futures and shutdown.
- [[R32]] — Coroutines, event loops and asynchronous I/O.
- [[R33]] — Embedded databases and explicit transaction behavior.
- [[R34]] — Profilers and interpreting cumulative time.
- [[R35]] — Repeated microbenchmarks and measurement caveats.
- [[R36]] — Python allocation snapshots and comparisons.
- [[R37]] — Loggers, handlers, configuration and severity.
- [[R38]] — Naming, layout and readable code conventions.
- [[R39]] — Python 3.14 supported free-threading status.
- [[R40]] — Representation error and approximate arithmetic.
- [[R41]] — Decimal contexts, arithmetic and rounding.
- [[R42]] — Temporary files and directory lifetime.
- [[R43]] — Threads, synchronization primitives and locks.
- [[R44]] — Python object serialization and untrusted-data risks.
- [[R45]] — Build metadata and distributing a Python package.
- [[R46]] — Structural pattern matching in Python 3.10.

## Repository reading order

Start with `README.md`, use each `lessons/*/README.md` beside the runnable module, then read `docs/exercises.md` before `docs/solutions.md`. For implementation review, follow `projects/task_tracker/model.py`, `storage.py`, `cli.py` and `tests/test_task_tracker.py`. The quick reference is an index for recall, not a substitute for tracing the examples.

## Keeping the PDF current

The source chapters live in `docs/python_guide/`; the builder extracts marked functions from the maintained source files and records source hashes in a build manifest. After a contract changes, update the relevant prose and expected outputs, run repository tests and rebuild. Extracting current code prevents one kind of drift; it cannot automatically correct an explanation that describes an obsolete rule.

The final section is the mock interview workbook. Its scenarios progress from language behavior to system boundaries, with answers, follow-up prompts and evaluation cues.
