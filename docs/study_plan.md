# A practical study plan

[Course home](../README.md) · [Quick reference](quick_reference.md)

Use this as ten study sessions plus a final project. A session can take 30–60 minutes, but explaining the examples matters more than finishing on a schedule.

## The routine for every chapter

1. Read the chapter's goal and walkthrough.
2. Open its Python files and predict the commented results before running them.
3. Run each lesson with `python learn.py <name>`.
4. Change one input or condition, predict the new result, and run again.
5. Answer the self-check and complete the matching exercise without looking at the solution.
6. Check the explanation, then write one sentence about what surprised you.

Do not just uncomment old fragments: every new lesson is already runnable. Keep your own variations in a separate practice file or branch.

| Session | Material | Checkpoint |
| --- | --- | --- |
| 1 | Values and strings | Explain slicing, conversion, and truthiness |
| 2 | Data structures | Draw aliasing versus shallow/deep copying |
| 3 | Control flow | Rewrite a comprehension as a loop |
| 4 | Functions | Explain defaults, keyword-only parameters, and a closure |
| 5 | Files and exceptions | Read a file with `with`, handle a specific failure |
| 6 | Objects | Distinguish class state, instance state, inheritance, composition |
| 7 | Decorators and generators | Preserve a wrapped return value; explain exhaustion |
| 8 | Modules | Move a helper into a package and run a module with `-m` |
| 9 | Standard library | Pick a suitable tool for counting, dates, paths, and JSON |
| 10 | Testing | Add a meaningful edge-case test and inspect a failure |
| 11–12 | Task tracker | Build the layers in order and run its tests |

## Returning after a break

Read the [quick reference](quick_reference.md), run the lesson on the topic you need, and answer its two self-check questions. If the output is surprising, return to that chapter's walkthrough. Run all demonstrations with `python learn.py all` for a broader review.

## What this course covers

This is a foundation in the Python language and standard library, including modules, object-oriented programming, generators, decorators, and testing. It does not attempt to teach web frameworks, data science, async programming, deployment, or a complete packaging workflow. Those are good next projects after you can explain and modify the task tracker.
