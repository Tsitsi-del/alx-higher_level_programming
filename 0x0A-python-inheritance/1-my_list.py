#!/usr/bin/python3
"""
Class list that inherits from list
"""


class MyList(list):
    """
    class list inherits from list
    """

    def print_sorted(self):
        """
        print list in ascending order
        """
        my_list = self[:]
        my_list.sort()
        print(my_list)
