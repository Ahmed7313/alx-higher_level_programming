#!/bin/python3
def square_matrix_simple(matrix):
  squared_matrix = [[0] * len(matrix) for _ in range(len(matrix[0]))]

  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      squared_matrix[i][j] = matrix[i][j] ** 2

  return squared_matrix
