#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Use a list comprehension to iterate over each element in my_list
    # Replace the element with 'replace' if it matches 'search', else keep it unchanged
    return [replace if x == search else x for x in my_list]

# Testing the function with the provided example
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
    new_list = search_replace(my_list, 2, 89)

    print(new_list)
    print(my_list)  # This should print the original list unchanged
    
