# 9. Standard library tools

Previous: [Modules and packages](../modules/README.md) · Next: [Testing and style](../testing/README.md)

**Goal:** reach for a built-in tool before inventing a replacement.

## Walkthrough

1. Run `python learn.py collections`; follow [collections_demo.py](collections_demo.py). `Counter` counts hashable values, `defaultdict` creates missing values on `[]` access, and `namedtuple` gives tuple fields names.
2. Run `python learn.py dates`; follow [dates_times.py](dates_times.py). Use `date` for a calendar day, `datetime` for date and time, and `timedelta` for a duration. The fixed example dates make revision repeatable.
3. Run `python learn.py paths`; follow [paths_os.py](paths_os.py). `pathlib` provides path objects, `os` exposes process/OS operations, and `shutil` supplies file utilities. The example's copy/move/delete operations stay inside a temporary directory.
4. Run `python learn.py utilities`; read [utilities.py](utilities.py). Explore local random generators, JSON serialization, regular expressions, iterator helpers, and approximate float comparison.

## Tricky cases

- `Counter()["absent"]` returns 0 without inserting. `defaultdict(list)["absent"]` inserts an empty list. `defaultdict.get()` does not invoke its factory.
- `timedelta.seconds` excludes whole days. Use `.total_seconds()` for the duration in seconds.
- A naive datetime has no timezone interpretation attached. Ordering it against an aware datetime raises `TypeError`. A fixed offset does not model regional daylight-saving rules.
- `Path.cwd()` depends on where the program was started. `Path(__file__)` refers to the source module. A path object does not imply that the path exists.
- `rmdir()` removes an empty directory; `unlink()` removes a file. Both can fail. Learn with temporary data.
- `shuffle()` mutates a list and returns `None`. Seeded output is useful for local experiments, but do not promise identical results for every random API across Python releases.
- JSON object keys are strings. A tuple round-trips as a list; a set is not directly serializable. `json.loads()` parses data; it does not execute Python code.
- `re.search()` finds a match anywhere; `re.fullmatch()` checks the whole input. A raw string such as `r"\d+"` makes regex backslashes easier to read.

## Self-check

1. Does `groups.get("new")` add a key to `defaultdict(list)`? Does `groups["new"]`?
2. What are `.seconds` and `.total_seconds()` for `timedelta(days=2, seconds=5)`?

Then try [exercise 9](../../docs/exercises.md#9-word-counts). [Answers](../../docs/solutions.md#chapter-self-checks).
