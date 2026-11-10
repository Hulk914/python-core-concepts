"""Parameter kinds, return values, and a safe mutable default pattern.

Run: python learn.py arguments
Try: call describe_person with the name keyword instead of a positional value.
"""


def add(first, second=5):
    """Return a value so the caller can reuse it; printing is a separate concern."""
    return first + second


def sum_args(*numbers):
    """*args collects extra positional arguments into a tuple."""
    return sum(numbers)


def describe_person(name, /, *, language="Python", **details):
    """name is positional-only; language is keyword-only; details is a dict."""
    return {"name": name, "language": language, **details}


def append_item(item, items=None):
    """Create a fresh list only when the caller did not provide one.

    A default such as items=[] would be created once when def executes, so
    successive calls would share the same list. Explicitly supplied lists
    are intentionally mutated and returned.
    """
    if items is None:
        items = []
    items.append(item)
    return items


def main():
    print("Default / keyword:", add(3), add(second=2, first=3))  # 8 5
    print("Variadic sum:", sum_args(10, 20, 30), sum_args())  # 60 0
    values = [2, 3]
    options = {"second": 4}
    print("Unpack positional / keyword:", add(*values), add(1, **options))
    print("Parameter kinds:", describe_person("Ayush", language="Python", city="Pune"))
    print("Independent defaults:", append_item("a"), append_item("b"))
    supplied = []
    append_item("kept", supplied)
    print("An explicitly passed list is mutated:", supplied)


if __name__ == "__main__":
    main()
