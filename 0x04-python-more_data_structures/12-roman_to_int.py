#!/usr/bin/python3
def roman_to_int(roman_string):
    # Check if input is a string and not None
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    # Map of Roman numerals to their integer values
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}

    # Initialize the previous value and total
    prev_value = 0
    total = 0

    # Iterate over each character in the string, in reverse order
    for char in roman_string[::-1]:
        # Convert the Roman numeral to its integer value
        value = roman_map.get(char, 0)

        # If the current value is less than the previous value,
        # subtract it from the total, otherwise add it
        if value < prev_value:
            total -= value
        else:
            total += value

        # Update the previous value
        prev_value = value

    return total

# Testing the function with the provided examples
if __name__ == "__main__":
    roman_to_int = __import__('12-roman_to_int').roman_to_int

    roman_number = "X"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "VII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "IX"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "LXXXVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "DCCVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))
