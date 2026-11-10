"""Values, operators, conversion, truthiness, and equality.

Run: python learn.py numbers
Try: change the operands of // and % to negative numbers.
"""


def main():
    count = 7
    price = 2.5
    print("Types:", type(count).__name__, type(price).__name__)  # int float
    print("Arithmetic:", count + 2, count / 2, count // 2, count % 2, count**2)
    print("Negative floor division:", -7 // 2)  # -4: floor, not truncation
    print("Conversion:", int("42"), float("3.5"), str(42))
    print("Truncation:", int(-3.9))  # -3: int(float) truncates toward zero

    # input() returns str; explicit conversion is needed before numeric addition.
    entered_text = "12"
    print("Converted input + 10:", int(entered_text) + 10)  # 22
    print("Truthiness:", bool(""), bool([]), bool(0), bool("False"))
    print("Boolean is an int subclass:", isinstance(True, int), True + True)

    left = [1, 2]
    right = [1, 2]
    alias = left
    print("Equal values / same object:", left == right, left is right)  # True False
    print("Alias is same object:", alias is left)  # True
    missing = None
    print("None check:", missing is None)  # use is None, not == None
    print("Floating point:", 0.1 + 0.2 == 0.3)  # False: binary rounding
    print("Readable result:", f"{0.1 + 0.2:.2f}")  # display formatting only


if __name__ == "__main__":
    main()
