#!/usr/bin/python3

"""module containing 'read_file' function"""


def read_file(filename=""):
    """function reads a text file (UTF8)
    and prints it to stdout
    """
    with open(filename, "r", encoding="UTF8") as f:
        print(f.read())
