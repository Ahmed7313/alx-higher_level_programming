#!/usr/bin/python3
class Square:
    """Class to represent a square with a private size attribute,
    which is managed via a getter and setter to ensure it is an integer and non-negative.
    """

    def __init__(self, size=0):
        """Initialize the Square with an optional size argument (default 0), 
        which is validated via the size setter.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square, raising exceptions if the value
        is not an integer or is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size


# If you wish to test the class with a script, you could use the following:
if __name__ == "__main__":
    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)

