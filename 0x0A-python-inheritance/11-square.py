#!/usr/bin/python3

"""module Contains a class that inherits from `rectangle'"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size):
        """initiation function"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area calculation"""
        return (self.__size * self.__size)

    def __str__(self):
        """print method"""
        return f"[Square] {self.__size}/{self.__size}"
