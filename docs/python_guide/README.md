# Python guide source and build instructions

The [99-page PDF](../ultimate_python_core_guide.pdf) is the main reading edition. The [expanded Markdown edition](../ultimate_python_core_guide.md) is searchable and editable without a PDF editor.

The guide includes theory, repository examples with source locations, worked outputs, ten exercises and solutions, a task-tracker walkthrough, revision pages, 46 primary references and 48 answered interview questions (12 per level). Extensions beyond the original course are marked. The interview section is the final section of the book.

## Source structure

- `01_foundations.md`: getting started, values, text, containers and control flow.
- `02_functions_files.md`: functions, scope, annotations, files and exceptions.
- `03_objects_iteration_modules.md`: objects, protocols, iteration, decorators and imports.
- `04_library_testing_project.md`: standard library, testing, capstone and advanced extensions.
- `05_workbook_revision_references.md`: practice, solutions, revision and reference library.
- `06_interviews_fresher_mid.md`: mock format, fresher and mid-level questions.
- `07_interviews_senior_architect.md`: senior and architect questions.
- `references.json`: official reference titles and links.

`<!-- page -->` defines an intentional print page. A heading immediately after it supplies the page title; `Section:` supplies its section. `{{code:relative/path.py:symbol}}` extracts a complete top-level function or class, including its decorators and original line number. `[[R01]]` resolves an official reference. Keep these markers in the source chapters; the expanded reading edition contains the actual code and links.

## Rebuild

The course still requires only the standard library. PDF authoring tools are optional and separate. Use a local environment or install them into the ignored `.book-tools` directory:

```console
python -m pip install --target .book-tools -r docs/python_guide/requirements.txt
python tools/build_python_guide.py
python tools/inspect_python_guide.py
```

The builder uses Windows Calibri and Consolas fonts from `C:/Windows/Fonts`. On another operating system, update `register_fonts()` in `tools/build_python_guide.py` to point to equivalent available TrueType files. The checked build used Python 3.14.6 for the authoring tools. The course's 34 tests were also run using the available Python 3.15.0 interpreter.

The builder emits the PDF and expanded Markdown, creates two linked contents pages and one bookmark per PDF page, rejects more than 100 pages, checks code widths and page fit, parses Python blocks with Python 3.10's grammar and executes blocks marked `python verify` in isolated subprocesses. These checks do not replace testing every supported interpreter.

The inspection tool checks page and bookmark counts, interview counts, extracted text, internal destinations and text bounds. It renders representative pages and a contact sheet into ignored `.book-preview/`. `build_manifest.json` there records source hashes and the build results; `pdf_audit.json` records PDF inspection results. Review rendered pages after layout or content changes.

Only mark independent, bounded snippets `python verify`. They should use temporary storage for file changes and must not require personal data, network access or input. Unmarked snippets can be partial examples, but all Python blocks must parse. Blocks extracted from repository functions are parsed without being executed alone because their imports/context may live elsewhere in the module.

## Verified edition

The prepared edition has 99 pages, 99 PDF bookmarks, 21 contents links, 293 external links, 88 parse-checked Python blocks and 70 executable example checks. All 34 repository tests pass. Representative rendered pages were visually reviewed; automated bounds checks found no text outside a page. External links point to checked official sources; future availability remains under their publishers' control.

When editing, change the source chapter, not only the expanded Markdown. Rerun the builder and inspection after relevant changes, and update the reported counts if they change. Run repository tests when a maintained implementation or its stated contract changes. Keep archived course notes unchanged.
