#!/usr/bin/python3

"""module for 'is_same_class' function """


def is_kind_of_class(obj, a_class):
    """Return TRUE or FALSE according to type of class

    args:
        obj: object import
        a_class: class type

    Return:
        True
        False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
