# 1. Values and strings

[Course home](../../README.md) · Next: [Data structures](../data_structures/README.md)

**Goal:** distinguish a value, its type, and the name referencing it; manipulate text without guessing at slice boundaries.

## Walkthrough

1. Open [numbers.py](numbers.py). Predict the output beside each comment, then run `python learn.py numbers`.
2. Compare `/` (true division), `//` (floor division), `%` (remainder), and `**` (power). Try negative operands: `-7 // 2` is `-4` because flooring moves toward negative infinity.
3. Follow the text-to-integer example. `input()` returns a string even when someone types digits; `int()` can raise `ValueError` when the text is not an integer.
4. Open [strings.py](strings.py), then run `python learn.py strings`. Indexing returns one character; slicing returns a new string. In `text[start:stop:step]`, stop is excluded.
5. Change `alternating_case()` to start with uppercase. Keep the original function until you can explain its empty-input behavior.

```python
word = "Python"
word[1:4]          # 'yth'
word[::-1]         # 'nohtyP'
f"{12.5:.2f}"      # '12.50'
```

## Tricky cases

- `bool("False")` is `True`: any nonempty string is truthy.
- `==` compares values; `is` checks whether two references identify the same object. Use `is None` for the missing-value sentinel. Never rely on string or integer caching for equality.
- `word[999]` raises `IndexError`, while `word[999:]` is `''`.
- Strings are immutable. `word.upper()` returns a value; it does not change `word`.
- `0.1 + 0.2 == 0.3` is false because of binary floating-point representation. Formatting changes the display; `math.isclose()` compares approximately.

## Self-check

1. What are `bool("0")`, `int(-3.9)`, and `"python"[-2:]`?
2. Why does `10 + "2"` fail? What would `10 + int("2")` produce?

Then try [exercise 1](../../docs/exercises.md#1-alternating-text). [Answers](../../docs/solutions.md#chapter-self-checks).
