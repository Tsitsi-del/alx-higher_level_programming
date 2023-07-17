#!/usr/bin/python3
# 5-no_c.py

def no_c(my_string):
    """Function that remove c and C from a string"""
    return my_string.translate({ord(x): None for x in 'cC'})
