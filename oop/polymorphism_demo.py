# polymorphism_demo.py

import math

# Base class
class Shape:
    def area(self):
        """Base method that should be overridden in derived classes."""
        raise NotImplementedError("Subclasses must implement the area() method.")


# Derived class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculate area of the rectangle."""
        return self.length * self.width


# Derived class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate area of the circle."""
        return math.pi * (self.radius ** 2)
