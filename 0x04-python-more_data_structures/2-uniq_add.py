#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Convert the list to a set to remove duplicates, then sum the unique elements
    return sum(set(my_list))

# Testing the function with the provided example
if __name__ == "__main__":
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))

