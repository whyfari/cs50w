#!/usr/bin/python3.7

import sys   

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Caught exception ValueError: invalid input")
    sys.exit(1)

try:
    result = x/y
except ZeroDivisionError:
    print("Caught exception ZeroDivisionError: cannot divide by 0")
    sys.exit(1)


print(result)


