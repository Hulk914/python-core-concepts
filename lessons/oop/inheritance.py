"""Inheritance models an 'is a' relationship; composition models 'has a'.

Run: python learn.py inheritance
Try: add another object with a speak() method to the animals list.
"""

from dataclasses import dataclass


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

    def __repr__(self):
        return f"{type(self).__name__}(name={self.name!r})"


class Cat(Animal):
    def __init__(self, name, indoor=True):
        super().__init__(name)
        self.indoor = indoor

    def speak(self):
        return f"{self.name} meows"


@dataclass
class Owner:
    """dataclass generates __init__, __repr__, and value-based __eq__."""

    name: str
    pet: Animal  # composition; annotations do not enforce runtime types

    def introduce(self):
        return f"{self.name}'s pet says: {self.pet.speak()}"


def main():
    animals = [Animal("Alex"), Cat("Milo")]
    for animal in animals:
        print("Same interface, different behavior:", animal.speak())
    print("Subclass check:", isinstance(animals[1], Animal))
    print("Composed object:", Owner("Ayush", animals[1]).introduce())
    print("Generated repr:", Owner("Ada", Animal("Pip")))
    # Value equality of a dataclass follows its fields, including their own ==.


if __name__ == "__main__":
    main()
