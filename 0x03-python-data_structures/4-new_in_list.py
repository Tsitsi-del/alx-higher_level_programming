#!/usr/bin/python3
# 4-new_in_list.py

def new_in_list(my_list, idx, element):
    """Function that replaces an
    element in copied list at index"""
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    copy = list(my_list)
    copy[idx] = element
    return (copy)
