#!/usr/bin/python3
# 12-fizzbuzz.py
def fizzbuzz():
    """Print numbers 1 to 100
    seperated by space, nultiple of three
    print Fizz and multple of five, print Buzz
    for multiple of both three and five, print FizzBuzz"""
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz ", end="")
        elif num % 3 == 0:
            print("Fizz ", end="")
        elif num % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(num), end="")
