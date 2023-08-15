#!/usr/bin/python3
"""
4-from_json_string.py
"""
import json


def from_json_string(my_str):
    """
    from_json_string - function that converts json to python
    Args:
        my_str: json string
    Return: python data structure
    """

    return json.loads(my_str)
