#!/usr/bin/python3
"""module to detect the peak number in an list"""


def find_peak(list_of_integers):
    """function for detection of peak in a list"""
    if list_of_integers is None:
        return None

    max_no = None

    for nums in list_of_integers:
        if max_no is None or max_no < nums:
            max_no = nums

    return max_no
