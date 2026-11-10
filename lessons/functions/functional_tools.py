"""Use small callables for transformations, predicates, and sort keys.

Run: python learn.py functional
Try: predict the second list(mapped) before running the example.
"""


def main():
    numbers = [1, 2, 3, 4, 5]
    mapped = map(lambda number: number % 2 == 0, numbers)
    print("map transforms:", list(mapped))  # [False, True, False, True, False]
    print("map is an iterator; now exhausted:", list(mapped))  # []
    print("filter selects:", list(filter(lambda number: number % 2 == 0, numbers)))
    print("Often clearer as a comprehension:", [n for n in numbers if n % 2 == 0])
    people = [("Ada", 36), ("Grace", 30), ("Linus", 30)]
    print("Stable sort by age:", sorted(people, key=lambda person: person[1]))
    print("Built-in callable:", sorted(["Python", "a", "code"], key=len))
    print("any / all:", any(n > 4 for n in numbers), all(n > 0 for n in numbers))
    print("Empty any / all:", any([]), all([]))  # False True


if __name__ == "__main__":
    main()
