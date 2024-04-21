#!/usr/bin/python3
"""Defines a class Square that represents a square with a property-controlled attribute."""

class Square:
    """A class that represents a square, controlling access to the size attribute 
    with property getters and setters to enforce that size is a non-negative integer."""

    def __init__(self, size=0):
        """Initialize a new Square instance with a given size.
        
        Args:
            size (int): The size of the square, default is 0.
        """
        self.size = size

    @property
    def size(self):
        """int: Retrieves the private size attribute of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square, ensuring it is an integer and non-negative.
        
        Args:
            value (int): The new size of the square.
        
        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Calculate and return the area of the square.
        
        Returns:
            The area of the square.
        """
        return self.__size ** 2

