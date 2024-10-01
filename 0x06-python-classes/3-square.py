#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """
    A class to represent a square.

    ...

    Attributes
    ----------
    size : str
        size of the square.
    """
    def __init__(self, size=0):
        """
        Constructs all the necessary attributes for the square object.

        Parameters
        ----------
            size : str
                size of the square.

        Methods
        -------
        area():
            Returns the area of square

        Raises:
        -------
            TypeError: if value is not an int
            ValueError: if value is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Returns the area of a Square
        """
        return (self.__size ** 2)
