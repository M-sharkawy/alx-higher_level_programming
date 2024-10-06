#!/usr/bin/python3

"""this module that prints a square with the character # """


def print_square(size):
    """
    this function prints a square with the character #

    Args:
        size (int): the size length of the square

    Returns:
        a square with the character # according to size

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for item in range(size):
            print("#" * size)
