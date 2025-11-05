# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

# Derived class Dog
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")

# Derived class Cat
class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing.")

# Creating objects
d = Dog("Buddy")
c = Cat("Whiskers")

# Calling inherited and class-specific methods
d.eat()
d.bark()
c.eat()
c.meow()
