#!/usr/bin/python3

"""module containing an empty 'BaseGeometry' class"""


class BaseGeometry:
    """Base geometry class """
    def area(self):
        """calculates area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates 'value'"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """class inherts the 'BaseGeometry' class"""
    def __init__(self, width, height):
        """initialize rectangle values"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
