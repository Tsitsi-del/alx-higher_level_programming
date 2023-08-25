#!/usr/bin/python3
"""
Class Test_Rectangle
"""


from unittest.mock import patch
import unittest
import json
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleMethods(unittest.TestCase):
    """
    tests for Rectangle class
    """

    @classmethod
    def SetUp(self):
        """
        testing each method
        """
        Base._Base__nb_objects = 0

    def tearDown(self):
        """
        clean after each test
        """
        pass

    def test_docstring(self):
        """
        checking for doc string
        """
        self.assertIsNotNone(Rectangle.__doc__)

    def test_RectangleClass(self):
        """
        Rectangle class type
        """
        self.assertEqual(str(Rectangle),
                         "<class 'models.rectangle.Rectangle'>")

    def test_inheritance(self):
        """
        Rectangle class inherits from Base
        """
        self.assertTrue(issubclass(Rectangle, Base))

    def test_random_arg(self):
        """
        testing random args
        """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    def test_passed_args(self):
        """
        test for one or m=no arguments passed
        """
        with self.assertRaises(TypeError):
            Rectangle(10)
            Rectangle()

    def test_height_width_1(self):
        """
        width and height types test
        """
        with self.assertRaiseRegex(TypeError, "height must be an integer"):
            Rectangle(4, "Tsitsi")
            Rectangle(4, 't')
            Rectangle(True, 7)

        with self.assertRaiseRegex(TypeError, "width must be an integer"):
            Rectangle("Tsitsi", 6)
            Rectangle('s', 8)
            Rectangle(True, 7)

        with self.assertRaiseRegex(TypeError, "x must be an integer"):
            Rectangle(5, 4, "NK")
            Rectangle(5, 4, 'n')
            Rectangle(True, 7, 3)

        with self.assertRaiseRegex(TypeError, "y must be an integer"):
            Rectangle(5, 4, 7, "NK")
            Rectangle(5, 4, 3, 'n')
            Rectangle(True, 7, 3, 2)

    def test_width_height_2(self):
        """
        width and height range test
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-5, 3)
            Rectangle(0, 1)
            Rectangle(0, 4)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(3, -4)
            Rectangle(2, 0)
            Rectangle(4, 0)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(3, 5, -1)
            Rectangle(12, 3, 0)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 5, 4, -3)
            Rectangle(12, 3, 2, 0)

    def test_area_1(self):
        """
        Rectangle area
        """
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 2 * 3)
        self.assertEqual(r2.area(), 2 * 10)
        self.assertEqual(r3.area(), 8 * 7)

    def test_display(self):
        """
        display test
        """
        r1 = Rectangle(4, 6)
        res = "####\n####\n####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as str_output:
            r1.display()
            self.assertEqual(str_output.getvalue(), res)

    def test_str(self):
        """
        Testing __str__
        """
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1)
        res = "[Rectangle] (12) 2/1 - 4/6\n"
        res2 = "Rectangle] (1) 1/0 - 5/5"
        self.assertEqual(r2.__str__(), res2)
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

    def test_update_arg(self):
        """
        Test update method with args
        """
        r = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 1/1")
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 2/1")
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 2/3")
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/0 - 2/3")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")
