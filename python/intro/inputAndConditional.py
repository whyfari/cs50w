#!/usr/bin/python3.7

# name = input("Name? ")
name = "Fari"

print("hello, " + name)

# using formatted string
print(f"Hello, {name}")

# num = 3
num = int(input("Number: "))
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("zero")

if num < 0 and num > -20 and num % 2 != 0:
    print("Small negative odd number")


# reading in space sepearted
# x and y are strings
x, y = input().split()


# x and y are ints
x, y = map(int, input().split()

# ex input: 1 2 3 4 5 6 7 8 9
# bb is a list of ints
bb=list(map(int, input().split())
# bb is a  of ints
cc=set(map(int, input().split())
