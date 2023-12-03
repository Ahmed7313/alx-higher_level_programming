#!/usr/bin/python3

def print_reversed_alphabet():
    alpha_string = ""
    for i in range(122, 96, -1):
        alpha_string += chr(i - 32) if i % 2 == 0 else chr(i)
    print("{}".format(alpha_string), end='')

print_reversed_alphabet()
