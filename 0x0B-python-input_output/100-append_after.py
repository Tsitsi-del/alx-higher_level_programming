#!/usr/bin/python3
"""
Function append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """
    method inserting text after searching string
    """
    file_lines = []
    with open(filename, "r", encoding="utf-8") as file_n:
        file_lines = file_n.readlines()
        x = 0
        while x < len(file_lines):
            if search_string in file_lines[x]:
                file_lines[x:x + 1] = [file_lines[x], new_string]
                x += 1
            x += 1
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(file_lines)
