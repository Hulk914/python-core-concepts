# Classes, instances and bound methods
Section: Objects and protocols

A class defines a type and groups related behavior. An instance holds particular state. Calling a normal class creates an instance through `__new__` and initializes it through `__init__`. `__init__` initializes an already created object; it must return `None`.

```python verify
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

Run: `python learn.py classes`. References: [[R10]], [[R06]].

<!-- page -->
# Class state, shadowing and method kinds
Section: Objects and protocols

A class attribute is found through attribute lookup when an instance has not supplied its own value. Assigning `instance.attribute` usually creates or updates instance state; it does not generally rewrite the class attribute. Descriptors such as properties can customize this behavior.

```python verify
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

```python verify
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

References: [[R07]], [[R10]], [[R16]].

<!-- page -->
# Special methods and Python protocols
Section: Objects and protocols

Special methods let objects participate in language operations. `__str__` serves a readable display; `__repr__` serves debugging and should be unambiguous when practical. `__len__` supports `len()`. A meaningful protocol is better than adding a special method only because the syntax is available.

```python verify
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

References: [[R06]], [[R02]].

<!-- page -->
# Inheritance, super and composition
Section: Objects and protocols

Inheritance models a substitutable “is a” relationship. Composition stores a collaborator to model “has a.” The repository's `Cat` specializes `Animal`; its `Owner` holds a pet. Both techniques reuse behavior, but they create different dependencies and extension points.

{{code:lessons/oop/inheritance.py:Cat}}

```python verify
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

Run: `python learn.py inheritance`. References: [[R10]], [[R15]].

<!-- page -->
# Dataclasses and explicit invariants
Section: Objects and protocols

A dataclass generates routine methods from declared fields, usually including initialization, representation and equality. It saves repetitive code; it is not an input-validation engine. Equality compares field values using those fields' own equality behavior.

{{code:projects/task_tracker/model.py:Task}}

```python verify
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

References: [[R14]], [[R15]].

<!-- page -->
# Properties, descriptors and encapsulation
Section: Objects and protocols

Extension beyond the repo: a property provides attribute syntax with controlled access. It is useful when a value needs validation or computation while callers use an ordinary attribute interface. A leading underscore marks an implementation detail by convention; it does not prevent access.

```python verify
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

References: [[R16]], [[R06]].

<!-- page -->
# Abstract interfaces and structural protocols
Section: Objects and protocols

Extension beyond the repo: interfaces let code depend on a required behavior instead of a concrete implementation. An abstract base class can define a nominal family and prevent construction until required methods are implemented. A typing `Protocol` describes structural compatibility for static analysis.

```python verify
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

References: [[R15]], [[R10]].

<!-- page -->
# Iterables, iterators and exhaustion
Section: Iterators and decorators

An iterable can supply an iterator through `iter()`. An iterator tracks progress, supplies the next value through `next()` and raises `StopIteration` when exhausted. An iterator's `iter()` returns itself. A list is reusable; a particular iterator over that list is consumed as it advances.

```python verify
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

```python verify
squares = (number * number for number in range(4))
assert next(squares) == 0
assert sum(squares) == 14
assert sum(squares) == 0
```

The second sum is zero because there are no remaining values, not because the original mathematical series changed. This is a common bug in logging, validation and test code that consumes an iterator before the real computation.

Checkpoint: what happens if you call `list(stream)` for debugging before the processing loop? For an open file it advances to the end. Reopen it, rewind when supported or inspect without consuming the whole pipeline.

References: [[R06]], [[R07]], [[R12]].

<!-- page -->
# Implement an iterator protocol
Section: Iterators and decorators

Extension beyond the repo: implementing an iterator once makes the protocol concrete. An iterator's `__iter__` returns itself; `__next__` returns the next item or raises `StopIteration`. A reusable iterable should instead supply a fresh iterator when independent traversals are requested.

```python verify
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

References: [[R06]], [[R07]].

<!-- page -->
# Generator functions and suspended state
Section: Iterators and decorators

A function containing `yield` is a generator function. Calling it returns a generator object; execution of its body begins when a value is requested. At each yield, local state is suspended and later resumed. Reaching the end exhausts the generator.

{{code:lessons/advanced/generators.py:fibonacci}}

```python verify
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

Run: `python learn.py generators`. References: [[R06]], [[R12]].

<!-- page -->
# Streaming pipelines and iterator tools
Section: Iterators and decorators

Compose small stages to process data incrementally: read an item, filter it, transform it and reduce it. Laziness can lower peak memory and provide an early result. It also moves failures later and makes repeated traversal less automatic.

```python verify
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

References: [[R12]], [[R06]].

<!-- page -->
# Decorators: replacing a callable safely
Section: Iterators and decorators

A decorator receives a callable and returns its replacement. `@announce` above a definition means `greet = announce(greet)` after the function is created. Decoration occurs when the definition executes; the wrapper's body runs when the replacement is called.

{{code:lessons/advanced/decorators.py:announce}}

```python verify
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

Run: `python learn.py decorators`. References: [[R11]], [[R03]].

<!-- page -->
# Configurable decorators, caching and effects
Section: Iterators and decorators

A parameterized decorator has three layers: configuration, decoration and invocation. Validate configuration once, capture it in a closure and keep call forwarding explicit. The repository's repeat exercise uses this pattern.

```python verify
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

References: [[R11]], [[R12]].

<!-- page -->
# Modules, packages and import behavior
Section: Modules and environments

A module is a namespace containing Python definitions and statements. A regular package groups modules and normally contains `__init__.py`; namespace packages are an intentional exception. An import finds a module, initializes it when necessary and binds a name in the importing namespace.

```python verify
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

Run: `python learn.py imports`. Reference: [[R27]].

<!-- page -->
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

References: [[R27]], [[R29]].

<!-- page -->
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

References: [[R28]], [[R38]], [[R45]].
