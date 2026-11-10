"""Strings are immutable sequences; slice stop positions are exclusive.

Run: python learn.py strings
Try: predict the result of word[-2:] before running it.
"""


def alternating_case(text):
    """Lowercase index 0, uppercase index 1, and keep alternating by position."""
    return "".join(
        character.lower() if index % 2 == 0 else character.upper()
        for index, character in enumerate(text)
    )


def main():
    word = "Python"
    print("First / last:", word[0], word[-1])  # P n
    print("Slices:", word[1:4], word[::-1], word[::2])  # yth nohtyP Pto
    print("Oversized slice:", repr(word[99:]))  # ''; word[99] raises IndexError
    print("Original / replacement:", word, "J" + word[1:])  # Python Jython
    print("Methods return new strings:", word.upper(), word)
    print("Clean and split:", "  red,blue  ".strip().split(","))
    print("Join:", " / ".join(["red", "blue"]))
    print("Formatting:", "Hello, {}".format("Ayush"), f"Total: {12.5:.2f}")
    print("Escape versus raw:", repr("line\nnext"), repr(r"line\nnext"))
    print("Alternating:", alternating_case("ayush"))  # aYuSh
    print("Empty input:", repr(alternating_case("")))


if __name__ == "__main__":
    main()
