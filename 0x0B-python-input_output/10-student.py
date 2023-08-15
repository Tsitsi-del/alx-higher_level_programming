#!/usr/bin/python3
"""
Function for class student
"""


class Student:
    """
    Student class
    """
    def __init__(self, first_name, last_name, age):
        """
        instance attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attribute=None):
        """
        retrieves a dictionary representation of Student instance
        """

        if attribute is not None:
            result = {i: self.__dict__[i] for i in self.__dict__.keys() & attribute}
            return result
        else:
            return self.__dict__
