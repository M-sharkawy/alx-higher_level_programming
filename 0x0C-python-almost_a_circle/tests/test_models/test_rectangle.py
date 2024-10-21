#!/usr/bin/python3
"""Test Rectangle class module"""
from io import StringIO
import sys
import unittest
from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):

    def tes_value(self):
        """test ...width
          height weather <= 0"""
        with self.assertRaises(ValueError):
            rs = Rectangle(-5, 10)
        with self.assertRaises(ValueError):
            rs2 = Rectangle(0, 10)
        with self.assertRaises(ValueError):
            rs3 = Rectangle(5, -10)
        with self.assertRaises(ValueError):
            rs4 = Rectangle(5, 0)

    def test_x_y_value(self):
        """test x y < 0"""
        with self.assertRaises(ValueError):
            result = Rectangle(5, 10, -5, 2)
        with self.assertRaises(ValueError):
            result2 = Rectangle(5, 10, 2, -4)

    def test_str_(self):
        """tests human...
          display fiunction (str)"""
        rctt = Rectangle(10, 12, 7, 8, 1)
        self.assertEqual(rctt.__str__(), "[Rectangle] (1) 7/8 - 10/12")

    def test_area(self):
        """test area"""
        rctt = Rectangle(10, 20)
        self.assertEqual(rctt.area(), 200)

    def test_type(self):
        """tests width height x y not int"""
        with self.assertRaises(TypeError):
            res = Rectangle(1.5, 15)
        with self.assertRaises(TypeError):
            res2 = Rectangle(15, 1.5)
        with self.assertRaises(TypeError):
            res3 = Rectangle(15, 15, 1.3, 2)
        with self.assertRaises(TypeError):
            res4 = Rectangle(15, 15, 1, 2.1)

    def test_display_x_y(self):
        """tests dispaly function with... only ..
        width and height ...and x and y"""
        rec = Rectangle(2, 4, 2, 1)
        output = StringIO()
        sys.stdout = output
        rec.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "\n  ##\n  ##\n  ##\n  ##\n")

    def test_args_update(self):
        """tests update ...
        function with *args......"""
        rc = Rectangle(10, 10, 10, 10)
        rc.update(92, 15, 20, 16, 12)
        msg = "[Rectangle] (92) 16/12 - 15/20"
        self.assertEqual(str(rc), msg)

    def test_kwargs_update(self):
        """tests udpate ....
        function with **kwargs......."""
        rc = Rectangle(10, 10, 10, 10)
        rc.update(id=13, x=15, y=12, width=5, height=8)
        msggg = "[Rectangle] (13) 15/12 - 5/8"
        self.assertEqual(str(rc), msggg)

    def test_to_dictionary(self):
        """tests ....
        to_dictionary function..........."""
        rec = Rectangle(10, 2, 1, 9, 1)
        rc_dictionary = rec.to_dictionary()
        expectd_dict = {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9}
        self.assertEqual(rc_dictionary, expectd_dict)

    def test_display(self):
        """tests dispaly/...
          function with 
          ...only width and height"""
        rc = Rectangle(2, 4)
        output = StringIO()
        sys.stdout = output
        rc.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "##\n##\n##\n##\n")

    def test_from_json_string_none(self):
        """tests from_json_string with none value........"""
        list_output = Rectangle.from_json_string(None)
        self.assertEqual(list_output, "[]")

    def test_from_json_string(self):
        """tests from_json_string function.........."""
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        expectd_output = [{"id": 89, "width": 10, "height": 4}]
        self.assertEqual(list_output, expectd_output)

    def test_json_string_empty(self):
        """tests from_json_string with ...... string"""
        list_output = Rectangle.from_json_string("[]")
        self.assertEqual(list_output, [])


if __name__ == "__main__":
    unittest.main()
