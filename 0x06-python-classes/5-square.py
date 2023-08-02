#!/usr/bin/python3
"""class square defined"""


class Square:
    """__init__ function defined"""
    def __init__(self, size=0):
        """initializes size of self with size"""
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
            """initialize"""
            self.__size = value
    """define area function"""
    def area(self):
        """returns area"""
        return self.__size ** 2
    """define print function"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
