#!/usr/bin/python3
"""class square defined"""


class Square:
    """represents a square
    Attributes:
        __size (int): size of a size of square
        __position (tuple): position of square in 2D space"""

    def __init__(self, size=0, position=(0, 0)):
        """initializes square
        Args:
            size (int): size of side of square
            position (tuple): position of square
        Returns:
            None"""
        self.size = size
        self.position = position

    def area(self):
        """square area function
        Returns:
            area of the square"""
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size
        Returns:
            size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): size of side of square
        Returns:
            None"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        """print square
        Returns:
            None"""
        if self.__size == 0:
            print()
            return
        for x in range(self.__position[1]):
            print()
            for i in range(self.__size):
                print("".join([" " for j in range(self.__position[0])]), end="")
                print("".join(["#" for k in range(self.__size)]))

    @property
    def position(self):
        """getter of __position
        Returns:
            position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter of __position
        Args:
            value (tuple): position of square
        Returns:
            None"""
        if type(value) is not tuple or len(value) != 2 or \
                type(value[0]) is not int or value[0] < 0 or \
                type(value[1]) is not int or value[1] < 0:
                    raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
