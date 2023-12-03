#!/usr/bin/python3

def print_reversed_alphabet():
    alpha_string = ""
    for i in range(122, 96, -1):
        if i % 2 == 0:  # Even ASCII values are uppercase (after conversion)
            alpha_string += chr(i - 32)
        else:  # Odd ASCII values are lowercase
            alpha_string += chr(i)
    print(alpha_string, end='')

print_reversed_alphabet()
