#!/usr/bin/python3
"""class square is defined"""


class Square:
    """__init__ function is defined"""
    def __init__(self, size=0):
        """if statement"""
        if type(size) is not int:
            """raise error"""
            raise TypeError("size must be an integer")
        elif size < 0:
            """raise error"""
            raise ValueError("size must be >= 0")
        else:
            """initialize"""
            self.__size = size
    """area function defined"""
    def area(self):
        """returns area"""
        return self.__size ** 2
