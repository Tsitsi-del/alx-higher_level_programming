#!/usr/bin/python3
# 7-add_tuple.py

def add_tuple(tuple_a=(), tuple_b=()):
    """Function that adds two tuples"""
    sum_tuple = ()
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    sum_tuple = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return sum_tuple
