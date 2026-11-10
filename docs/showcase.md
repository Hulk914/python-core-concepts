# Sharing this project

[Course home](../README.md)

## Suggested repository description

> An example-first core Python course and refresher: 10 chapters, 21 runnable lessons, tricky questions, exercises, and a tested CLI task tracker. Standard library only.

Suggested repository name: `core-python-field-guide`.

Suggested GitHub topics: `python`, `python3`, `python-tutorial`, `python-basics`, `learning-python`, `standard-library`, `unittest`, `cli`.

## A short demo

1. Start at the README and show the learning path and quick reference.
2. Run `python learn.py sequences` and explain the shallow-copy example.
3. Run `python learn.py decorators` and explain return-value and metadata preservation.
4. Add and complete a task using `--file .practice/showcase.json`.
5. Run the tests and open a malformed-JSON or invalid-ID test.

Explain one design choice rather than reading every file. Useful choices include isolating examples from import-time execution, using temporary files, and separating the task model from the storage and CLI layers.

## Resume wording

Use only wording that reflects what you have reviewed, understood, and maintained. A possible starting point:

> Developed a core Python learning repository with 21 runnable examples across 10 chapters, edge-case explanations, and a JSON-backed CLI task tracker; added 34 unit and integration tests and a GitHub Actions compatibility workflow.

The counts describe this repository's initial version. Update them as the project grows. The workflow is configured locally; its remote results exist only after you push and it runs. Do not describe learner numbers, adoption, performance gains, or production use unless you have evidence.

## LinkedIn post draft

> I turned my Python course practice notes into **Core Python Field Guide**, a step-by-step course and revision resource.
>
> It covers the foundations through classes, decorators, generators, modules, and standard library tools. Each chapter includes examples, tricky cases, and self-checks. A command-line task tracker brings the concepts together with JSON storage and automated tests.
>
> The exercise I found most useful was explaining why code behaves the way it does: shallow copies, mutable defaults, late-bound closures, and exhausted iterators are all included.
>
> Repository: [add your GitHub repository link]
>
> Feedback on clarity, examples, and missing edge cases is welcome.

Personalize the paragraph about what you learned before posting it.

## Before making it public

Read through the examples and archive, personalize the description, and choose a license if you want others to reuse and distribute your work. No license has been selected in this workspace.

This workspace was not already a Git repository. To create a local repository yourself:

```console
git init
git add .
git commit -m "Create core Python course and task tracker"
```

Create your GitHub repository, then use GitHub's displayed instructions to connect and push it. The workflow will run on pushes and pull requests. No repository has been created or published by preparing these files.
