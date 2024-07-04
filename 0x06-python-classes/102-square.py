#!/usr/bin/python3
"""Defines a class Square with a size attribute and comparison capabilities based on area."""

class Square:
    """Class representing a square with comparison based on its area."""
    
    def __init__(self, size=0):
        """Initialize a new square with a given size.
        
        Args:
            size (float|int): The size of the new square, must be a non-negative number.
        """
        self.size = size

    @property
    def size(self):
        """float|int: Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square, ensuring it's a number and non-negative.

        Raises:
            TypeError: If the value is not a number (int or float).
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Check equality based on area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check inequality based on area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check less than based on area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check less than or equal based on area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check greater than based on area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check greater than or equal based on area."""
        return self.area() >= other.area()

# Example usage
if __name__ == "__main__":
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")

