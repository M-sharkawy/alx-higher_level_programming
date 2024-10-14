#!/usr/bin/python3

"""module containing 'inherits_from' function"""


def inherits_from(obj, a_class):
    """Returns True or false

    Args:
        obj: object
        a_class: the class to check

    Return:
        True: True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class
        False: otherwise
    """
    if type(obj) == a_class:
        return (False)
    else:
        return (isinstance(obj, a_class))
