#!/usr/bin/python3
"""
Class_to_json_method
"""


def class_to_json(obj):
    """
    dictionary representation
    """
    json_dict = obj.__dict__
    return json_dict
