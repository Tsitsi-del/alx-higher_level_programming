#!/usr/bin/python3
"""Class named Square is defined"""


class Square:
    """function named __init__ defined"""
    def __init__(self, size=0):
        """if statement"""
        if type(size) != int:
            """raise error"""
            raise TypeError("size must be an integer")
        elif size < 0:
            """raise error"""
            raise ValueError("size must be >= 0")
        else:
            """initialize __size of size and self"""
            self.__size = size
