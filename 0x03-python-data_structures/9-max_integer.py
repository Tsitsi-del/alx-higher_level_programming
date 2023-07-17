#!/usr/bin/python3
def max_integer(my_list=[]):
    """Function to find max in list"""
    if len(my_list) == 0:
        return (None)
    mx = my_list[0]
    for x in range(len(my_list)):
        if my_list[x] > mx:
            mx = my_list[x]
    return (mx)
