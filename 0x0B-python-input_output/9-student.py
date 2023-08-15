#!/usr/bin/python3
"""
    Class Student
"""


class Student:
    """
        Class Student
        Attributes:
            first_name (str): student name.
            last_name (str): last name of student.
            age (int): student age.
        Methods:
            __init__ - initialize student instance.
            to_json - dictionary of student instance.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_ name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Dictionary of student instance.
        """
        return self.__dict__
