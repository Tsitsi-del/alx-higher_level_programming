#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    key_list = list(new_dict.keys())

    for x in key_list:
        new_dict[x] *= 2

    return (new_dict)
