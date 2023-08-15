#!/usr/bin//python3
"""
2-append_write.py
"""


def append_write(filename="", text=""):
    """
    append_write - function that appends text to UTF-8 file
    Args:
        filename: name of the file
        text: text to be written
    Return: number of characters added
    """

    with open(filename, "a", encoding="UTF-8") as file_utf:
        return (file_utf.write(text))
