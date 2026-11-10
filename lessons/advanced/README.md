# 7. Decorators and generators

Previous: [Objects](../oop/README.md) · Next: [Modules and packages](../modules/README.md)

**Goal:** understand function wrapping and iteration without hidden execution assumptions.

## Walkthrough

1. Run `python learn.py decorators`; read [decorators.py](decorators.py). `@announce` replaces the decorated name with `announce(original_function)`.
2. Trace arguments into `wrapper`, the call to the original function, and the returned greeting. Without `return result`, the caller would receive `None`.
3. Inspect `greet.__name__`, `greet.__doc__`, and `greet.__wrapped__`. `functools.wraps` preserves useful metadata and exposes the wrapped function.
4. Run `python learn.py generators`; read [generators.py](generators.py). Calling a generator function creates an iterator; its body begins when iteration requests a value.
5. Trace the Fibonacci values through `next()`, `list()`, and a second `list()`. Create a new generator to start again.

## Tricky cases

- Decoration executes when the definition is evaluated. The wrapper's body runs when the decorated callable is called. Some decorators can therefore have import-time effects; this one only creates a wrapper on import.
- `*args, **kwargs` forwarding keeps the wrapper usable with many signatures. It does not itself validate arguments.
- An exception from the wrapped function propagates and skips code after the call. Use `finally` for actions required on both outcomes.
- A generator is one-shot. `next(exhausted)` raises `StopIteration`; `next(exhausted, default)` returns the default.
- A lazy generator can reduce peak memory, but `list(generator)` materializes all results. Laziness does not promise faster execution.
- Even validation before the first `yield` is delayed until iteration begins.

## Self-check

1. What do `list(g)` and then `list(g)` produce for `g = (n*n for n in range(3))`?
2. Does `fibonacci(-1)` raise immediately, or does `next(fibonacci(-1))` raise? Why?

Then try [exercise 7](../../docs/exercises.md#7-a-repeatable-decorator) and [exercise 8](../../docs/exercises.md#8-lazy-running-totals). [Answers](../../docs/solutions.md#chapter-self-checks).
