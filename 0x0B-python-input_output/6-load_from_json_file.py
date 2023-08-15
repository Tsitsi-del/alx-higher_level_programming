#!/usr/bin/python3
"""
6-load_from_json_file.py
"""
import json


def load_from_json_file(filename):
    """
    load_from_json_file - function that creates Object from json file
    Args:
        filename: name of file
    """

    with open(filename, "r") as file_json:
        my_object = json.load(file_json)
        return my_object
