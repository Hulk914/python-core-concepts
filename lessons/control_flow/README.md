# 3. Control flow and comprehensions

Previous: [Data structures](../data_structures/README.md) · Next: [Functions](../functions/README.md)

**Goal:** write readable conditions and loops, then recognize when a comprehension is simpler.

## Walkthrough

1. Run `python learn.py loops` and read [branching_loops.py](branching_loops.py). Python uses indentation for blocks. `elif` branches are tested only until one branch matches.
2. Follow `range`, `enumerate`, tuple unpacking, and `zip`. Change the lengths of the two zipped lists.
3. Remove the even number from `candidates`. The `for` loop's `else` now runs because the loop ends without `break`; an empty iterable also reaches `else`.
4. Run `python learn.py comprehensions` and read [comprehensions.py](comprehensions.py). Rewrite one example as a loop before making it compact again.
5. Compare the trailing filter with the conditional expression at the front:

```python
[n for n in range(4) if n % 2 == 0]                  # [0, 2]
["even" if n % 2 == 0 else "odd" for n in range(4)]   # four labels
```

## Tricky cases

- `range(5)` excludes 5. `range(5, 0)` is empty; descending iteration needs a negative step.
- `break` exits the nearest loop; `continue` skips the rest of one iteration; `pass` does nothing.
- `and` and `or` return operands, not necessarily booleans: `"" or "guest"` is `"guest"`.
- `zip()` silently stops when the shortest input ends. On Python 3.10+, `zip(..., strict=True)` detects unequal lengths.
- Removing items from the list currently being iterated can skip elements. Build a filtered list instead.
- Comprehensions are for constructing results. Prefer a regular loop for several actions or complicated branching.

## Self-check

1. What does `list(range(5, 0, -2))` return?
2. Does a loop's `else` run when the iterable is empty? When the loop executes `break`?

Then try [exercise 3](../../docs/exercises.md#3-even-values-and-their-squares). [Answers](../../docs/solutions.md#chapter-self-checks).
