#!/usr/bin/python3

"""
Usage: nqueens N
If the user called the program with the wrong number of arguments,
print Usage: nqueens N, followed by a new line, and exit with the status 1
where N must be an integer greater or equal to 4

If N is not an integer, print N must be a number, followed by a new line,
and exit with the status 1
If N is smaller than 4, print N must be at least 4, followed by a new line,
and exit with the status 1

The program should print every possible solution to the problem
One solution per line
You don’t have to print the solutions in a specific order

You are only allowed to import the sys module
"""


import sys


def square_is_safe(board, row, col, n):
    """
    function checks if a square's column and its diagonals
    are free from any queen
    """
    # check for queen in same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    # check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    return True


def solve_nqueens(n):
    """
    function ensures input is at least 4 (a min of 4 queens is needed).
    it proceeds to create an empty list of lists filled with *, that will
    be replaced with queen placements solutions.
    function then calls the utility func to start the recursive backtracking
    """
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_nqueens_utils(board, 0, n, solutions)
    for sol in solutions:
        print(sol)


def solve_nqueens_utils(board, row, n, solutions):
    """
    This utility function handles the backtracking. it prints the solution
    when row == n. otherwise, it places a queen in each column of the current
    row, checks if its safe, and then recurs to the next row. if the placement
    doesnt lead to a solution, it backtracks by resetting the position
    and trying the next column
    """
    if row == n:
        solutions.append([[i, j] for i in range(n) for j in range(
                         n)if board[i][j] == 1])
        return
    for col in range(n):
        if square_is_safe(board, row, col, n):
            board[row][col] = 1
            solve_nqueens_utils(board, row + 1, n, solutions)
            board[row][col] = 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)
