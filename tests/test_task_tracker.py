"""Model, persistence, and CLI contracts; all test files are disposable."""

from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from projects.task_tracker.cli import main
from projects.task_tracker.model import Task, add_task, complete_task, summarize
from projects.task_tracker.storage import load_tasks, save_tasks

ROOT = Path(__file__).resolve().parents[1]


class TaskModelTests(unittest.TestCase):
    def test_add_trims_title_and_uses_maximum_id(self):
        tasks = [Task(5, "Older task"), Task(2, "Another task")]
        task = add_task(tasks, "  New task  ")
        self.assertEqual(task, Task(6, "New task"))
        self.assertIs(tasks[-1], task)

    def test_empty_title_leaves_list_unchanged(self):
        tasks = []
        with self.assertRaisesRegex(ValueError, "empty"):
            add_task(tasks, " \t ")
        self.assertEqual(tasks, [])

    def test_complete_is_repeatable_and_unknown_id_fails(self):
        tasks = [Task(1, "Read"), Task(2, "Practice")]
        self.assertEqual(complete_task(tasks, 1), Task(1, "Read", True))
        complete_task(tasks, 1)
        self.assertFalse(tasks[1].done)
        with self.assertRaisesRegex(ValueError, "No task"):
            complete_task(tasks, 99)

    def test_summary_for_empty_and_mixed_tasks(self):
        self.assertEqual(summarize([]), {"total": 0, "done": 0, "pending": 0})
        tasks = [Task(1, "Read", True), Task(2, "Practice")]
        self.assertEqual(summarize(tasks), {"total": 2, "done": 1, "pending": 1})


class TaskStorageTests(unittest.TestCase):
    def setUp(self):
        self.directory = TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.path = Path(self.directory.name) / "nested" / "tasks.json"

    def test_missing_file_is_empty_without_creating_it(self):
        self.assertEqual(load_tasks(self.path), [])
        self.assertFalse(self.path.exists())

    def test_round_trip_unicode_and_overwrite(self):
        tasks = [Task(1, "Réviser Python"), Task(2, "Write tests", True)]
        save_tasks(self.path, tasks)
        self.assertEqual(load_tasks(self.path), tasks)
        save_tasks(self.path, [])
        self.assertEqual(load_tasks(self.path), [])
        self.assertFalse(self.path.with_suffix(".json.tmp").exists())

    def test_malformed_json_is_reported_and_preserved(self):
        self.path.parent.mkdir()
        self.path.write_text("not json", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Invalid JSON"):
            load_tasks(self.path)
        self.assertEqual(self.path.read_text(encoding="utf-8"), "not json")

    def test_invalid_records_are_rejected(self):
        valid = {"id": 1, "title": "Read", "done": False}
        invalid = [
            {},
            ["not a record"],
            [{"id": 1, "title": "Read"}],
            [{**valid, "extra": 1}],
            [{**valid, "id": True}],
            [{**valid, "id": 0}],
            [{**valid, "id": 1.0}],
            [{**valid, "title": " "}],
            [{**valid, "title": 42}],
            [{**valid, "done": "false"}],
            [valid, valid],
        ]
        self.path.parent.mkdir()
        for records in invalid:
            with self.subTest(records=records):
                self.path.write_text(json.dumps(records), encoding="utf-8")
                with self.assertRaises(ValueError):
                    load_tasks(self.path)

    def test_failed_replace_keeps_existing_file_and_cleans_staging(self):
        save_tasks(self.path, [Task(1, "Original")])
        with patch.object(Path, "replace", side_effect=OSError("replace failed")):
            with self.assertRaisesRegex(OSError, "replace failed"):
                save_tasks(self.path, [Task(2, "New")])
        self.assertEqual(load_tasks(self.path), [Task(1, "Original")])
        self.assertFalse(self.path.with_suffix(".json.tmp").exists())


class TaskCliTests(unittest.TestCase):
    def setUp(self):
        self.directory = TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.path = Path(self.directory.name) / "tasks.json"

    def call_cli(self, *arguments):
        output, errors = StringIO(), StringIO()
        with redirect_stdout(output), redirect_stderr(errors):
            code = main(["--file", str(self.path), *arguments])
        return code, output.getvalue(), errors.getvalue()

    def test_add_list_complete_summary_workflow(self):
        self.assertEqual(self.call_cli("add", "Revise"), (0, "Added #1: Revise\n", ""))
        self.assertEqual(self.call_cli("list"), (0, "[ ] 1: Revise\n", ""))
        self.assertEqual(self.call_cli("done", "1"), (0, "Completed #1: Revise\n", ""))
        self.assertEqual(self.call_cli("list"), (0, "[x] 1: Revise\n", ""))
        self.assertEqual(self.call_cli("summary"), (0, "Total: 1 | Done: 1 | Pending: 0\n", ""))

    def test_read_commands_do_not_create_storage(self):
        self.assertIn("No tasks yet", self.call_cli("list")[1])
        self.assertIn("Total: 0", self.call_cli("summary")[1])
        self.assertFalse(self.path.exists())

    def test_invalid_changes_do_not_write(self):
        code, output, errors = self.call_cli("add", "  ")
        self.assertEqual(code, 1)
        self.assertEqual(output, "")
        self.assertIn("empty", errors)
        self.assertFalse(self.path.exists())
        self.call_cli("add", "Original")
        before = self.path.read_bytes()
        code, _, errors = self.call_cli("done", "99")
        self.assertEqual(code, 1)
        self.assertIn("No task", errors)
        self.assertEqual(self.path.read_bytes(), before)

    def test_corrupt_storage_is_not_overwritten(self):
        self.path.write_text("broken", encoding="utf-8")
        code, _, errors = self.call_cli("add", "New task")
        self.assertEqual(code, 1)
        self.assertIn("Invalid JSON", errors)
        self.assertEqual(self.path.read_text(encoding="utf-8"), "broken")

    def test_module_entrypoint_and_argument_error(self):
        result = subprocess.run(
            [sys.executable, "-m", "projects.task_tracker", "--file", str(self.path), "add", "Demo"],
            cwd=ROOT, capture_output=True, text=True, timeout=15,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Added #1: Demo", result.stdout)
        invalid = subprocess.run(
            [sys.executable, "-m", "projects.task_tracker", "done", "not-an-integer"],
            cwd=ROOT, capture_output=True, text=True, timeout=15,
        )
        self.assertEqual(invalid.returncode, 2)
        self.assertIn("invalid int value", invalid.stderr)


if __name__ == "__main__":
    unittest.main()
