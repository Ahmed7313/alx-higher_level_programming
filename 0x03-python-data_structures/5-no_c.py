#!/usr/bin/env python3
def no_c(my_string):
    return ''.join(ch for ch in my_string if ch not in ['c', 'C'])

if __name__ == "__main__":
    # This part is for testing and will not be executed when imported
    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))

