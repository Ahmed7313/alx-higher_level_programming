#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print()

# You can save this script as 8-uppercase.py in your repository
# Directory: 0x01-python-if_else_loops_functions
