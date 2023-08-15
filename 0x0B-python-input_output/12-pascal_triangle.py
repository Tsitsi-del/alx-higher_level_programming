#!/usr/bin/python3
"""
Function for pascal triangle
"""


def pascal_triangle(n):
    """
    returns list of lists of integers
    """
    if n <= 0:
        return []
    tri = []
    for x in range(n):
        rw = [1]
        if tri:
            p_rw = tri[-1]
            for k in range(len(p_rw) - 1):
                rw.append(p_rw[k] + p_rw[k + 1])
            rw.append(1)
        tri.append(rw)
    return tri
