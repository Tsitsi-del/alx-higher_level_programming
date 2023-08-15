#!/usr/bin/python3
"""
    Class Student
"""


class Student:
    """
        Class Student defines student by:
        Attributes:
            first_name (str): student name
            last_name (str): student name
            age (int): student age
        Methods:
            __init__ - initializes Student instance
            to_json - retrieve dictionary of Student Instance
    """
    def __init__(self, first_name, last_name, age):
        """
            Initialize Student instance
        """
        self.first_name = first_ name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            Dictionary of student instance.
        """
        return self.__dict__
