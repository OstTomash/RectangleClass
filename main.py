class Rectangle:
    """A simple class representing a rectangle.

    This class allows users to define a rectangular width and height, check entered values and
    get the area and perimeter.

    Attributes:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.

    Methods:
        - __init__(width, height) - initialize the Rectangle object with given attributes and
        checking that entered values are greater than or equal to 1.
        - square() - returns the area of the rectangle.
        - perimeter() - returns the perimeter of the rectangle.
        - __str__() - returns a string representation of the rectangle object.


    Example usage:
    >>> example_rect = Rectangle(2, 4)
    >>> example_square = example_rect.square()
    >>> example_perimeter = example_rect.perimeter()
    >>> print(example_rect)
    Rectangle: width = 2, height = 4
    """
    def __init__(self, width, height):
        """
        Initialize a Rectangle object with given attributes and
        checking that entered values are greater than or equal to 1.

        Raises:
            - ValueError: If entered values are less than 1 or negative numbers
        """
        if width < 1 or height < 1:
            raise ValueError("Dimensions must be non-negative and greater than 1.")
        self.width = width
        self.height = height

    def square(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation of the rectangle object"""
        return f"Rectangle: width = {self.width}, height = {self.height}"


rect = Rectangle(2, 4)
square = rect.square()
perimeter = rect.perimeter()

print(rect)
print('Square', square)
print('Perimeter', perimeter)
