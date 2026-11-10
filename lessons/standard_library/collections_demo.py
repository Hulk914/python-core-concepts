"""Counter, defaultdict, and namedtuple solve common container tasks.

Run: python learn.py collections
Try: compare groups.get('missing') with groups['missing'].
"""

from collections import Counter, defaultdict, namedtuple


def main():
    counts = Counter([1, 1, 1, 2, 2, 3])
    print("Counts / most common:", counts, counts.most_common(1))
    print("Missing Counter key:", counts[99])  # 0, does not insert the key
    print("Missing key inserted?:", 99 in counts)  # False
    groups = defaultdict(list)
    for category, name in [("fruit", "apple"), ("fruit", "pear"), ("veg", "carrot")]:
        groups[category].append(name)
    print("Grouped:", dict(groups))
    print("get does not call default factory:", groups.get("missing"))  # None
    print("Missing [] creates a value:", groups["missing"])
    print("Key now exists:", "missing" in groups)  # True

    Dog = namedtuple("Dog", ["age", "breed", "name"])
    sammy = Dog(age=5, breed="Husky", name="Sammy")
    print("Named / positional access:", sammy.age, sammy[0])
    print("New value, original unchanged:", sammy._replace(age=6), sammy.age)


if __name__ == "__main__":
    main()
