#!/usr/bin/python3
"""N Queens problem solver."""


import sys


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve(board, col):
    """Recursive function to solve N Queens problem."""
    # Base case: If all queens are placed, return True
    if col >= N:
        return True

    # Consider this column and try placing this queen in all rows
    for i in range(N):
        if is_safe(board, i, col):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recur to place rest of the queens
            if solve(board, col + 1):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove queen from board[i][col]
            board[i][col] = 0

    # If the queen can't be placed in any row in this column, then return False
    return False


def print_solution(board):
    """Print the solution."""
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print("[{}, {}]".format(i, j), end=" ")
    print()


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: {} N".format(sys.argv[0]))
        sys.exit(1)

    # Get the value of N from the command line argument
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the chessboard
    board = [[0] * N for _ in range(N)]

    # Solve the N Queens problem
    if not solve(board, 0):
        print("No solution exists")
    else:
        # Print all possible solutions
        for solution in board:
            print_solution(solution)

