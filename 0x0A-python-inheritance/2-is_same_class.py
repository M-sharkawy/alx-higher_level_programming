#!/usr/bin/python3

"""module for is same class function """


def is_same_class(obj, a_class):
    """
    function that returns True if the object is exactly
    an instance of the specified class ;
    otherwise False

    args:
        obj: object, a_class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
