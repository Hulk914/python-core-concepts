# Practice exercises

[Course home](../README.md) · [Solutions](solutions.md#exercise-solutions)

Try each task before opening the solutions. Example results define the contract; include the listed edge cases in your checks. Use the Python REPL, your own practice file, or a local branch.

## 1. Alternating text

Write `alternating_case(text)` so even-indexed characters are lowercase and odd-indexed characters uppercase.

- `"ayush"` → `"aYuSh"`
- `"PYTHON"` → `"pYtHoN"`
- `""` → `""`
- Spaces count as positions; `"a bc"` → `"a bC"`.

Hint: use `enumerate()` and `"".join(...)`. This position rule is based on the original input characters; Unicode case transformations can sometimes change the length of the result.

## 2. Unique values in order

Write `unique_in_order(values)` for hashable values. Preserve the first appearance of each value without changing the input.

- `[3, 1, 3, 2, 1]` → `[3, 1, 2]`
- `[]` → `[]`

Hint: dictionaries preserve insertion order. Why would `list(set(values))` fail the order contract? What happens with unhashable values such as nested lists?

## 3. Even values and their squares

Write `even_squares(values)` returning a list of squares of even integers, preserving order and duplicates.

- `[3, -2, 0, 4, 4]` → `[4, 0, 16, 16]`
- `[1, 3]` → `[]`

Hint: separate the transformation from the filter condition.

## 4. Running counter

Write `make_counter(start=0)` returning a function that increments and returns its own count. Two calls to the factory must produce independent counters.

- `counter = make_counter(10)`; two calls → `11`, `12`
- A new `make_counter()` should begin at `1` on its first increment.

Hint: `nonlocal` lets the inner function rebind enclosing state.

## 5. Load nonempty lines

Write `load_nonempty_lines(path)` to read UTF-8 text, strip leading/trailing whitespace from each line, and return only nonempty lines.

- File contents `"  Python  \n\n Practice\n"` → `["Python", "Practice"]`
- An empty file → `[]`
- A missing file should raise `FileNotFoundError`; do not silently treat it as empty.

Hint: use a context manager and test with `TemporaryDirectory`.

## 6. A small Book class

Create `Book(title, pages)` with `str(book)` returning `"Python Notes (120 pages)"` and `len(book)` returning its page count. Require pages to be an integer greater than or equal to zero; reject booleans as page counts.

- Negative pages → `ValueError`
- Non-integer pages, including `True` → `TypeError`
- Zero pages → valid, but explain `bool(book)`.

Hint: `bool` subclasses `int`. Consider `type(pages) is int` for this strict contract.

## 7. A repeatable decorator

Write `repeat(times)` so `@repeat(3)` invokes the decorated function three times, forwarding its arguments and returning a list of results. Preserve the function's name and docstring. Require a non-negative integer repeat count.

- Decorating `def double(n): return n * 2`, then calling with 4 → `[8, 8, 8]`
- Zero repetitions → `[]`, without calling the wrapped function
- Negative count → `ValueError`; bool or non-integer count → `TypeError`

Hint: this needs three layers: configuration, decoration, and invocation. Let exceptions from the wrapped function propagate.

## 8. Lazy running totals

Write a generator `running_totals(values)` yielding each cumulative sum.

- `[2, -1, 3]` → yields `2`, `1`, `4`
- Empty iterable → no values
- Accept an iterator as well as a list; do not convert it into a list first.

Hint: one accumulator and one `yield` per input item.

## 9. Word counts

Write `word_counts(text)` using `Counter`. Treat words as whitespace-separated tokens and ignore case. Punctuation remains part of a token for this exercise.

- `"Python python code"` → counts `python: 2`, `code: 1`
- `""` → empty counter
- `"code code!"` → two different keys

Hint: `casefold()` is useful for case-insensitive text comparison. Do not add punctuation stripping unless you change and document the contract.

## 10. Test a contract

Write `unittest` cases for `capitalize_text()` that would catch a mistaken implementation using `.title()`. Cover empty input and a rejected non-string value too.

Hint: one lowercase word passes under both implementations. A multiword string distinguishes them.

## Final project extensions

After completing the [task tracker](../projects/task_tracker/README.md), choose one feature:

- Add `list --pending` and test mixed and empty task lists.
- Add `rename <id> <title>` with the same title validation as `add`.
- Add a due-date field using ISO dates, documenting how old JSON files are migrated.

Implement one feature completely: CLI behavior, validation, tests, and documentation. Keep the current file format working or explicitly design a migration.
