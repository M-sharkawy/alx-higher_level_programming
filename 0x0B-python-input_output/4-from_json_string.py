#!/usr/bin/python3

"""module containing 'from_json_string' function"""


def from_json_string(my_str):
    """function that returns an object (Python data structure)
    represented by a JSON string"""
    import json

    data = json.loads(my_str)
    return (data)
