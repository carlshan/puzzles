"""
Advent of Code 2021
Author: Carl Shan
Day 4
Problem: Play bingo
"""

advent_input = open("day4.in", "r")
data = advent_input.readlines()

numbers_drawn = data[0].strip().split(',')

remaining = data[2:]
remaining = [row for row in remaining if row != '\n']
all_boards = [remaining[i : i + 5] for i in range(0, len(remaining), 5)]

def clean_row_or_col(nums):
    """
    Returns a list of the integers that are in the row or column.
    """
    return [x for x in nums.strip().split(' ') if x != ""]

def get_rows_and_cols(board):
    """
    Given a board, return a list containing all rows and columns.
    """
    rows_and_cols = []
    cols = [[], [], [], [], []]
    # Getting all rows
    for row in board:
        cleaned = clean_row_or_col(row)
        rows_and_cols.append(cleaned)
        # Building up each column
        for i in range(len(cleaned)):
            cols[i].append(cleaned[i])

    # Getting all columns
    for col in cols:
        rows_and_cols.append(col)

    return rows_and_cols

def has_bingo(board, drawn):
    """
    Given a list of numbers that have been called, checks to see if this board has a bingo.
    """
    rows_and_cols = get_rows_and_cols(board)
    for r_or_c in rows_and_cols:
        num_called = 0
        for num in r_or_c:
            if num in drawn:
                num_called += 1
        if num_called == 5: # all 5 numbers were called
            return True

    return False


def find_first_board_with_bingo(boards, numbers_drawn):

    drawn = numbers_drawn[:4] # initializing to first four since we know those need to first happen

    for i in range(4, len(numbers_drawn)): # call numbers one at a time and check each board
        drawn.append(numbers_drawn[i])
        for board in boards:
            if has_bingo(board, drawn):
                return board, drawn

def find_last_board_with_bingo(boards, numbers_drawn):

    drawn = numbers_drawn[:4] # initializing to first four since we know those need to first happen
    all_bingos = []
    already_seen = []
    for i in range(4, len(numbers_drawn)): # call numbers one at a time and check each board
        drawn.append(numbers_drawn[i])
        for board in boards:
            if has_bingo(board, drawn) and board not in already_seen:
                all_bingos.append((board, drawn))
                already_seen.append(board)
        if len(already_seen) == len(boards): # we are done since all boards have seen bingo
            break

    return all_bingos[-1] # the one with the last bingo

# Part 1: This board wins first:
def part_1(all_boards, numbers_drawn):
    winner, numbers_drawn = find_first_board_with_bingo(all_boards, numbers_drawn)

    unmarked = set()
    for i in get_rows_and_cols(winner):
        for num in i:
            if num not in numbers_drawn:
                unmarked.add(num)

    print(sum(map(int, unmarked)) * int(numbers_drawn[-1]))

def part_2(all_boards, numbers_drawn):
    last_winner, numbers_drawn = find_last_board_with_bingo(all_boards, numbers_drawn)

    unmarked = set()
    for i in get_rows_and_cols(last_winner):
        for num in i:
            if num not in numbers_drawn:
                unmarked.add(num)

    print(sum(map(int, unmarked)) * int(numbers_drawn[-1]))