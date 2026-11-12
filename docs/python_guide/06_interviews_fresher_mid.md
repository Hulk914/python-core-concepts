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

<!-- page -->
# Fresher · objects, equality and arithmetic
Section: Mock interview · fresher

## F01 · What does assignment copy? How do == and is differ?

**Answer:** ordinary assignment binds a name to an object; it does not copy the object. `==` compares values through equality behavior, while `is` checks identity. Two equal lists can be distinct objects. Two names referring to one list observe the same mutation. Rebinding one name later does not redirect the other name.

```python verify
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

Repo: `lessons/basics/numbers.py`. References: [[R06]], [[R01]], [[R40]].

<!-- page -->
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

Repo: `strings.py`, `sequences.py`, `mappings_sets.py`. References: [[R02]], [[R04]], [[R19]].

<!-- page -->
# Fresher · copying and control flow
Section: Mock interview · fresher

## F05 · Why can a copied list still change the original?

**Answer:** a shallow copy allocates a new outer list and reuses references to its elements. Appending to the copy's outer list is independent; mutating an inner shared list affects both views. A deep copy recursively copies supported contents and tracks already visited objects. Use it when an independent object graph is actually required, not as an automatic fix for unclear ownership.

```python verify
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

Repo: `sequences.py`, `branching_loops.py`. References: [[R05]], [[R03]].

<!-- page -->
# Fresher · functions and defaults
Section: Mock interview · fresher

## F07 · What is the difference between print and return?

**Answer:** `print()` writes a representation to a stream for a reader or another process. `return` supplies a value to the caller and ends the function's current execution. A function with no explicit returned value returns `None`. Printing a total does not let the caller multiply that total unless the function also returns it.

The repo's `add(first, second=5)` returns a reusable result. `sum_args(*numbers)` collects extra positional values in a tuple and returns their sum, including zero for no arguments. `**details` collects extra keyword values in a dictionary. At a call, `*` and `**` expand values rather than collect them.

**Follow-up answered:** Python binds parameter names to supplied objects. If a function appends to a supplied list, the caller sees it. If it then rebinds its parameter to another list, the caller's binding is unchanged. A strong answer avoids the inaccurate split between “mutable by reference” and “immutable by value.”

## F08 · Why is a list default dangerous? Show a correction.

**Answer:** default expressions are evaluated when `def` executes. An omitted list argument can therefore reuse one list across many calls. If that list is mutated, later calls inherit earlier results. Use a sentinel such as `None` and create a new list inside the call when omission means “fresh state.”

```python verify
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

Repo: `lessons/functions/arguments.py`. References: [[R03]], [[R08]].

<!-- page -->
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

Repo: `reading_writing.py`, `handling_errors.py`. References: [[R07]], [[R09]], [[R13]].

<!-- page -->
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

Repo: `classes.py`, `imports.py`, `tests/test_text_tools.py`. References: [[R10]], [[R27]], [[R25]].

<!-- page -->
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

Repo: `arguments.py`, `scope.py`. References: [[R03]], [[R08]].

<!-- page -->
# Mid-level · laziness and decorators
Section: Mock interview · mid-level

## M03 · When does a generator validate, and how would you change it?

**Answer:** a generator function's body begins during iteration, not when the generator object is constructed. The repo's `fibonacci(-1)` therefore returns an object; its first `next()` raises `ValueError`. Once exhausted, that same object cannot be rewound by calling `iter()` or `list()` again.

To reject invalid counts immediately, use a normal outer function that validates and returns an inner generator. The outer function itself must not contain a yield. Keep the validation policy unchanged and test the time at which the error appears, not just its type.

```python verify
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

Repo: `generators.py`, `decorators.py`. References: [[R06]], [[R11]].

<!-- page -->
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

Repo: `mappings_sets.py`, `model.py`, `storage.py`. References: [[R06]], [[R14]], [[R18]].

<!-- page -->
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

Repo: `handling_errors.py`, `imports.py`, `tests/test_runner.py`. References: [[R09]], [[R27]].

<!-- page -->
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

Repo: `tests/test_task_tracker.py`, `storage.py`. References: [[R25]], [[R26]], [[R18]].

<!-- page -->
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

Repo: `dates_times.py`, `reading_writing.py`, `generators.py`. References: [[R20]], [[R21]], [[R12]].
