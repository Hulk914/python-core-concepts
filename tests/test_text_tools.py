"""Expand the original single-word capitalization test to cover its contract."""

import unittest

from lessons.testing.text_tools import capitalize_text


class CapitalizeTextTests(unittest.TestCase):
    def test_text_cases(self):
        cases = [
            ("python", "Python"),
            ("HELLO WORLD", "Hello world"),
            ("", ""),
            (" hello", " hello"),
            ("123ABC", "123abc"),
        ]
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertEqual(capitalize_text(text), expected)

    def test_rejects_non_text(self):
        for value in (None, 123, ["python"]):
            with self.subTest(value=value):
                with self.assertRaisesRegex(TypeError, "string"):
                    capitalize_text(value)


if __name__ == "__main__":
    unittest.main()
