#!/usr/bin/python3
"""
Class Base Test
"""


import os
import unittest
import json
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class TestBaseMehtods(unittest.TestCase):
    """
    tests fr Base class
    """
    def setUp(self):
        """
        run for each tests
        """
        Base._Base__nb_objects = 0
        self.new_base = Base(id=1)

    def tearDown(self):
        """
        clear up tests
        """
        pass

    def test_docstring(self):
        """
        test docstring is presnt
        """
        self.assertIsNotNone(Base.__doc__)

    def test_instnce_var(self):
        """
        check instance variables
        """
        self.assertEqual(self.new_base.id, 1)

    def test_random_args(self):
        """
        test random args passed
        """
        testa = Base(7)
        self.assertEqual(testa.id, 7)
        testb = Base(24)
        self.assertEqual(testb.id, 24)
        testc = Base()
        self.assertEqual(testc.id, 1)
        testd = Base(-15)
        self.assertEqual(testd.id, -15)

    def test_sequantial(self):
        """
        tests sequantial ids
        """
        bs1 = Base()
        bs2 = Base()
        self.assertEqual(bs1.id + 1, bs2.id)
