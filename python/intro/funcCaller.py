#!/usr/bin/python3.7

from func import square

# can import the whole namespace but in that case you'd have to say `func.square` when calling the function
#import func 

for i in range(4):
    print(f"The square of {i} is {square(i)}")

