#!/usr/bin/python3
"""Defines a class Square with a size and position that can be printed directly."""

class Square:
    """A class that represents a square with size and position attributes."""
    
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with optional size and position.

        Args:
            size (int): The size of the square, default is 0.
            position (tuple): The x and y offsets for printing the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """int: Gets or sets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size, ensuring it is a non-negative integer.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """tuple: Gets or sets the position for printing the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position, ensuring it is a tuple of 2 positive integers.

        Raises:
            TypeError: If the value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with '#' characters."""
        print(self.__str__())

    def __str__(self):
        """Return the string representation of the square for printing."""
        if self.__size == 0:
            return "\n"
        
        result = "\n" * self.__position[1]  # Adding vertical spaces (new lines)
        for _ in range(self.__size):
            result += " " * self.__position[0] + "#" * self.__size + "\n"
        return result

# Example usage
if __name__ == "__main__":
    my_square = Square(5, (0, 0))
    print(my_square)

    print("--")

    my_square = Square(5, (4, 1

