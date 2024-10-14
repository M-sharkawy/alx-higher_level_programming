#!/usr/bin/python3

"""Contains a class that inherits from `BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class inherts the 'BaseGeometry' class"""

    def __init__(self, width, height):
        """initialize rectangle values"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        return self.__height * self.__wdith
