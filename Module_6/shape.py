import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Function to demonstrate polymorphism
def print_area(shape):
    print(f"The area is: {shape.area()}")

# Creating instances of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Calling the function with different objects
print_area(circle)      # Output: The area is: 78.53981633974483
print_area(rectangle)   # Output: The area is: 24
