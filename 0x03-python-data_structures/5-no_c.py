#!/usr/bin/python3
# author: sharkawy


def no_c(my_string):
    filtered_string = [c for c in my_string if c not in ('C', 'c')]

    return ("".join(filtered_string))
