#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ord_list = list(a_dictionary.keys())
    ord_list.sort()

    for x in ord_list:
        print("{}: {}".format(x, a_dictionary.get(x)))
