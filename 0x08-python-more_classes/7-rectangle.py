#!/usr/bin/python3
"""this module Write an empty class Rectangle that defines a rectangle:"""


class Rectangle:
    """
    empty class Rectangle that defines a rectangle

    args:
        width (int): rectangle width
        height (int): rectangle height

    Methods:
        area(): function to retreive area of the rectangle
        perimeter(): function to retrieve perimeter of the rectangle
        str(): print rectangle of "#"

    Raises:
        TypeError: width must be an integer
        ValueError: width must be >= 0
        TypeError: height must be an integer
        ValueError: height must be >= 0
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Creates new instances of Rectangle.

        args:
            width (int): rectangle width
            height (int): rectangle height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """retrieve the width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """height setter for width retrieval"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """reterieve the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter for height retrieval"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """calculates the rectangle's area"""
        return self.__height * self.__width

    def perimeter(self):
        """calculates the rectangle's perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        """print rectangle of #"""
        line = ""
        if self.__width == 0 or self.__height == 0:
            return line
        for x in range(self.__height):
            for y in range(self.__width):
                line += Rectangle.print_symbol
            if x != self.__height - 1:
                line += "\n"
        return line

    def __repr__(self):
        """retrun rectangle attributies"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """prints a string when instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
