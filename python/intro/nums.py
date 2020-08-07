#!/usr/bin/python3.7

def print_formatted(number):
    for i in range(1, number+1):

        # numbesr are okay but isn't aligned properly
        # print(i+1, oct(i+1).lstrip("0o").rstrip("L"), hex(i+1).lstrip("0x").rstrip("L"), bin(i+1).lstrip("0b").rstrip("L"))

        width = len("{0:b}".format(number))
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(
            i, width=width))


print("print 1-5 in dec, oct, hex, bin")
print_formatted(5)
