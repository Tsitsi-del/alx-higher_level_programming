#!/usr/bin/python3
"""
Function inherits_from
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance
    if a class that inherited from a class
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
