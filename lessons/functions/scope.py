"""LEGB lookup: Local, Enclosing function, Global module, Builtins.

Run: python learn.py scope
Try: remove nonlocal and explain the resulting UnboundLocalError.
"""

COURSE = "Core Python"


def make_counter(start=0):
    """Return a closure with its own saved count."""
    count = start

    def increment():
        nonlocal count  # rebind the variable in the enclosing function
        count += 1
        return count

    return increment


def main():
    local_label = "scope lesson"
    print("Local / global / builtin:", local_label, COURSE, len(COURSE))
    first = make_counter()
    second = make_counter(10)
    print("Independent closures:", first(), first(), second())  # 1 2 11

    # Closures look up the shared name when called, after this loop has finished.
    late = [lambda: index for index in range(3)]
    captured = [lambda index=index: index for index in range(3)]
    print("Late binding:", [function() for function in late])  # [2, 2, 2]
    print("Default captures each value:", [function() for function in captured])
    # Avoid names such as str, list, and int for variables: they hide builtins.


if __name__ == "__main__":
    main()
