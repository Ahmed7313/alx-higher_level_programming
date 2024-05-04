#!/usr/bin/python3
"""Module for Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square, both width and height.
            x (int, optional): The x coordinate. Defaults to 0.
            y (int, optional): The y coordinate. Defaults to 0.
            id (int, optional): An optional id.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
