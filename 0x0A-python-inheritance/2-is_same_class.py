#!/usr/bin/python3

"""module for is same class function """


def is_same_class(obj, a_class):
    """
    function that returns True if the object is exactly
    an instance of the specified class ;
    otherwise False

    obj: object import
        a_class: class type

    Return:
        True or False
    """
    if type(obj) == a_class:
        return True
    else:
        return False
