#!/usr/bin/python3
"""test module for square class
    square test cases module"""

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
            sq = Square("martino")

    def test_size_less_than_or_equal_zero(self):
        with self.assertRaises(ValueError):
            sq = Square(-10)

        with self.assertRaises(ValueError):
            sq = Square(0)

    def test_str_(self):
        sq = Square(5, 3, 4, 1)
        self.assertEqual(sq.__str__(), "[Square] (1) 3/4 - 5")

    def test_display(self):
        sq = Square(2)
        sq.display()
        self.assertEqual(self.output.getvalue(), "##\n##\n")

    def test_to_dictionary(self):
        sq = Square(5, 3, 4, 1)
        expected_dict = {"id": 1, "size": 5, "x": 3, "y": 4}
        self.assertEqual(sq.to_dictionary(), expected_dict)


if __name__ == "__main__":
    unittest.main()
