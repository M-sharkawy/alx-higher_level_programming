#!/usr/bin/python3

"""module containing an empty 'BaseGeometry' class"""


class BaseGeometry:
    """Base geometry class """
    def area(self):
        """calculates area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates 'value'"""
        self.name = name
        self.value = value
        if type(value) is not int:
            raise TypeError(f"{self.name} must be an integer")
        if value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
