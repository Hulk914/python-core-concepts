# Counter, defaultdict, namedtuple and deque
Section: Standard-library toolbox

Specialized containers make common intentions explicit. `Counter` counts hashable values. `defaultdict` supplies a missing value through a factory. `namedtuple` gives names to fixed tuple positions. `deque` supports efficient appends and pops at both ends and is a better queue than repeatedly removing a list's first element.

```python verify
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

Run: `python learn.py collections`. Reference: [[R19]].

<!-- page -->
# Dates, durations and time zones
Section: Standard-library toolbox

`date` represents a calendar date; `time` a time of day; `datetime` combines them; `timedelta` represents a duration. Calendar validity is checked by constructors and parsers. Fixed examples make the repo's date lesson repeatable regardless of the day you run it.

```python verify
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

Run: `python learn.py dates`. References: [[R20]], [[R21]].

<!-- page -->
# JSON and data-boundary validation
Section: Standard-library toolbox

JSON is a data interchange format, not a snapshot of arbitrary Python objects. `dumps` encodes to text and `loads` decodes text. `dump` and `load` work with file-like objects. JSON booleans are `true` and `false`; the decoded Python values are `True` and `False`.

```python verify
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

Run: `python learn.py utilities`. References: [[R18]], [[R44]].

<!-- page -->
# Regular expressions and precise text rules
Section: Standard-library toolbox

A regular expression describes a text pattern. Use a plain string operation when it states the requirement more directly. `.startswith()`, `.split()` and membership often express a simple rule more clearly than a pattern. Use regex when the shape is genuinely variable.

```python verify
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

References: [[R22]].

<!-- page -->
# Randomness, paths and small useful tools
Section: Standard-library toolbox

`random` is for simulation and ordinary randomized choices. A local `Random(seed)` object avoids changing global random state. `secrets` is the appropriate standard-library choice for unpredictable tokens and other security-sensitive random values.

```python verify
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

Run: `python learn.py paths` and `python learn.py utilities`. References: [[R17]], [[R23]], [[R24]].

<!-- page -->
# Tests that distinguish correct behavior
Section: Testing and debugging

A useful test can fail for a plausible wrong implementation. A single lowercase word does not distinguish `.capitalize()` from `.title()`; a multiword input does. The repo's text function explicitly rejects non-text input and follows `str.capitalize()`, which capitalizes the first character and lowercases the rest.

{{code:lessons/testing/text_tools.py:capitalize_text}}

```python verify
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

Run: `python -m unittest tests.test_text_tools -v`. Reference: [[R25]].

<!-- page -->
# Isolation, failure injection and integration
Section: Testing and debugging

Tests should be repeatable and independent of personal files, current dates and previous test order. The tracker tests use `TemporaryDirectory` and cleanup registration. CLI tests capture standard output and standard error, pass arguments directly and assert return codes.

```python verify
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

Source: `tests/test_task_tracker.py`, `tests/test_runner.py`. References: [[R25]], [[R26]].

<!-- page -->
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

References: [[R09]], [[R25]], [[R37]].

<!-- page -->
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

Source: `projects/task_tracker/README.md`. References: [[R29]], [[R18]].

<!-- page -->
# Task tracker: model operations and identity
Section: Capstone implementation

The domain model represents a task with an integer ID, title and completion flag. A task's ID is distinct from its position in a list. Removing or reordering tasks should not redefine the identities of the remaining tasks.

{{code:projects/task_tracker/model.py:add_task}}

{{code:projects/task_tracker/model.py:complete_task}}

```python verify
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

Reference: [[R14]].

<!-- page -->
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

```python verify
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

Source: `projects/task_tracker/storage.py:load_tasks`. Reference: [[R18]].

<!-- page -->
# Task tracker: replacement and its limits
Section: Capstone implementation

Saving directly into the destination can leave a truncated document if writing fails midway. The tracker prepares JSON, writes a neighboring staging file and replaces the destination after the write finishes. Cleanup removes leftover staging on ordinary exit paths.

{{code:projects/task_tracker/storage.py:save_tasks}}

## What this design provides

The old destination is not intentionally truncated during staging. If replacement raises in the tested case, the previous data remains and staging is cleaned. Keeping staging beside the destination avoids the usual cross-filesystem rename problem. Encoding is explicit, and non-ASCII titles remain readable in JSON.

## What requires a stronger design

The fixed `.tmp` name lets simultaneous writers interfere. Even unique staging names would not prevent a lost update: two processes can read the same old list and each replace it with a different new list. Replacement does not make the entire read/modify/write sequence transactional.

Atomic visibility also differs from crash durability. Strong power-loss guarantees can require flushing data and directory metadata with platform-specific care. Cleanup itself can fail and potentially mask an earlier error. For this learning application, the documented scope is one process at a time; concurrent use calls for a deliberate transaction or locking design.

Source: `tests/test_task_tracker.py` verifies failed replacement and round-trip behavior. References: [[R17]], [[R33]].

<!-- page -->
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

References: [[R25]], [[R29]], [[R33]].

<!-- page -->
# CPython memory, references and measurement
Section: Deeper Python extensions

Extension beyond the repo: CPython commonly uses reference counting together with cyclic garbage collection. Losing a binding through `del name` removes that reference; it does not command every Python implementation to destroy the object at that instant. Other references or cycles may keep objects alive.

An unreachable cycle can need the cyclic collector even after external references disappear. A weak reference can observe an object without owning its lifetime, but only supported objects allow weak references. Resource release should still use a context manager rather than relying on collection timing.

## Memory size is a graph question

`sys.getsizeof(container)` normally reports the container's own allocation, not the total recursively retained graph. Shared subobjects make naive summing inaccurate: you can count the same object twice. Generator frames and closures can retain references long after the creating function returns.

```python verify
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

References: [[R06]], [[R36]].

<!-- page -->
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

References: [[R30]], [[R31]], [[R32]], [[R39]], [[R43]].

<!-- page -->
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

References: [[R34]], [[R35]], [[R36]], [[R37]].
