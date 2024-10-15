#!/usr/bin/python3

"""module containing 'to_json_string' function"""


def to_json_string(my_obj):
    """function that returns the JSON representation of an object"""
    import json

    data = json.dumps(my_obj)
    return (data)
