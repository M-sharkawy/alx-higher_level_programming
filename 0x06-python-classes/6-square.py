#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """
    A class to represent a square.

    ...

    Parameters
    ----------
    size (int) : size of the square.
    position (int): position of tuple

    Methods
    -------
    area(): Returns the area of square
    position(): Return the position

    Raises:
    -------
        TypeError: if value is not an int
        ValueError: if value is less than 0
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Constructs all the necessary attributes for the square object.

        Parameters
        ----------
        size (int) : size of the square.
        position (int) : tuple

        Methods
        -------
        area(): Returns the area of square
        position() : Return position

        Raises:
        -------
            TypeError: if value is not an int
            ValueError: if value is less than 0
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """retreive the size of the square"""
        return self._size

    @size.setter
    def size(self, value):
        """set the size of the square
                    ...
            Args:
            -----
                value (int) : the square size
            Raises:
            -------
                TypeError: if value is not an int
                ValueError: if value is less than 0
            """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = value

    @property
    def position(self):
        """ makes the private attribute to be used in class """
        return self.__position

    @position.setter
    def position(self, value):
        """set the size of the square
                    ...
            Args:
            -----
                value (int) : tuple poistion
            Raises:
            -------
                TypeError: position must be a tuple of 2 positive integers
            """
        if (type(value) is not tuple or len(value) != 2 or
                type(value[1]) is not int or value[1] < 0 or
                type(value[0]) is not int or value[0] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Returns the area of a Square
        """
        return (self._size ** 2)

    def my_print(self):
        """print square of #"""
        if self.size <= 0:
            print()
            return
        else:
            for i in range(self.position[1]):
                print("")
            for i in range(self.size):
                print(" " * self.position[0] + '#' * self.size)
