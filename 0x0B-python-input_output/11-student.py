#!/usr/bin/python3

"""module containing 'Student' class"""


class Student:
    """
    Class contains student info

    args:
        first_name (str): first name
        last_name (str): last name
        age (int): age

    Methods:
        _init_ : initializing method
        to json: convert instances to json
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            mydict = {}
            for element in attrs:
                try:
                    mydict[element] = getattr(self, element)
                except AttributeError:
                    pass
            return mydict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key in json:
            setattr(self, key, json[key])
