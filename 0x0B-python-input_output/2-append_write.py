#!/usr/bin/python3

"""module containing 'append_write' function"""


def append_write(filename="", text=""):
    """function that appends a string at the end of
    a text file (UTF8) and returns the number
    of characters written"""
    with open(filename, "a", encoding="UTF-8") as f:
        data = f.write(text)
        return (data)
