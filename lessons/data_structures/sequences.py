"""Lists mutate; tuples preserve their references, not deep immutability.

Run: python learn.py sequences
Try: replace .copy() with deepcopy() in the nested example.
"""

from copy import deepcopy


def main():
    numbers = [3, 1, 1]
    numbers.append(4)
    print("Count / popped:", numbers.count(1), numbers.pop())  # 2 4
    print("Sorted copy:", sorted(numbers), "original:", numbers)
    result = numbers.sort()
    print("In-place sort:", numbers, "return:", result)  # [1, 1, 3] None

    alias = numbers
    shallow = numbers.copy()
    alias.append(9)
    print("Alias follows mutation:", alias, "independent outer list:", shallow)

    original = [[1], [2]]
    copied = original.copy()
    independent = deepcopy(original)
    copied[0].append(99)
    print("Shallow copy shares inner lists:", original)  # [[1, 99], [2]]
    print("Deep copy:", independent)  # [[1], [2]]

    coordinates = (10, 20)
    x, y = coordinates
    print("Tuple unpacking:", x, y, "one-item tuple:", (10,))
    nested = ([1], 2)
    nested[0].append(3)
    print("A list inside a tuple can change:", nested)  # ([1, 3], 2)

    shared_rows = [[0] * 2] * 2
    shared_rows[0][0] = 7
    independent_rows = [[0] * 2 for _ in range(2)]
    independent_rows[0][0] = 7
    print("Repeated references:", shared_rows)  # [[7, 0], [7, 0]]
    print("Independent rows:", independent_rows)  # [[7, 0], [0, 0]]


if __name__ == "__main__":
    main()
