"""
Advent of Code 2021
Author: Carl Shan
Day 9
Goal: Find the 'low points' in a grid.

A 'low point' is a point in the grid that is surrounded by points that are lower
than it.

Diagonals do not count as adjacent.
"""

with open('day9.in') as f:
    data = f.read().splitlines()

def get_neighbors(x, y):
    """
    Returns coordinates in the N, S, E, W direction of the coordinate.
    """
    return [(x, y - 1),
            (x, y + 1),
            (x - 1, y),
            (x + 1, y)]

def is_in_grid(x, y, grid):
    """
    Returns a boolean indicating whether (x, y) is within the boundaries of the grid.
    """
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

def get_grid(data):
    grid = {}
    # Create the grid
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            grid[(x, y)] = int(char)

    return grid

def get_low_points(data, grid):
    """
    Find the 'low points' in a grid.

    A 'low point' is a point in the grid that is surrounded by points that are
    lower than it.

    Diagonals do not count as adjacent.
    """
    # Find the low points
    low_points = []
    for coord in grid:
        x, y = coord
        neighbors = get_neighbors(x, y)
        for neighbor in neighbors:
            nx = neighbor[0]
            ny = neighbor[1]
            if (is_in_grid(nx, ny, data)):
                if (grid[(x, y)]) >= grid[(nx, ny)]:
                    break
        else:
            low_points.append((x, y))

    return low_points

def get_risk_level(low_points, grid):
    """
    The risk level of a low point is 1 + the value of the low point.

    This returns the total risk level of all low points.
    """
    total = 0
    for point in low_points:
        x, y = point
        total += 1 + grid[(x, y)]

    return total

# Part 1
grid = get_grid(data)
low_points = get_low_points(data, grid)
# print(get_risk_level(low_points, grid))

# Part 2
# For each low point, recursively find the basin, which is the number of points that
# all "flow" to the point: they are all the adjacent smaller values.

def get_basin(point, basin, grid, data):
    """
    Recursively find all neighbors extending out from point that
    are smaller than the point.

    Equivalent to depth first search.

    Stop when all neighbors are larger.
    """
    neighbors = get_neighbors(point[0], point[1])
    for neighbor in neighbors:
        nx = neighbor[0]
        ny = neighbor[1]
        if (not is_in_grid(nx, ny, data)):
            continue
        if grid[neighbor] == 9 or grid[neighbor] < grid[point]: # will not "flow" down
            continue
        else:
            if neighbor not in basin: # already explored
                basin.append(neighbor)
                get_basin(neighbor, basin, grid, data)

def get_basins(low_points, grid, data):
    """
    Find the 'basins' in a grid.

    A 'basin' is a point in the grid that is surrounded by points that are all
    lower than it.

    Diagonals do not count as adjacent.
    """
    # Find the basins
    basins = []
    for low_point in low_points:
        basin = [low_point]
        get_basin(low_point, basin, grid, data)
        basins.append(basin)

    return basins

basins = get_basins(low_points, grid, data)
lengths = [len(basin) for basin in basins]
sorted_lengths = sorted(lengths, reverse=True) # sorted in descending order

from functools import reduce

# Product of the first three largest terms
print(reduce(lambda a, b: a * b, sorted_lengths[:3]))