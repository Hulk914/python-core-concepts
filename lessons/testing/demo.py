"""A tiny assertion example; real unit tests live under tests/.

Run: python learn.py testing
Test: python -m unittest tests.test_text_tools -v
"""

from lessons.testing.text_tools import capitalize_text


def main():
    for text in ["python", "HELLO WORLD", ""]:
        print(f"{text!r} -> {capitalize_text(text)!r}")
    assert capitalize_text("python") == "Python"
    print("Example assertion passed. Run unittest for the full test suite.")
    # assert can be disabled with python -O; use explicit exceptions to validate
    # user input. unittest assertions are still checked under optimized mode.


if __name__ == "__main__":
    main()
