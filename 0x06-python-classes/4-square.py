#!/usr/bin/python3
"""class square defined"""


class Square:
    """__init__ function is defined"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """returns __size of self"""
        return self.__size

    @size.setter
    def size(self, value):
        """if statement"""
        if type(value) is not int:
            """raise error"""
            raise TypeError("size must be an integer")
        elif value < 0:
            """raise error"""
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """defines area function"""
        return self.__size ** 2
