"""
Puzzle:
Find an arrangement on a 5x5 board where you can put 5 queens and have at least
3 empty spots.

This solution is a brute force method of finding the position of the board that
satisfies the above conditions.
"""

import numpy as np
import random

DEBUG = False


def is_empty(board, pos):
    """
    Checks if a board position is empty.
    """
    return board[pos] == 0


def pick_empty_position(board, rows, cols):
    pos = None
    while not pos:
        test_pos = (random.choice(rows), random.choice(cols))
        if is_empty(board, test_pos):
            pos = test_pos
    return pos


def eval_conds(pos1, pos2, pos3, pos4, pos5):
    cond1 = pos1 == (-1, -1)
    cond2 = pos2 == (-1, -1)
    cond3 = pos3 == (-1, -1)
    cond4 = pos4 == (-1, -1)
    cond5 = pos5 == (-1, -1)
    return cond1, cond2, cond3, cond4, cond5


def evaluate_board(board, n):
    """
    Returns the total 0s in the board
    """
    size = board.size
    success = size - board.sum() >= n
    total_0s = size - board.sum()
    return success, total_0s


def update_cell(pos, board):
    board[pos] = 1


def update_row(pos, board):
    board[pos[0], :] = 1


def update_col(pos, board):
    board[:, pos[1]] = 1


def update_bottom_left(row, col, board):
    if row > 4 or col > 4 or row < 0 or col < 0:
        return
    else:
        board[row, col] = 1
        update_bottom_left(row+1, col-1, board)


def update_bottom_right(row, col, board):
    if row > 4 or col > 4 or row < 0 or col < 0:
        return
    else:
        board[row, col] = 1
        update_bottom_right(row+1, col+1, board)


def update_top_left(row, col, board):
    if row > 4 or col > 4 or row < 0 or col < 0:
        return
    else:
        board[row, col] = 1
        update_top_left(row-1, col-1, board)


def update_top_right(row, col, board):
    if row > 4 or col > 4 or row < 0 or col < 0:
        return
    else:
        board[row, col] = 1
        update_top_right(row-1, col+1, board)


def update_diag(pos, board):
    """
    Updates diagonals
    """
    row = pos[0]
    col = pos[1]
    update_bottom_left(row+1, col-1, board)
    update_bottom_right(row+1, col+1, board)
    update_top_left(row-1, col-1, board)
    update_top_right(row-1, col+1, board)


def update_all_cells(positions, board):
    """
    Updates all cells of the board based on the positions
    """
    for pos in positions:
        update_row(pos, board)
        update_col(pos, board)
        update_diag(pos, board)

rows = range(0, 5)
cols = range(0, 5)


def main():
    SUCCESS = False
    loop = 0
    while not SUCCESS:
        # Picks 5 different positions for the Queen
        board = np.zeros(shape=(5, 5))
        pos1 = pick_empty_position(board, rows, cols)
        update_cell(pos1, board)
        pos2 = pick_empty_position(board, rows, cols)
        update_cell(pos2, board)
        pos3 = pick_empty_position(board, rows, cols)
        update_cell(pos3, board)
        pos4 = pick_empty_position(board, rows, cols)
        update_cell(pos4, board)
        pos5 = pick_empty_position(board, rows, cols)
        update_cell(pos5, board)

        positions = [pos1, pos2, pos3, pos4, pos5]

        # Updates each of the rows, columns and diags for each queen
        update_all_cells(positions, board)

        # Checks to see if there are 3 empty positions
        SUCCESS, total_0s = evaluate_board(board, 3)
        loop += 1
        print("Round {}: {}".format(loop, total_0s))

    return positions, board

if __name__ == "__main__":
    if not DEBUG:
        positions, board = main()
        print(positions)
        print(board)
