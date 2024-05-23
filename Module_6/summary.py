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

# Function to check if the object is an instance of a subclass
def check_instance(obj):
    if isinstance(obj, Circle):
        print("This is a Circle instance.")
    elif isinstance(obj, Rectangle):
        print("This is a Rectangle instance.")
    elif isinstance(obj, Shape):
        print("This is a Shape instance.")
    else:
        print("This is not a Shape instance.")

# Creating instances of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Calling the function with different objects
print_area(circle)      # Output: The area is: 78.53981633974483
print_area(rectangle)   # Output: The area is: 24

# Checking instances
check_instance(circle)  # Output: This is a Circle instance.
check_instance(rectangle)  # Output: This is a Rectangle instance.
check_instance(Shape())  # Output: This is a Shape instance.
