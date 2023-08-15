#!/usr/bin/python3


def read_file(filename=""):
    """
    read_file - function that read a text file UTF-8
    Args:
        filename: name of the file
    """

    with open(filename, "r", encoding="UTF-8") as f:
        file_contents = f.read()
        for line in file_contents:
            print(line, end="")
