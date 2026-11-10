"""Comprehensions construct containers; generator expressions defer work.

Run: python learn.py comprehensions
Try: rewrite each comprehension as an ordinary for loop.
"""


def extract_even(numbers):
    """Return even values in their original order, including duplicates."""
    return [number for number in numbers if number % 2 == 0]


def main():
    print("Even squares:", [n**2 for n in range(10) if n % 2 == 0])
    print("Filter:", extract_even([1, 2, 2, 3, 4]))  # [2, 2, 4]
    print("Transform every item:", ["even" if n % 2 == 0 else "odd" for n in range(4)])
    print("Dictionary:", {n: n**2 for n in range(3)})
    print("Unique lengths:", sorted({len(word) for word in ["cat", "dog", "python"]}))
    rows = [[1, 2], [3, 4]]
    print("Flatten:", [value for row in rows for value in row])
    squares = (n**2 for n in range(4))
    print("Generator first:", next(squares))  # 0
    print("Generator remaining sum:", sum(squares))  # 1 + 4 + 9 = 14
    print("Empty comprehension:", extract_even([]))


if __name__ == "__main__":
    main()
