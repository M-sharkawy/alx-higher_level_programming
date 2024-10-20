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
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        import json

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            my_dict = json.dumps(list_dictionaries)
            return my_dict

    @staticmethod
    def from_json_string(json_string):
        import json

        if json_string is None or len(json_string) == 0:
            return "[]"
        else:
            str_dict = json.dumps(json_string)
            return str_dict
