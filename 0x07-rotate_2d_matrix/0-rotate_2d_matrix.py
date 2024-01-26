#!/usr/bin/python3
"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise.
Do not return anything. The matrix must be edited in-place.
You can assume the matrix will have 2 dimensions and will not be empty.
"""


def rotate_2d_matrix(matrix):
    """ rotata matrix """
    n = len(matrix)

    # Number of layers (outermost to innermost)
    layers = n // 2 if n % 2 == 0 else (n + 1) // 2

    for layer in range(layers):
        for i in range(layer, n - layer - 1):
            # Save the top element
            temp = matrix[layer][i]

            # Move left element to top
            matrix[layer][i] = matrix[n - i - 1][layer]

            # Move bottom element to left
            matrix[n - i - 1][layer] = matrix[n - layer - 1][n - i - 1]

            # Move right element to bottom
            matrix[n - layer - 1][n - i - 1] = matrix[i][n - layer - 1]

            # Move saved top element to right
            matrix[i][n - layer - 1] = temp
