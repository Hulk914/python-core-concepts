"""Catch errors you can handle; separate parsing, work, and cleanup.

Run: python learn.py exceptions
Try: pass an empty string or a decimal string to parse_integer.
"""


def parse_integer(text):
    """Parse text as int, or raise a helpful ValueError with the original cause."""
    try:
        return int(text)
    except ValueError as error:
        raise ValueError(f"Expected a whole number, got {text!r}") from error


def divide(numerator, denominator):
    """Keep ZeroDivisionError visible for the caller to handle appropriately."""
    return numerator / denominator


def main():
    for text in ("12", "oops"):
        try:
            number = parse_integer(text)
        except ValueError as error:
            print("Handled:", error)
        else:
            print("Successful parse + 10:", number + 10)
        finally:
            print("Finished this attempt")  # runs on success and failure

    try:
        divide(10, 0)
    except ZeroDivisionError:
        print("Cannot divide by zero")
    # A bare except also catches KeyboardInterrupt and SystemExit. Prefer a
    # specific type. A return inside finally can hide a return or an exception.
    # Use context managers for resource cleanup instead of __del__.


if __name__ == "__main__":
    main()
