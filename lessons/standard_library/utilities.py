"""A compact introduction to random, json, re, itertools, and math.

Run: python learn.py utilities
Try: serialize a set with json.dumps and identify the unsupported type.
"""

from itertools import chain, islice
import json
from math import isclose
import random
import re


def main():
    generator = random.Random(7)  # local seed; do not change global random state
    cards = [1, 2, 3, 4]
    result = generator.shuffle(cards)
    print("Shuffle mutates / return:", cards, result)
    print("Pick:", generator.choice(cards))
    # random is for simulations. Use secrets for security-sensitive tokens.

    encoded = json.dumps({"name": "Ayush", "active": True}, sort_keys=True)
    print("JSON text:", encoded)
    print("Decoded boolean:", json.loads(encoded)["active"])
    print("JSON converts tuples to arrays/lists:", json.loads(json.dumps((1, 2))))
    print("Digit groups:", re.findall(r"\d+", "lesson 12, page 34"))
    print("Whole-string check:", bool(re.fullmatch(r"[A-Za-z]+", "Python3")))
    print("Chain:", list(chain([1, 2], [3])))
    print("Slice an iterator:", list(islice(range(100), 2, 5)))
    print("Float comparison:", isclose(0.1 + 0.2, 0.3))


if __name__ == "__main__":
    main()
