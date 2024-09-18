#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or Type(roman_string) != str:
        return 0

    nums = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    summ = 0

    for index in range(len(roman_string)):
        value = nums[roman_string[index]]
        if index + 1 < len(roman_string) and nums[roman_string[index + 1]] > value:
            summ -= value
        else:
            summ += value
    return summ
