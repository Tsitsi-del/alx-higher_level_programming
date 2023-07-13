#!/usr/bin/pyhton3
# 4-print_hexa.py
"""Print numbers 0 to 98 in
hexadecimal and decimal"""
for number in range(0, 99):
    print("{} = {}".format(number, hex(number)))
