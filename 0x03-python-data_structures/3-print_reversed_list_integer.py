#!/usr/bin/python3
# 3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    """Function to print a list in reverse"""
    if my_list:
        my_list.reverse()
        for x in range(0, len(my_list)):
            print("{:d}".format(my_list[x]))
