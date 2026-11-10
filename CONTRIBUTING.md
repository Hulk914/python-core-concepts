# Contributing

The goal is a small, readable course that a learner can run without installing packages. Contributions can improve explanations, correct examples, add a focused edge case, or extend the task tracker with tests.

## A lesson should have

- A descriptive module docstring with its run command and one experiment to try.
- Short, reusable functions where they make the concept clearer.
- A `main()` demonstration behind an `if __name__ == "__main__"` guard.
- Visible output and short comments explaining surprising results.
- A chapter walkthrough, tricky cases, two self-checks, and matching answers.

Use the standard library and Python 3.10-compatible syntax. Keep imports free of prompts, printing, filesystem writes, or demonstration execution. Use a temporary directory for examples that create or change files. Keep set displays sorted, and use fixed dates when illustrating date arithmetic.

## Check a change

Run these from the root:

```console
python -m unittest discover -s tests -v
python -m compileall -q learn.py lessons projects tests
```

The test suite also runs every registered lesson and imports all course/project modules. Run a changed lesson individually while developing. Add behavior tests for a new contract or a meaningful failure case rather than tests that reproduce the implementation.

If you use Ruff, the optional `pyproject.toml` configuration selects basic syntax, import-use, and undefined-name checks. Run `python -m ruff check .` after installing it in your own development environment. Ruff is not required by the course or the CI workflow.

For a new lesson, update `learn.py`, the course table, the relevant chapter README, and the quick reference. Check local Markdown links after renaming files. Keep original archived notes unchanged; explain corrections in the maintained lessons.

## Pull requests

Describe the learner-facing problem, show the resulting behavior, and state what you ran to verify it. If an example changes its contract, update the exercise, answer, and tests together.

## Useful references

- [Python tutorial](https://docs.python.org/3/tutorial/)
- [Python standard library](https://docs.python.org/3/library/)
- [unittest documentation](https://docs.python.org/3/library/unittest.html)
- [GitHub's Python workflow guide](https://docs.github.com/en/actions/tutorials/build-and-test-code/python), the reference for the CI setup.
- Official action documentation: [checkout](https://github.com/actions/checkout) and [setup-python](https://github.com/actions/setup-python).
