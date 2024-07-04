#!/usr/bin/python3
"""Defines a class Square that represents a square with size and position attributes."""

class Square:
    """Class that represents a square with control over its size and position attributes."""
    
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the Square with optional size and position arguments.
        
        Args:
            size (int): The size of the square, default is 0.
            position (tuple): The (x, y) position tuple for the square.
        """
        self.size = size
        self.position = position
    
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

    @property
    def position(self):
        """tuple: Retrieves the private position attribute of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square, ensuring it is a tuple of 2 positive integers.

        Args:
            value (tuple): The new position of the square.
        
        Raises:
            TypeError: If `value` is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square.
        
        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character '#' based on its size and position."""
        if self.__size == 0:
            print("")
            return
        
        # Print the new lines before the square
        print("\n" * self.__position[1], end="")

        # Print the square with spaces for the x position
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

# Testing script
if __name__ == "__main__":
    my_square_1 = Square(3)
    my_square_1.my_print()

    print("--")

    my_square_2 = Square(3, (1, 1))
    my_square_2.my_print()

    print("--")

    my_square_3 = Square(3, (3, 0))
    my_square_3.my_print()

    print("--")

