#!usr/bin/python3
"""square test cases module"""
from models.square import Square
from models.base import Base
import sys
import unittest
from io import StringIO

class SquareTest(unittest.TestCase):
    """Class for testing square module"""

    def setUp(self):
        Base._Base__nb_objects = 0
        self.output = StringIO()
        sys.stdout = self.output

    def test_size_non_int(self):
        with self.assertRaises(TypeError):
            lol = Square("momo")

    def test_size_less_than_or_equal_zero(self):
        with self.assertRaises(ValueError):
            lol = Square(-7)

        with self.assertRaises(ValueError):
            oll = Square(0)

    def test_display(self):
        lol = Square(2)
        lol.display()
        self.assertEqual(self.output.getvalue(), "##\n##\n")

    def test_str_(self):
        lol = Square(7, 3, 6, 1)
        self.assertEqual(lol.__str__(), "[Square] (1) 3/6 - 7")

    def test_to_dictionary(self):
        lol = Square(6, 3, 2, 1)
        expected_dict_ = {"id": 1, "size": 6, "x": 3, "y": 2}
        self.assertEqual(lol.to_dictionary(), expected_dict_)
