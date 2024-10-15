#!/usr/bin/python3

"""module containing 'save_to_json_file' function"""


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file(json)"""
    import json

    with open(filename, "w"):
        data = json.dump(my_obj)
    return (data)
