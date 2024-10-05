#!/usr/bin/python3

"""this module makes addition for two integer numbers """

def add_integer(a, b=98):
    """
    this function adds two integer or float numbers
    
    Args:
        a (int, float) : first supplied integer
        b (int, float) : second supplied integer
    
    Returns:
        addition of the two numbers
    
    Raises:
        TypeError: if the type of 'a' or 'b' is not integer/float
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))
