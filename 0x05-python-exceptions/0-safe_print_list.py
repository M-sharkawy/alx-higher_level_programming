#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    index = 0

    try:
        while index < x:
            print("{:d}".format(my_list[index]), end="")
            index += 1
    except IndexError:
        pass

    print()
    return index
