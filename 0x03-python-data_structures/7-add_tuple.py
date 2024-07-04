#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least two elements, padding with 0 if needed
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    # Add the corresponding elements of the tuples
    return tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]

if __name__ == "__main__":
    # This part is for testing and will not be executed when imported
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)

    print(add_tuple(tuple_a, (1, )))
    print(add_tuple(tuple_a, ()))

