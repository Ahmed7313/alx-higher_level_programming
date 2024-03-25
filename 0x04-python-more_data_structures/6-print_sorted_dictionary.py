#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Iterate through the sorted keys of the dictionary
    for key in sorted(a_dictionary.keys()):
        # Print the key and its corresponding value
        print(f"{key}: {a_dictionary[key]}")

# Testing the function with the provided example
if __name__ == "__main__":
    a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
    print_sorted_dictionary(a_dictionary)

