# polymorphism_demo.py

import math  # Importing math for π calculations in Circle

# Our base class for any generic shape
class Shape:
    def area(self):
        # Raising NotImplementedError since each shape needs its own area calculation
        raise NotImplementedError("You need to override this method in subclasses!")

# Now, a derived class for rectangles
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        # Rectangle area formula: length * width
        return self.length * self.width

# A derived class for circles
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Circle area formula: π * radius^2
        return math.pi * (self.radius ** 2)