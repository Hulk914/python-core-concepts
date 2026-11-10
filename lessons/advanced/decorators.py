"""A decorator accepts a callable and returns a replacement callable.

Run: python learn.py decorators
Try: decorate a function that returns a value and takes keyword arguments.
"""

from functools import wraps


def announce(function):
    """Log before/after a call while preserving its result and metadata."""

    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Before {function.__name__}")
        result = function(*args, **kwargs)
        print(f"After {function.__name__}")
        return result

    return wrapper


@announce
def greet(name, *, punctuation="!"):
    """Return a greeting."""
    return f"Hello, {name}{punctuation}"


def main():
    print("Result:", greet("Ayush", punctuation="."))
    print("Preserved metadata:", greet.__name__, greet.__doc__)
    print("Original via __wrapped__:", greet.__wrapped__("Ada"))
    # @announce means greet = announce(greet). The wrapper body runs on calls,
    # not on import. If the original raises, the 'After' line is not reached;
    # choose try/finally when an action must happen regardless of success.


if __name__ == "__main__":
    main()
