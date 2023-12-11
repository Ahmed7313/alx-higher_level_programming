#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print(" ".join("{:d}".format(elem) for elem in row))

if __name__ == "__main__":
    # This part is for testing and will not be executed when imported
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print_matrix_integer(matrix)
    print("--")
    print_matrix_integer()

