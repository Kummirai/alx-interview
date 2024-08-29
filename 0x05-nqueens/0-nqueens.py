#!/usr/bin/python3
"""Solves the N-queens puzzle.
Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.
Example:
    $ ./0-nqueens.py N
N must be an integer greater than or equal to 4.
Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.
Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""

import sys

def is_safe(board, row, col, n):
    """Check if a queen can be placed at position (row, col) on the board."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens(n, row, board):
    """Solve the N queens problem using backtracking."""
    if row == n:
        print_board(board)
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_n_queens(n, row + 1, board)

def print_board(board):
    """Print a solution to the N queens problem."""
    n = len(board)
    for row in range(n):
        for col in range(n):
            if board[row] == col:
                print('Q', end=' ')
            else:
                print('.', end=' ')
        print()

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [-1] * n
    solve_n_queens(n, 0, board)

if __name__ == "__main__":
    main()
    