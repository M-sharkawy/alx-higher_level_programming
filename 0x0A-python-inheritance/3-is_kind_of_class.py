#!/usr/bin/python3

"""module for 'is_same_class' function """


def is_same_class(obj, a_class):
    """Return TRUE or FALSE according to type of class

    args:
        obj: object import
        a_class: class type

    Return:
        True
        False
    """
    if issubclass(obj, a_class)):
        return True
    else:
        return False
