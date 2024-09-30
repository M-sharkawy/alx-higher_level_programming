#!/usr/bin/python3


def safe_print_integer(value):
    try:
        if value == int(value):
            print("{:d}".format(value), end="\n")
            return (True)
    except (ValueError, TypeError):
        return (False)
