#!/usr/bin/python3
"""Define a MagicClass matching exactly a bytecode provided by ALX."""

import math

class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialize a MagicClass.
        
        Args:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = 0  # Initialize the radius to 0.
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")  # Type checking for radius.
        self.__radius = radius  # Set radius after validation.

    def area(self):
        """Return the area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)  # Area calculation using the formula A = πr².

    def circumference(self):
        """Return the circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)  # Circumference calculation using the formula C = 2πr.

# Example of using the MagicClass
if __name__ == "__main__":
    try:
        circle = MagicClass(12.34)
        print(f"Area: {circle.area()}")  # Example of calling the area method.
        print(f"Circumference: {circle.circumference()}")  # Example of calling the circumference method.
    except Exception as e:
        print(e)

