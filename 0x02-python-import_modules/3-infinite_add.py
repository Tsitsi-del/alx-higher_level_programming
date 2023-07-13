#!/usr/bin/python3

if __name__ == "__main__":
    """Function to print he addition of args"""
    import sys

    sum = 0
    for count in range(len(sys.argv) - 1):
        sum += int(sys.argv[count + 1])
    print("{}".format(sum))
