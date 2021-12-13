"""
Advent of Code
Author Carl Shan
Day 11: Dumbo Octopus
"""

data = open('day11.in', 'r').read().splitlines()

def build_grid(data):
    grid = {}
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            grid[(int(x), int(y))] = int(char)

    return grid


def get_adjacent(pos):
    """
    Given a position, return all positions adjacent to it, including diagonals.
    """
    x, y = pos
    adjascent = [(x+1, y), (x-1, y), (x, y+1), (x, y-1),
                 (x+1, y+1), (x-1, y-1), (x-1, y+1), (x+1, y-1)]
    return adjascent

def step(grid):
    """
    Returns the total number of fish that flashed in each step.
    """
    # First, increase the value for each element in the grid by 1.
    flashed = []
    for key in grid:
        grid[key] += 1

    # Then, if any element is greater than 9, add it to the set of flashed elements.
    for key in grid:
        if grid[key] > 9:
            flashed.append(key)

    # Now, increase the value of each element adjacent to the flashed element by 1.
    for key in flashed:
        neighbors = get_adjacent(key)
        for neighbor in neighbors:
            if neighbor in grid and neighbor not in flashed:
                grid[neighbor] += 1
                if grid[neighbor] > 9:
                    flashed.append(neighbor)

    # For all elements that have flashed, set their value to 0
    for key in flashed:
        grid[key] = 0

    return len(set(flashed))

def print_grid(grid):
    """
    Given a dict containing tuples of (x, y) coordinates and values, print the grid.
    """
    for y in range(max(grid.keys(), key=lambda x: x[1])[1] + 1):
        for x in range(max(grid.keys(), key=lambda x: x[0])[0] + 1):
            print(grid[(x, y)], end='')
        print()

def part1(data, ndays):
    grid = build_grid(data)
    total_flashed = 0

    for i in range(1, ndays+1):
        num_flashed = step(grid)
        total_flashed += num_flashed
        # print('Day:', i)
        # print_grid(grid)

    return total_flashed

def part2(data):
    grid = build_grid(data)
    num_flashed = 0
    ndays = 0
    while num_flashed != len(grid):
        num_flashed = step(grid)
        ndays += 1
        # print('Day:', ndays)
        # print_grid(grid)

    return ndays


# print(part1(data, 100))
print(part2(data))