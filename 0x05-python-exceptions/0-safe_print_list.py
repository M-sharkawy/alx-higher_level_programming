#!/usr/bin/python3

'''function that prints x elements of a list'''

def safe_print_list(my_list=[], x=0):
        index = 0

        try:
            for item_ in my_list:
                if index < x:
                    print(item_, end="")
                    index += 1
        except IndexError:
                pass
        finally:
                print("\n")
        
        return (index)
