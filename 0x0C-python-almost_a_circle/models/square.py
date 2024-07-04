#!/usr/bin/python3
"""Module for Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance with size, x, y, and id."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square, updating both width and height."""
        self.width = value  # Rectangle's setter handles validation
        self.height = value  # Ensure height matches width

    def __str__(self):
        """Return string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """Update attributes of the Square instance."""
        attributes = ['id', 'size', 'x', 'y']
        if args:
            # Assign args based on order to attributes
            for attr, value in zip(attributes, args):
                if attr == 'size':
                    self.size = value  # Utilize size setter for validation
                else:
                    setattr(self, attr, value)
        elif kwargs:
            # Assign kwargs to attributes if args is empty
            for key, value in kwargs.items():
                if key == 'size':
                    self.size = value  # Utilize size setter for validation
                elif key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Square."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
