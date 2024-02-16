#!/usr/bin/python3
"""
returns a list of lists of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """ pascal's triangle """
    if n <= 0:
        return []

    result = []

    for i in range(n):
        row = [1] * (i + 1)
        result.append(row)

        for j in range(1, i):
            result[i][j] = result[i - 1][j - 1] + result[i - 1][j]

    return result
