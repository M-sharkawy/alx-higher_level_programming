#!/usr/bin/python3

"""Model for class Base"""


class Base:
    """
    """
    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id
        Base.__nb_objects += 1
