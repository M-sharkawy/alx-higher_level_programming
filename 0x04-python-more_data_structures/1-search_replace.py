#!/usr/bin/python3
def search_replace(my_list, search, replace):

    my_newlist = my_list.copy()

    for i in range(len(my_newlist)):
        if my_newlist[i] == search:
            my_newlist[i] = replace

    return my_newlist
