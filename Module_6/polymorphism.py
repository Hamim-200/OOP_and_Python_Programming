class Animal:
    def make_sound(self):
        print("This is an animal sound.")

class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow! Meow!")

# Function to demonstrate polymorphism
def animal_sound(animal):
    animal.make_sound()

# Creating instances of Dog and Cat
dog = Dog()
cat = Cat()

# Calling the function with different objects
animal_sound(dog)  # Output: Woof! Woof!
animal_sound(cat)  # Output: Meow! Meow!
