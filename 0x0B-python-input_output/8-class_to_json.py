#!/usr/bin/python3

"""module containing 'class_to_json' function"""


def class_to_json(obj):
    """function that returns the dictionary
    description with simple data structur"""

    return (vars(obj))
