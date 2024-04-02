# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Generic animal sound"

# Child class inheriting from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    # Method overriding
    def speak(self):
        return "Woof!"

# Another child class inheriting from Animal
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    # Method overriding
    def speak(self):
        return "Meow!"

# Create instances of the classes
dog1 = Dog("Buddy", "Golden Retriever")
cat1 = Cat("Whiskers", "Tabby")

# Polymorphism: Call the speak method on different objects using a reference to the superclass
animals = [dog1, cat1]
for animal in animals:
    print(animal.name, "says:", animal.speak())