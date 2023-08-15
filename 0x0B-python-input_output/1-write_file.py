#!/usr/bin/python3
"""
1-write_file.py
"""


def write_file(filename="", text=""):
    """
    write_file - function that writes a string to file UTF-8
                returns the number of characters
    Args:
        filename: name of file
        text: text to be written
    Return: number of bytes
    """

    with open(filename, "w", encoding="UTF-8") as file_utf:
        return (file_utf.write(text))
