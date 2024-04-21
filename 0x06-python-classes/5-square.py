#!/usr/bin/python3
"""Module to define a Square class with methods to calculate area and print the square."""

class Square:
    """Class that defines a square with a private size and methods to calculate its area and print it."""
    
    def __init__(self, size=0):
        """Initialize the Square with an optional size argument (default 0), which is validated via the size setter."""
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
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square.
        
        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character '#' or an empty line if size is 0."""
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

# Testing script
if __name__ == "__main__":
    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")

