"""
Advent of Code 2021
Author: Carl Shan
Day 5
Problem: Determine beginning and ends of lines, determine the number of points where at least two lines overlap
"""

aoc_input = open('day5.in', 'r')
data = aoc_input.readlines()

def clean_line(line):
    c1, c2 = line.split(' -> ')
    (x1, y1) = c1.split(',')
    (x2, y2) = c2.split(',')

    return ((int(x1), int(y1)), (int(x2), int(y2)))

cleaned = [clean_line(line) for line in data]

def is_vertical(c1, c2):
    """
    Returns whether a line is a vertical line, as we need to handle it differently.
    """
    return c1[0] == c2[0]

def is_horizontal(c1, c2):
    """
    Returns whether a line is a horizontal line.
    """
    return c1[1] == c2[1]

def get_slope(c1, c2):
    """
    Returns the slope of a line.
    """
    slope = (c2[1] - c1[1]) / (c2[0] - c1[0])
    return slope

intersections = dict() # will hold coord: num_overlaps

def get_all_points(c1, c2):
    """
    Given the start and end of a line, return a list containing all the points stored as tuples (x, y)
    """
    all_points = [c1, c2]
    start_x = min(c1[0], c2[0])
    stop_x = max(c1[0], c2[0])

    start_y = min(c1[1], c2[1])
    stop_y = max(c1[1], c2[1])
    if is_vertical(c1, c2):
        for y in range(start_y + 1, stop_y):
            all_points.append((c1[0], y)) # x coordinate stays the same
    elif is_horizontal(c1, c2):
        for x in range(start_x + 1, stop_x):
            all_points.append((x, c1[1]))
    else:
        slope = int(get_slope(c1, c2))
        if c1[0] == start_x: # this is the smallest or left_most point
            start_x = c1[0]
            start_y = c1[1]
            stop_x = c2[0]
            stop_y = c2[1]
        else:
            start_x = c2[0]
            start_y = c2[1]
            stop_x = c1[0]
            stop_y = c1[1]

        for x in range(start_x + 1, stop_x):
            new_point = (x, start_y + slope * (x - start_x))
            all_points.append(new_point)

    return all_points

def print_grid(nrows, ncols, intersections):
    grid = [
        [' . ' for j in range(ncols)] for i in range(nrows)
    ]
    for coord in intersections:
        row = coord[1]
        col = coord[0]
        grid[row][col] = ' {} '.format(str(intersections[coord]))

    for row in grid:
        print(row)


def count_intersections(data, intersections):
    num_intersections = 0

    # First, process the data
    for line in data:
        c1, c2 = line
        # if is_horizontal(c1, c2) or is_vertical(c1, c2):
        all_points = get_all_points(c1, c2)
        for point in all_points:
            if point not in intersections:
                intersections[point] = 1
            else:
                intersections[point] += 1

    # Now, count intersections
    for point in intersections:
        if intersections[point] >= 2:
            num_intersections += 1

    return num_intersections

num_intersections = count_intersections(cleaned, intersections)
# print_grid(10, 10, intersections)

