#!/usr/bin/python3
"""
Function add_attribute
"""


def add_attribute(obj, name, val):
    """
    add new attribute to an object
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, val)
