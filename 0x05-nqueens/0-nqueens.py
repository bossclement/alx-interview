#!/usr/bin/python3
import sys

""" N Queens placement on NxN chessboard """


def is_safe(board, row, col):
    """Check if it is safe to place a queen at board[row][col]
    Check for queens in the same column"""

    for i in range(row):
        if board[i] == col:
            return False

    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1

    i = row - 1
    j = col + 1
    while i >= 0 and j < N:
        if board[i] == j:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(N):
    """Initialize an empty board"""

    board = [-1] * N
    solutions = []

    def backtrack(row):
        if row == N:
            solutions.append(list(enumerate(board)))
            return

        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)

    backtrack(0)

    for solution in solutions:
        print(solution)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])

        if N < 4:
            print("N must be at least 4")
            sys.exit(1)

        solve_nqueens(N)

    except ValueError:
        print("N must be a number")
        sys.exit(1)
