#!/usr/bin/python3

"""Model for class Base"""


class Base:
    """ The Base class is to manage base for all the program
    to manage id attributties

    args:
        id (int): id number
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
