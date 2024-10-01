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
    def __init__(self, size):
        """
        Constructs all the necessary attributes for the square object.

        Parameters
        ----------
            size : str
                size of the square.
        """
        self.__size = size
