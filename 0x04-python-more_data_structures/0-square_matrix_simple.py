#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Use a list comprehension to iterate through rows of the matrix
    # For each row, iterate through its elements and square each element
    # Resulting structure is a new matrix with squared values
    return [[x**2 for x in row] for row in matrix]

# Testing the function with the provided example
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)  # The original matrix should remain unchanged
