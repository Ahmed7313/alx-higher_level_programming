#!/usr/bin/python3

def print_last_digit(number):
    """
    Prints and returns the last digit of a number.
    """
    # Handle negative numbers by taking their absolute value
    last_digit = abs(number) % 10

    # Print the last digit
    print(last_digit, end='')

    # Return the last digit
    return last_digit
