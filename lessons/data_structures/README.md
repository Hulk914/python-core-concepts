# 2. Data structures and references

Previous: [Values and strings](../basics/README.md) · Next: [Control flow](../control_flow/README.md)

**Goal:** choose a container and explain what changes when two names reference it.

| Type | Main purpose | Mutable? | Key rule |
| --- | --- | --- | --- |
| `list` | Ordered sequence | Yes | Duplicates are allowed |
| `tuple` | Fixed sequence of references | No | Contents can reference mutable objects |
| `dict` | Key/value lookup | Yes | Keys must be hashable; insertion order is preserved |
| `set` | Unique values and set operations | Yes | Values must be hashable; order is not guaranteed |

## Walkthrough

1. Read [sequences.py](sequences.py), then run `python learn.py sequences`.
2. Draw two arrows from names to the same list for `alias = numbers`. Assignment binds a name; it does not copy the object.
3. Compare `.copy()` with `deepcopy()` for the nested list. A shallow copy creates an outer list and shares its elements.
4. Run `python learn.py mappings` and follow [mappings_sets.py](mappings_sets.py). Contrast `profile[key]` with `profile.get(key, default)`.
5. Change the set operands and predict union (`|`), intersection (`&`), and difference (`-`). Sort the result for a repeatable display.

## Tricky cases

```python
rows = [[0]] * 2
rows[0].append(1)
# rows == [[0, 1], [0, 1]]: both elements reference the same inner list
```

- `list.sort()` mutates and returns `None`; `sorted(list)` returns a new list.
- `(10)` is an integer; `(10,)` is a tuple.
- A tuple containing a list is not hashable. Tuple immutability alone does not guarantee hashability.
- `{}` is an empty dictionary. Write `set()` for an empty set.
- `.get()` does not add a missing key; `setdefault()` can add one. Dictionary membership checks keys, not values.
- Avoid adding or removing dictionary keys while iterating over the dictionary; iterate over a snapshot or build a new dictionary.

## Self-check

1. After `a = [1]; b = a; b.append(2)`, what is `a`?
2. Can `([1], 2)` change? Can it be a dictionary key? Explain both answers.

Then try [exercise 2](../../docs/exercises.md#2-unique-values-in-order). [Answers](../../docs/solutions.md#chapter-self-checks).
