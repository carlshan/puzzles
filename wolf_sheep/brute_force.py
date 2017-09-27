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


def is_empty(pos, board):
    """
    Checks if a board position is empty.
    """
    return board[pos] == 0


def pick_empty_position(board, rows, cols):
    """
    Finds an empty position and fills it in
    """
    pos = None
    while not pos:
        test_pos = (random.choice(rows), random.choice(cols))
        if is_empty(test_pos, board):
            pos = test_pos
            board[test_pos] = 1
    return pos


def evaluate_board(board, n):
    """
    Returns the total 0s in the board
    """
    size = board.size
    success = size - board.sum() >= n
    total_0s = size - board.sum()
    return success, total_0s


def update_row(pos, board):
    """
    Fills in the row of a position
    """
    board[pos[0], :] = 1


def update_col(pos, board):
    """
    Fills in the col of a position
    """
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
    Updates diagonals of a position
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


def pretty_format(positions, board):
    """
    Prints the board to reveal where the wolves are placed.
    """

    # TODO: This is still pretty ugly. I should pretty-fy it.
    str_board = np.array(board, dtype=str)
    for pos in positions:
        str_board[pos] = ' Q '
    return str_board

def replace_with_char(board, char):
    """
    This just replaces 1.0 and 0.0 with the value char
    """
    for row in board:
        for index in range(0, len(row)):
            value = row[index]
            if value != ' Q ':
                row[index] = ' X '
    return board

def main():
    """
    This does the main searching over all the positions.
    TODO: Make this less random to actually brute force things.
    """
    SUCCESS = False
    loop = 0
    rows = range(0, 5)
    cols = range(0, 5)

    while not SUCCESS:
        board = np.zeros(shape=(5, 5))
        positions = []
        # Picks 5 different positions for the Queen
        for i in range(0, 5):
            positions.append(pick_empty_position(board, rows, cols))

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
        pretty_positions = ', '.join(map(lambda tup: str(tup), positions))
        print("The positions of the five wolves are: " + pretty_positions)
        pretty_board = pretty_format(positions, board)
        print('---'*8)
        for row in replace_with_char(pretty_board, 'X'):
            print('| '  + ' '.join(row) + ' |')
        print('---'*8)
