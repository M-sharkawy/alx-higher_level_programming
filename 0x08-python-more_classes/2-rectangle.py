#!/usr/bin/python3

"""this module Write an empty class Rectangle that defines a rectangle:"""


class Rectangle:
    """
    empty class Rectangle that defines a rectangle

    args:
        width (int): rectangle width
        height (int): rectangle height

    Methods:
        area(): function to retreive area of the triangle
        perimeter(): function to retrieve perimeter of the triangle

    Raises:
        TypeError: width must be an integer
        ValueError: width must be >= 0
        TypeError: height must be an integer
        ValueError: height must be >= 0
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieve the width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """reterieve the height of the triangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """retreive area of the triangle"""
        return(self.width * self.height)

    def perimeter(self):
        """retrieve the perimeter of the triangle"""
        if self.width == 0 or self.height == 0:
            return(0)
        else:
            return(self.width + self.height) * 2
