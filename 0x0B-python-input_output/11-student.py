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

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of Student instance
        """

        if type(attrs) is list and all([type(i) == str for i in attrs]):
            return {j: x for j, x in self.__dict__.items() if j in attrs}
        else:
            return self.__dict__.copy()

    def reload_from_json(self, json):
        """
        loads attributes from json
        """
        for key, value in json.tems():
            self.__dict__[key] = value
