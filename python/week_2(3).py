# Base class
class Animal:
    def make_sound(self):
        print("Some generic animal sounds")

# Derived class Dog
class Dog(Animal):
    def __init__(self, name="Husky"):
        self.name = name

    def make_sound(self):
        print(f"{self.name} says Bow!")

# Derived class Cat
class Cat(Animal):
    def __init__(self, name="Max"):
        self.name = name

    def make_sound(self):
        print(f"{self.name} says Meow!")

# Derived class Bird
class Bird(Animal):
    def __init__(self, name="Perks"):
        self.name = name

    def make_sound(self):
        print(f"{self.name} says Tweet!")

# Creating a list of objects
a1 = [Dog(), Cat(), Bird()]

# Loop through objects and call their methods
for a in a1:
    a.make_sound()
