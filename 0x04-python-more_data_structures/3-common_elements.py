#!/usr/bin/python3
def common_elements(set_1, set_2):
    # Return the intersection of set_1 and set_2
    return set_1 & set_2

# Testing the function with the provided example
if __name__ == "__main__":
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}
    c_set = common_elements(set_1, set_2)
    print(sorted(list(c_set)))

