"""
Advent of Code 2020
Author: Carl Shan
Day 3: Toboggan Trajectory
"""

from functools import reduce

data = [
    list(row)
    for row in open('day3.in', 'r').read().strip().splitlines()
]

start = (0, 0)
slopes = [(1, 1),
          (3, 1),
          (5, 1),
          (7, 1),
          (1, 2)]
def solve(data, start, slopes, part=1):
    counters = []
    for hor, vert in slopes:
        row, col = start[0] + vert, start[1] + hor
        counter = 0
        num_row = 0
        while num_row < len(data) - vert:
            counter += int(data[row][col] == '#')
            row, col = (row + vert), ((col + hor) % len(data[0]))
            num_row += vert
        if part == 1:
            return counter
        else:
            counters.append(counter)

    return counters


print(solve(data, start, slopes, 1)) # part 1
counters = solve(data, start, slopes, 2)
print(reduce(lambda x, y: x * y, counters)) # part 2

