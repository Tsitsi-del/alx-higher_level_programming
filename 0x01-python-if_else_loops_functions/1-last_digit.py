#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
dgit = abs(number) % 10
if number < 0:
    dgit = -dgit
print("Last digit of {} is {} and is".format(number, dgit), end="")
if dgit > 5:
    print(f"Last digit of {number:d} is {dgit:d} and is greater than 5")
elif dgit == 0:
    print(f"Last digit of {number:d} is {dgit} and is 0")
else:
    print(f"Last digit of {number:d} is {dgit:d} and is less than 6 and not 0")
