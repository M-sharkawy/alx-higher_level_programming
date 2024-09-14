#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list) - 1):
        list = my_list.copy()
        return list
    else:
        list = my_list.copy()
        list[idx] = element
        return list
