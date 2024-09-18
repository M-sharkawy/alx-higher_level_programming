#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    nums = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    total = 0
    for idx in range(len(roman_string)):
        value = nums[roman_string[idx]]
        if idx + 1 < len(roman_string) and nums[roman_string[idx + 1]] > value:
            total -= value
        else:
            total += value
    return total
