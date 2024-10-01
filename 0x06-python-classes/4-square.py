#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """
    A class to represent a square.

    ...

    Parameters
    ----------
    size (str) : size of the square.

    Methods
    -------
    area():
        Returns the area of square

    Raises:
    -------
        TypeError: if value is not an int
        ValueError: if value is less than 0
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
        self.__size = size

        @property
        def size(self):
            """retreive the size of the square"""
            return self.__size

        @size.setter
        def size(self, value):
            """set the size of the square
                        ...
            Args:
            -----
                value (int) : suppose to be int value
            Raises:
            -------
                TypeError: if value is not an int
                ValueError: if value is less than 0
            """
            if type(size) is not int:
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

    def area(self):
        """
        Returns the area of a Square
        """
        return (self.__size ** 2)
