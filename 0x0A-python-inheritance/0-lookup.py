#!/usr/bin/python3

"""module for lookup function """


def lookup(obj):
    """
    function return all the attr. and methods of an object

    args:
        obj: object
    """
    return (dir(obj))
