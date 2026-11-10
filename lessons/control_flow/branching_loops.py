"""Conditions, iteration helpers, and loop control.

Run: python learn.py loops
Try: remove 4 from candidates and observe the for/else result.
"""


def main():
    score = 75
    if score >= 90:
        grade = "excellent"
    elif score >= 60:
        grade = "pass"
    else:
        grade = "retry"
    print("Grade:", grade)
    print("Chained comparison:", 60 <= score < 90)
    print("Short circuit returns an operand:", "" or "fallback", "ready" and 42)

    for number in range(1, 5):  # 1, 2, 3, 4; stop is excluded
        if number % 2:
            continue
        print("Even:", number)

    for index, letter in enumerate("cat", start=1):
        print("Position:", index, letter)
    for first, second in [(1, 2), (3, 4)]:
        print("Unpacked:", first, second)
    print("zip stops at shorter input:", list(zip(["a", "b"], [10])))

    remaining = 2
    while remaining > 0:
        print("Countdown:", remaining)
        remaining -= 1

    candidates = [1, 3, 4]
    for candidate in candidates:
        if candidate % 2 == 0:
            print("Found an even number:", candidate)
            break
    else:
        print("No even number found")  # executes only if no break occurred

    print("Safe removal using a new list:", [n for n in candidates if n % 2])


if __name__ == "__main__":
    main()
