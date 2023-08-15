#!/usr/bin/python3
"""
5-save_to_json_file.py
"""
import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file - function that writes to text file
    Args:
        my_obj: object
        filename: name of the file
    Return:
    """

    with open(filename, "w") as file_json:
        json.dump(my_obj, file_json)
