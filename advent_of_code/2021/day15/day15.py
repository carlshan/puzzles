"""
Advent of Code 2021
Author: Carl Shan
Day 15: Chiton
"""

from collections import deque
from queue import PriorityQueue

data = open('/Users/cshan/dev/puzzles/advent_of_code/2021/day15/day15.in', 'r').read().splitlines()
start = (0, 0)
end = (len(data[0]) - 1, len(data) - 1)

def is_valid(data, curr):
    """
    This function checks if the current position is valid.
    """
    # Check if we are at the edge of the map
    if curr[0] < 0 or curr[0] >= len(data[0]) or curr[1] < 0 or curr[1] >= len(data):
        return False

    return True


def find_path_with_lowest_sum(data, curr, end, risk_so_far, prev):
    """
    This function recursively finds the path with the lowest sum from the current position to the end.
    """
    # Base case: we are at the end
    if curr == end:
        return risk_so_far

    # Recursive case: try to find the lowest sum for each of the four directions
    # (up, down, left, right)
    up = (curr[0], curr[1] - 1)
    down = (curr[0], curr[1] + 1)
    left = (curr[0] - 1, curr[1])
    right = (curr[0] + 1, curr[1])

    moves = [
                #up,
                down,
                #left,
                right
            ]

    valid_moves = [move for move in moves if is_valid(data, move) and move != prev]

    lowest_sum = 999999

    for move in valid_moves:
        # Enter the next move and find the lowest sum of all possible moves
        x, y = move
        lowest_with_move = find_path_with_lowest_sum(data, move, end, risk_so_far + int(data[y][x]), curr)
        if lowest_with_move < lowest_sum:
            lowest_sum = lowest_with_move

    return lowest_sum

def get_neighbors(curr, data):
    up = (curr[0], curr[1] - 1)
    down = (curr[0], curr[1] + 1)
    left = (curr[0] - 1, curr[1])
    right = (curr[0] + 1, curr[1])

    moves = [
            up,
            down,
            left,
            right
        ]

    valid_moves = [move for move in moves if is_valid(data, move)]

    return valid_moves


# From: https://stackabuse.com/dijkstras-algorithm-vs-a-algorithm/
def dijkstra(data, start):
    costs = dict() # stores the previously lowest seen cost for each position
    costs[start] = 0
    pq = PriorityQueue()
    pq.put((0, start)) # (cost, position)
    visited = set()

    while not pq.empty():
        cost, curr = pq.get()
        visited.add(curr)

        for neighbor in get_neighbors(curr, data):
            new_cost = cost + int(data[neighbor[1]][neighbor[0]])
            if neighbor not in visited:
                if neighbor not in costs:
                    costs[neighbor] = new_cost
                    pq.put((new_cost, neighbor))
                else:
                    old_cost = costs[neighbor]
                    new_cost = cost + int(data[neighbor[1]][neighbor[0]])
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        costs[neighbor] = new_cost
    return costs



def expand_row(row, inc):
    new_row = []
    for s in row:
        new_row.append(str(expand_num(int(s), inc)))

    return ''.join(new_row)


def expand_data(data):
    """
    This expands the data to be 5 times larger both vertically and horizontally.
    Each time it expands, it will increment each value by 1.
    """

    new_data = [expand_col(row) for row in data]
    # for each row in new_data
    # append a new row
    new_rows = []

    for inc in [1, 2, 3, 4]:
        for row in new_data:
            new_rows.append(expand_row(row, inc))

    for row in new_rows:
        new_data.append(row)
    return new_data


# print(find_path_with_lowest_sum(data, start, end, 0, start))
# print(dijkstra(data, start)[end])

def expand_num(n, inc):
    if n + inc == 10:
        return 1
    elif n + inc > 10:
        return n + inc - 9
    else:
        return n + inc

def expand_col(row):
    """
    Given a string of integers, return a string of integers that is 5 times longer
    larger.
    """
    new_row = []
    orig_row_len = len(row)
    for inc in [0, 1, 2, 3, 4]:
        for i in range(orig_row_len):
            n = int(row[i])
            new_row.append(str(expand_num(n, inc)))
    return ''.join(new_row)

expanded = expand_data(data)
end = (len(expanded[0]) - 1, len(expanded) - 1)
shortest_paths = dijkstra(expanded, start)
print(shortest_paths[end])