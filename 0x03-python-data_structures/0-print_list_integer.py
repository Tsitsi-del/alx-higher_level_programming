#!usr/bin/python3
# 0-print_list_integer.py

def print_list_integer(my_list=[]):
    """Function printing integers in list"""
    for x in range(len(my_list)):
        print("{:d}".format(my_list[x]))
