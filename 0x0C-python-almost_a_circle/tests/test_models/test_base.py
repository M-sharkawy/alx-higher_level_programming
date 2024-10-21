#!/usr/bin/python3

"""module for unittesting of base class methods"""


import unittest
from models.base import Base
import json

class Test_base(unittest.TestCase):
    """tests for base class"""
    def setUp(self):
        Base.__nb_objects(0)

    def test_input_id(self):
        INS = Base(12)
        self.assertEqual(INS.id, 12)

    def test_nb_objects_id(self):
        INS1 = Base()
        INS2 = Base()
        INS3 = Base()
        self.assertEqual(INS1.id, 1)
        self.assertEqual(INS2.id, 2)
        self.assertEqual(INS3.id, 3)

    def test_combined_id(self):
        INS1 = Base()
        INS2 = Base(23)
        INS3 = Base()
        self.assertEqual(INS1.id, 1)
        self.assertEqual(INS2.id, 23)
        self.assertEqual(INS3.id, 2)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            INS = Base(1, 2)  # type: ignore

    def test_sets_negative_id(self):
        INS = Base(-7)
        self.assertEqual(INS.id, -7)

    def test_to_json(self):
        input = [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]
        expected = json.dumps(input)
        self.assertEqual(Base.to_json_string(input), expected)

    def test_to_json_empty(self):
        input = []
        expected = "[]"
        self.assertEqual(Base.to_json_string(input), expected)

    def test_to_json_none(self):
        input = None
        expected = "[]"
        self.assertEqual(Base.to_json_string(input), expected)

if __name__ == "__main__":
    unittest.main()
