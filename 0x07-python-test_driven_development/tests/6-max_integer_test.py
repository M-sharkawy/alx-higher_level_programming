#!/usr/bin/python3

"""Module to find the max integer in a list
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    This is the class unittest for the max integer function
    """

    def test_sorted_list(self):

       sorted_list = [2, 3, 4, 5]
       self.assertEqual(max_integer(sorted_list), 5)

    def test_unsorted_list(self):

        unsorted_list = [1, 5, 3, 4]
        self.assertEqual(max_integer(unsorted_list), 5)

    def test_empty_list(self):

        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_floatlist(self):

        floatlist = [1.25, 2.33, 3.67, 4.44]
        self.assertEqual(max_integer(floatlist), 4.44)

    def test_intl_floatl(self):

        intl_floatl = [1.25, 4.44, 4, 5]
        self.assertEqual(max_integer(intl_floatl), 5)

    def test_only_one(self):

        only_one_ = [8]
        self.assertEqual(max_integer(only_one_), 8)

    def test_max_first(self):

        max_first = [9, 1, 5, 3]
        self.assertEqual(max_integer(max_first), 9)

    def test_max_middle(self):

        max_middle = [10, 33, 55, 3]
        self.assertEqual(max_integer(max_middle), 55)

    def test_non_string(self):

        self.assertEqual(max_integer(""), None)

    def test_many_strings(self):

        many_strings = ["string1", "string2", "string3"]
        self.assertEqual(max_integer(many_strings), "string3")

if __name__ == '__main__':
    unittest.main()
