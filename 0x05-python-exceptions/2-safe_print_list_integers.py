#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter_ = 0
    for item_ in range(0, x):
        try:
            print("{:d}".format(my_list[item_]), end="")
            counter_ += 1
        except (ValueError, TypeError):
            pass

    print("")
    return (counter_)
