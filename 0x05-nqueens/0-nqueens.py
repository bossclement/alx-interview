#!/usr/bin/python3
import sys

""" N Queens placement on NxN chessboard """


def n_queen(t_arr, arr, col, i, num):
    """
       n_queen - Find all posibles solution for N-queen problem and return it
             in a list
       @t_arr: temporaly list to store the all points of a posible solution
       @arr: store all the solution
       @col: save a colum use for a queen
       @i: the row of the chess table
       @num: Number of queens
    """
    if (i > num):
        arr.append(t_arr[:])
        return arr

    for j in range(num + 1):
        if i == 0 or ([i - 1, j - 1] not in t_arr and
                      [i - 1, j + 1] not in t_arr and
                      j not in col):
            if i > 1:
                dia = 0
                for k in range(2, i + 1):
                    if ([i - k, j - k] in t_arr) or ([i - k, j + k] in t_arr):
                        dia = 1
                        break
                if dia:
                    continue
            t_arr.append([i, j])
            col.append(j)
            n_queen(t_arr, arr, col, i + 1, num)
            col.pop()
            t_arr.pop()

    return arr


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        num = int(sys.argv[1])
    except BaseException:
        print("N must be a number")
        exit(1)

    if not isinstance(num, int):
        print("N must be a number")
        exit(1)

    elif num < 4:
        print("N must be at least 4")
        exit(1)

    n_queen_arr = n_queen([], [], [], 0, num - 1)
    for i in n_queen_arr:
        print(i)
