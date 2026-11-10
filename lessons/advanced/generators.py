"""Generator functions suspend at yield and resume on the next request.

Run: python learn.py generators
Try: call next(iterator, 'finished') after consuming the iterator.
"""

from itertools import islice


def cubes(count):
    """Yield cubes from 0 up to, but excluding, count."""
    for number in range(count):
        yield number**3


def fibonacci(count):
    """Yield count Fibonacci values, starting with 1, 1. Negative counts fail.

    Because this is a generator function, validation happens on iteration,
    not when fibonacci(count) creates the generator object.
    """
    if count < 0:
        raise ValueError("count must be non-negative")
    first, second = 1, 1
    for _ in range(count):
        yield first
        first, second = second, first + second


def main():
    print("Cubes:", list(cubes(5)))
    iterator = fibonacci(6)
    print("First / second:", next(iterator), next(iterator))  # 1 1
    print("Remaining:", list(iterator))  # [2, 3, 5, 8]
    print("Exhausted:", list(iterator))  # []
    print("Safe next:", next(iterator, "finished"))
    print("Start again with a new generator:", list(fibonacci(6)))
    print("Take only three:", list(islice(cubes(1_000_000), 3)))
    squares = (number**2 for number in range(5) if number % 2 == 0)
    print("Generator expression:", list(squares))


if __name__ == "__main__":
    main()
