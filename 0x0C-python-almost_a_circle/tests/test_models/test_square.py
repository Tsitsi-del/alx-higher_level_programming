#!/usr/bin/python3
"""
Class Test Square
"""


from unittest.mock import patch
import unittest
import json
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class TestSquareMethods(unittest.TestCase):
    """
    tests for Square Class
    """

    def SetUp(self):
        """
        invoked for each test
        """
        Base._Base__nb_objects = 0

    def tesarDown(self):
        """
        Cleans after each test
        """
        pass

    def test_nw_square(self):
        """
        test new square
        """
        sq1 = Square(3)
        sq2 = Square(1, 2, 3, 4)
        self.assertEqual(sq1.size, 3)
        self.assertEqual(sq1.width, 3)
        self.assertEqual(sq1.x, 0)
        self.assertEqual(sq1.y, 0)
        self.assertEqual(sq1.id, 1)
        self.assertEqual(sq2.size, 1)
        self.assertEqual(sq2.width, 1)
        self.assertEqual(sq2.x, 2)
        self.assertEqual(sq2.y, 3)
        self.assertEqual(sq2.id, 4)

    def test_attribute(self):
        """
        Test width, x and y types
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")

    def test_constructor_args(self):
        """
        tests constructor with no arguments
        """
        with self.assertRaises(TypeError) as e:
            r = Square()
        sq = "__init__() missing required positional arguments: 'size'"
        self.assertEqual(str(e.exception), sq)

    def test_Rectangle_instance(self):
        """
        test class Square is Rectangle instance
        """
        sq1 = Square(1)
        self.assertEqual(True, isinstance(sq1, Rectangle))

    def test_area(self):
        """
        area method
        """
        sq1 = Square(4)
        self.assertEqual(sq1.area(), 16)

    def test_area_1(self):
        """
        test area after modfying size
        """
        sq1 = Square(4)
        self.assertEqual(sq1.area(), 16)
        sq1.size = 9
        self.assertEqual(sq1.area(), 81)

    def test_load_from_file(self):
        """
        test load json file
        """
        load_file = Square.load_from_file()
        self.assertEqual(load_file, load_file)

    def test_display_args(self):
        """
        test display with no args
        """
        sq1 = Square(9)
        with self.assertRaises(TypeError) as e:
            Square.display()
        s = "display() missing 1 required positional argumbent: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_str(self):
        """
        testing __str__
        """
        sq1 = Square(3, 1, 3)
        res = "Square] (1) 1/3 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_ot:
            print(sq1)
            self.assertEqual(str_ot.getvalue(), res)
