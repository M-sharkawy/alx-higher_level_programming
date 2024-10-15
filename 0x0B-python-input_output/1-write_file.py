#!/usr/bin/python3

"""module containing 'read_file' function"""


def write_file(filename="", text=""):
    """function writes a string to a text file (UTF8)
      and returns the number of characters written"""
    with open(filename, "w", encoding="UTF-8") as f:
        data = f.write(text)
        return (data)
