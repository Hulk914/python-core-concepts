"""Dictionaries map hashable keys; sets hold unique hashable values.

Run: python learn.py mappings
Try: explain why a list cannot be a dictionary key.
"""


def main():
    profile = {"name": "Ayush", "language": "Python"}
    profile["level"] = "learning"
    print("Lookup:", profile["name"])
    print("Missing key with default:", profile.get("city", "unknown"))
    print("get does not insert:", "city" in profile)  # False
    print("Insertion order:", list(profile))
    for key, value in profile.items():
        print(f"  {key}: {value}")

    # A repeated key keeps its last assigned value.
    print("Duplicate key:", dict([("a", 1), ("a", 2)]))  # {'a': 2}
    left = {1, 2, 2, 3}
    right = {3, 4}
    left.add(5)
    left.discard(99)  # discard tolerates absence; remove would raise KeyError
    print("Unique values:", sorted(left))
    print("Union:", sorted(left | right))
    print("Intersection:", sorted(left & right))
    print("Difference:", sorted(left - right))
    print("Empty dict / empty set:", type({}).__name__, type(set()).__name__)
    # Sorting makes the displayed output stable; sets have no insertion-order guarantee.
    print("Unique letters:", sorted(set("banana")))


if __name__ == "__main__":
    main()
