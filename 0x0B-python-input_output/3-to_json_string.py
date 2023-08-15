#!/usr/bin/python3
"""
3-to_json_string.py
"""


def to_json_string(my_obj):
    """
    to_json_string - function that returns json
    represantion of string
    Args:
        my_obj: string to represent json
    Returns: json representation of string
    """

    return json.dumps(my_obj)
