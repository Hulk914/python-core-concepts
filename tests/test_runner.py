"""Exercise the public entry points and ensure imports remain quiet."""

from pathlib import Path
import subprocess
import sys
import unittest

from learn import LESSONS

ROOT = Path(__file__).resolve().parents[1]


class RunnerTests(unittest.TestCase):
    def run_python(self, *arguments):
        return subprocess.run(
            [sys.executable, *arguments], cwd=ROOT,
            capture_output=True, text=True, timeout=30,
        )

    def test_menu_needs_no_input(self):
        result = self.run_python("learn.py")
        self.assertEqual(result.returncode, 0, result.stderr)
        for name in LESSONS:
            self.assertIn(name, result.stdout)

    def test_all_lessons_complete_without_input(self):
        result = self.run_python("learn.py", "all")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        for name in LESSONS:
            self.assertIn(f"=== {name}:", result.stdout)

    def test_single_lesson_does_not_run_other_lessons(self):
        result = self.run_python("learn.py", "strings")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Alternating: aYuSh", result.stdout)
        self.assertNotIn("=== numbers:", result.stdout)

    def test_invalid_lesson_is_a_clear_argument_error(self):
        result = self.run_python("learn.py", "missing")
        self.assertEqual(result.returncode, 2)
        self.assertIn("invalid choice", result.stderr)

    def test_module_execution_sets_main_name(self):
        result = self.run_python("-m", "lessons.modules.imports")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("This module's __name__: __main__", result.stdout)

    def test_importing_every_module_is_quiet_and_does_not_prompt(self):
        script = (
            "import importlib, pkgutil, learn, lessons, projects; "
            "from unittest.mock import patch; "
            "modules = [module.name for package in (lessons, projects) "
            "for module in pkgutil.walk_packages(package.__path__, package.__name__ + '.')]; "
            "guard = patch('builtins.input', side_effect=RuntimeError('Unexpected prompt')); "
            "guard.start(); "
            "[importlib.import_module(name) for name in modules]"
        )
        result = self.run_python("-c", script)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "")
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
