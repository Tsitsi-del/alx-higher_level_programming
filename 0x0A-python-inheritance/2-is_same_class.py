#!/usr/bin/python3
"""
Function is_same_class
"""


def is_same_class(obj, a_class):
    """
    Return true if object is exactly an
    instance of class otherwise false
    """
    return type(obj) == a_class
