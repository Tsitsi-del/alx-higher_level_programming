#!/usr/bin/python3
def number_keys(a_dictionary):
    res = 0
    key_list = list(a_dictionary.keys())

    for x in key_list:
        res += 1

    return (res)
