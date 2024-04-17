#!/usr/bin/python3
class Square:
    """A class to represent a square with a private instance attribute size."""

    def __init__(self, size=0):
        """Initialize the Square with a specific size.

        Args:
            size (int): The size of a side of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The current square area.
        """
        return self.__size ** 2

