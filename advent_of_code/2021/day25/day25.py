"""
Advent of Code 2021
Author: Carl Shan
Day 25: Sea Cucumber
"""

data = open('day25.in', 'r').read().strip().split('\n')
cucumbers = [list(row) for row in data]

def move_cucumbers(cucumbers):
    """
    Move the cucumbers.
    Cucumbers 'v' move down (and wrap around)
    Cucumbers '>' move to the right (and wrap around)

    '>' cucumbers move first, and then 'v'.

    A cucumber can only move if there are no other cucumbers blocking them.
    """

    # Move '>' cucumbers first, then 'v' cucumbers.
    can_move_east = set()
    num_cols = len(cucumbers[0])
    num_rows = len(cucumbers)
    for row in range(len(cucumbers)):
        for col in range(num_cols):
            if cucumbers[row][col] == '>' and cucumbers[row][(col + 1) % num_cols] == '.': # Is a '>' cucumber and can move right
                can_move_east.add((row, col))

    for row, col in can_move_east:
        cucumbers[row][col] = '.'
        cucumbers[row][(col + 1) % num_cols] = '>'

    # Now move 'v' cucumbers.
    can_move_south = set()
    for row in range(len(cucumbers)):
        for col in range(len(cucumbers[0])):
            if cucumbers[row][col] == 'v' and cucumbers[(row + 1) % num_rows][col] == '.':
                can_move_south.add((row, col))

    for row, col in can_move_south:
        cucumbers[row][col] = '.'
        cucumbers[(row + 1) % num_rows][col] = 'v'

    return len(can_move_east) + len(can_move_south) # Number of cucumbers that moved.

def print_cucumbers(cucumbers):
    for row in cucumbers:
        print(''.join(row))
    print()

def part1(cucumbers):
    """
    Part 1: How many cucumbers can be moved?
    """
    num_moved = 1
    num_steps = 0
    while num_moved != 0:
        num_moved = move_cucumbers(cucumbers)
        num_steps += 1

    return num_steps

print(part1(cucumbers))