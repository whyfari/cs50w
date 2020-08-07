#!/usr/bin/python3.7

# DECORATOR

# a python is a value alike any other, functional programming paradigm
# decorators take a function as input and returns a modified function as output

def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function...")
    return wrapper

@announce
def hello():
    print("Hello world")

hello()
