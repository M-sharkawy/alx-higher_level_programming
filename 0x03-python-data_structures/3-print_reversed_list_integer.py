#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    else:
        my_list_reversed = my_list[::-1]
        for num in my_list_reversed:
            print("{:d}".format(num))
