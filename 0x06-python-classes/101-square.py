#!/usr/bin/python3
"""Define a class Square."""

class Square:
    """Represent a square with properties for size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square with a given size and position.
        
        Args:
            size (int): The size of the new square, must be a non-negative integer.
            position (tuple of int): The x and y offset position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the '#' character, taking into account its position."""
        if self.__size == 0:
            print("")
            return
        
        print("\n" * self.__position[1], end="")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Return the string representation for printing a Square."""
        if self.__size == 0:
            return ""
        
        lines = []
        lines.extend([""] * self.__position[1])  # Append new lines based on vertical position
        for _ in range(self.__size):
            lines.append(" " * self.__position[0] + "#" * self.__size)
        
        return "\n".join(lines)

# Example usage
if __name__ == "__main__":
    my_square = Square(5, (0, 0))
    print(my_square)

    print("--")

    my_square = Square(5, (4, 1))
    print(my_square)

