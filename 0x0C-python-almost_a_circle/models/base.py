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
        """method converts json to str"""
        import json

        if json_string is None or len(json_string) == 0:
            return "[]"
        else:
            str_dict = json.loads(json_string)
            return str_dict

    @classmethod
    def save_to_file(cls, list_objs):
        """saves list of instance to a file"""
        if list_objs is None or list_objs == 0:
            return "[]"
        else:
            my_list = []
            my_list = [obj.to_dictionary() for obj in list_objs]
            json_str = cls.to_json_string(my_list)
            with open(f"{cls.__name__}.json", "w", encoding="UTF-8") as f:
                f.write(json_str)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance with all
        attributes set based on the dictionary."""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)

        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        with open(f"{cls.__name__}.json", "r", encoding="UTF-8") as file:
            if file is None:
                return []
            else:
                my_list = []
                instance_list = []
                my_list = cls.from_json_string(file.read())
                for i in my_list:
                    instance_list.append(cls.create(**i))
                return instance_list
