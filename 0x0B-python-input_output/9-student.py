#!/usr/bin/python3
"""
Class Student
"""


class Student:
    """
        Class Student
    """
        def __init__(self, first_name, last_name, age):
            """
                Student instance
            """
            self.first_name = first_ name
            self.last_name = last_name
            self.age = age

        def to_json(self):
            """
                Dictionary of student insatnce
            """
            return self.__dict__
