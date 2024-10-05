#!/usr/bin/python3

"""this module  function that prints My name is <first name> <last name> """


def say_my_name(first_name, last_name=""):
    """
    this function prints the first and second names

    Args:
        first_name (string) : first name
        last_name (string) : last name

    Returns:
        first and last name

    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
