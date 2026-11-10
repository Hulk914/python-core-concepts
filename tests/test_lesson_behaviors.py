"""Check reusable examples at boundaries that reveal common misunderstandings."""

from contextlib import redirect_stdout
from io import StringIO
import unittest

from lessons.advanced.decorators import announce
from lessons.advanced.generators import cubes, fibonacci
from lessons.basics.strings import alternating_case
from lessons.control_flow.comprehensions import extract_even
from lessons.files_exceptions.handling_errors import parse_integer
from lessons.functions.arguments import append_item, describe_person, sum_args
from lessons.functions.scope import make_counter
from lessons.oop.classes import Dog


class LessonBehaviorTests(unittest.TestCase):
    def test_alternating_text_and_empty_input(self):
        self.assertEqual(alternating_case("ayush"), "aYuSh")
        self.assertEqual(alternating_case(""), "")
        self.assertEqual(alternating_case("a b"), "a b")  # position counts spaces

    def test_even_filter_preserves_order_duplicates_and_input(self):
        numbers = [4, 1, -2, 0, 4]
        self.assertEqual(extract_even(numbers), [4, -2, 0, 4])
        self.assertEqual(numbers, [4, 1, -2, 0, 4])
        self.assertEqual(extract_even([]), [])

    def test_default_lists_do_not_leak_between_calls(self):
        first = append_item("one")
        second = append_item("two")
        self.assertEqual(first, ["one"])
        self.assertEqual(second, ["two"])
        self.assertIsNot(first, second)

    def test_explicit_list_is_mutated_even_when_empty(self):
        supplied = []
        self.assertIs(append_item("one", supplied), supplied)
        self.assertEqual(supplied, ["one"])

    def test_argument_contracts(self):
        self.assertEqual(sum_args(), 0)
        self.assertEqual(sum_args(1, -1, 4), 4)
        self.assertEqual(describe_person("Ada")["language"], "Python")
        with self.assertRaises(TypeError):
            describe_person(name="Ada")

    def test_counter_closures_are_independent(self):
        first, second = make_counter(), make_counter(10)
        self.assertEqual([first(), first(), second(), first()], [1, 2, 11, 3])

    def test_integer_parsing_and_cause(self):
        self.assertEqual(parse_integer(" -12 "), -12)
        for text in ("", "1.5", "no"):
            with self.subTest(text=text):
                with self.assertRaises(ValueError) as caught:
                    parse_integer(text)
                self.assertIsInstance(caught.exception.__cause__, ValueError)

    def test_dogs_have_separate_state(self):
        first, second = Dog("Lab", "Jenny"), Dog("Husky", "Sammy")
        first.tricks.append("sit")
        first.species = "override"
        self.assertEqual(second.tricks, [])
        self.assertEqual(second.species, "mammal")
        self.assertEqual(len(first), 5)
        self.assertFalse(Dog("Lab", ""))

    def test_decorator_forwards_arguments_return_and_metadata(self):
        @announce
        def combine(first, *, second):
            """A documented function."""
            return first + second

        output = StringIO()
        with redirect_stdout(output):
            self.assertEqual(combine(2, second=3), 5)
        self.assertEqual(combine.__name__, "combine")
        self.assertEqual(combine.__doc__, "A documented function.")
        self.assertEqual(output.getvalue(), "Before combine\nAfter combine\n")

    def test_decorator_propagates_failure_without_after_message(self):
        @announce
        def fail():
            raise ValueError("expected failure")

        output = StringIO()
        with redirect_stdout(output), self.assertRaisesRegex(ValueError, "expected failure"):
            fail()
        self.assertEqual(output.getvalue(), "Before fail\n")

    def test_fibonacci_sequence_and_exhaustion(self):
        iterator = fibonacci(6)
        self.assertEqual(next(iterator), 1)
        self.assertEqual(list(iterator), [1, 2, 3, 5, 8])
        self.assertEqual(list(iterator), [])
        self.assertEqual(next(iterator, "done"), "done")
        with self.assertRaises(StopIteration):
            next(iterator)

    def test_empty_and_invalid_generator_counts(self):
        self.assertEqual(list(fibonacci(0)), [])
        self.assertEqual(list(cubes(0)), [])
        self.assertEqual(list(cubes(4)), [0, 1, 8, 27])
        iterator = fibonacci(-1)  # construction does not run validation
        with self.assertRaisesRegex(ValueError, "non-negative"):
            next(iterator)


if __name__ == "__main__":
    unittest.main()
