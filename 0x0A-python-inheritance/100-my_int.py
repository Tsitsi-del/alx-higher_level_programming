#!/usr/bin/python3
"""
Class MyInt
"""


class MyInt(int):
    """
    class MyInt
    """

    def __init__(self, x):
        """
        instances of class MyInt
        """
        self.__x = x

    def __eq__(self, other):
        """
        equal method
        """
        return self.__x != other

    def __ne__(self, other):
        """
        method not equal
        """
        return self.__x == other
