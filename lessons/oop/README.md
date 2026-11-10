# 6. Objects, inheritance, and composition

Previous: [Files and exceptions](../files_exceptions/README.md) · Next: [Decorators and generators](../advanced/README.md)

**Goal:** keep related state and behavior together, and choose relationships deliberately.

## Walkthrough

1. Run `python learn.py classes`; read [classes.py](classes.py). A class defines behavior; each instance holds its own state. `self` is the instance passed to an instance method.
2. Compare `species` on the class with `name`, `breed`, and `tricks` on each instance. Moving `tricks = []` to the class would share one list across instances.
3. Trace `print(dog)`, `repr(dog)`, and `len(dog)` to `__str__`, `__repr__`, and `__len__`. Implement protocols only when they make sense for the model.
4. Run `python learn.py inheritance`; read [inheritance.py](inheritance.py). `Cat` is an `Animal`; `Owner` has an animal. `super()` delegates through the method resolution order.
5. See how the caller can use `.speak()` on different objects without branching on their concrete types: this is polymorphism. Python also supports duck typing without shared inheritance.

## Tricky cases

- Setting `dog.species` shadows the class attribute for that instance. Setting `Dog.species` affects instances that still use the class value.
- `del dog` removes that reference. It does not promise that `__del__` runs immediately, and it is not a resource management strategy.
- With no `__bool__`, Python can use `__len__` for truthiness; a zero-length object is falsy.
- `@dataclass` generates routine methods. Its equality compares field values using their own equality rules; it does not make the whole object graph deeply immutable.
- A field annotated `pet: Animal` is not checked automatically when constructing the owner.
- Prefer composition when a relationship is about containing or using another object, rather than being a subtype.

## Self-check

1. Why should each dog's `tricks` list be created in `__init__`?
2. In this lesson, why is `bool(Dog("Lab", ""))` false?

Then try [exercise 6](../../docs/exercises.md#6-a-small-book-class). [Answers](../../docs/solutions.md#chapter-self-checks).
