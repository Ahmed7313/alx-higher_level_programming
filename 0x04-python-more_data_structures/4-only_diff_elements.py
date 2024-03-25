#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Use set symmetric difference to find elements in either set but not in both
    return set_1 ^ set_2

# Testing the function with the provided example
if __name__ == "__main__":
    set_1 = { "Python", "C", "Javascript" }
    set_2 = { "Bash", "C", "Ruby", "Perl" }
    od_set = only_diff_elements(set_1, set_2)
    print(sorted(list(od_set)))

