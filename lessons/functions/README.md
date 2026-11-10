# 4. Functions, interfaces, and scope

Previous: [Control flow](../control_flow/README.md) · Next: [Files and exceptions](../files_exceptions/README.md)

**Goal:** write reusable functions with predictable inputs, outputs, and state.

## Walkthrough

1. Run `python learn.py arguments`; follow [arguments.py](arguments.py). A function that returns a value can be composed and tested; a function that only prints returns `None` unless it explicitly returns something else.
2. Call `describe_person("Ada", language="Python")`. `/` ends positional-only parameters; a bare `*` starts keyword-only parameters. `*args` collects positional values into a tuple; `**kwargs` collects keyword values into a dictionary.
3. Compare collecting with unpacking: in a call, `f(*values, **options)` expands containers into arguments.
4. Run `python learn.py functional` and read [functional_tools.py](functional_tools.py). `map` transforms each item; `filter` keeps items whose predicate is truthy. They return iterators.
5. Run `python learn.py scope` and read [scope.py](scope.py). Trace LEGB lookup, then compare two independently created counters.

## Tricky cases

```python
def collect(value, items=[]):  # deliberate pitfall; do not use this default
    items.append(value)
    return items

collect(1)   # [1]
collect(2)   # [1, 2]: the same default list is reused
```

Use `None` and create a new list inside the function. The default is evaluated when the `def` statement executes, not on each call. An explicitly passed list can still be mutated.

- Rebinding a parameter to a new list does not rebind the caller's name. Mutating the original list is visible to the caller.
- Assigning to a name makes it local unless declared `global` or `nonlocal`. Reading it before that local assignment can cause `UnboundLocalError`.
- Closures capture access to enclosing names; default argument values can capture the current value in a loop.
- `any([])` is `False`; `all([])` is `True` because no element violates the condition.
- A type annotation documents intent; it does not automatically validate input at runtime.

## Self-check

1. Why do `[lambda: i for i in range(3)]` all return 2 when called after the loop? How do you capture 0, 1, and 2 instead?
2. What happens if you call `describe_person(name="Ada")`? Why?

Then try [exercise 4](../../docs/exercises.md#4-running-counter). [Answers](../../docs/solutions.md#chapter-self-checks).
