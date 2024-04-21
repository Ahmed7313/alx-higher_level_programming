import math

class MagicClass:
    def __init__(self, radius=0):
        """Initialize the MagicClass with a radius. The radius must be a number (int or float)."""
        self.__validate_radius(radius)
        self.__radius = radius

    def __validate_radius(self, radius):
        """Validate that the radius is an int or float."""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")

    def area(self):
        """Calculate the area of the circle."""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Calculate the circumference of the circle."""
        return 2 * math.pi * self.__radius

# Example of using the MagicClass
if __name__ == "__main__":
    try:
        circle = MagicClass(12.34)
        print(f"Area: {circle.area()}")
        print(f"Circumference: {circle.circumference()}")
    except Exception as e:
        print(e)

