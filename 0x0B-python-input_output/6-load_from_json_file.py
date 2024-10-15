#!/usr/bin/python3

"""module containing 'load_from_json_file' function"""


def load_from_json_file(filename):
    """function that creates an Object from a (JSON)"""
    import json

    with open(filename, "r") as f:
        for line in f:
            file = line
        data = json.load(file)
    return (data)
