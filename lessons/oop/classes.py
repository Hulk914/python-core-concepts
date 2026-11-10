"""Class attributes, instance attributes, and special methods.

Run: python learn.py classes
Try: set first.species and compare the instance with the class attribute.
"""


class Dog:
    """A small model evolved from the original course's Dog example."""

    species = "mammal"  # shared through attribute lookup, unless shadowed

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
        self.tricks = []  # each instance gets its own mutable list

    def bark(self, age):
        return f"{self.name} woofs at age {age}; species: {self.species}"

    def __str__(self):
        return f"Dog named {self.name}"

    def __repr__(self):
        return f"Dog(breed={self.breed!r}, name={self.name!r})"

    def __len__(self):
        # A learning example of a protocol; a real domain model may not need len.
        return len(self.name)


def main():
    first = Dog("Labrador", "Jenny")
    second = Dog("Husky", "Sammy")
    first.tricks.append("sit")
    print("Method:", first.bark(10))
    print("str / repr:", str(first), repr(first))
    print("len protocol:", len(first))  # 5
    print("Independent state:", first.tricks, second.tricks)
    print("Class attribute:", Dog.species, second.species)
    first.species = "instance override"
    print("Shadowed attribute:", first.species, second.species, Dog.species)
    print("Has __len__ but name is empty:", bool(Dog("Lab", "")))  # False
    # del first would remove a reference, not promise immediate finalization.


if __name__ == "__main__":
    main()
