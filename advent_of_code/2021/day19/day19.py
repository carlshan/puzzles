"""
Advent of Code 2021
Author: Carl Shan
Day 19: Beacon Scanner
"""

from collections import defaultdict

raw_data = open('day19.ex', 'r').read().strip().split('\n')

def parse_raw_data(raw_data):
    """
    Returns a dict with a list of every coordinate position for each scanner.
    """
    curr = None
    data = defaultdict(list)
    for line in raw_data:
        if '---' in line: # denotes the beginning of a new scanner
            curr = int(line.split('scanner ')[1][0])
            continue
        if line:
            data[curr].append(tuple(map(int, line.split(','))))

    return data

data = parse_raw_data(raw_data)

def convert_coord_to_list_index(coord, x_min, x_max, y_min, y_max):
    """
    Given an x coordinate, return the index of the list that the coordinate is in.
    The x cooresponds to the columns in the matrix.
    The y cooresponds to the rows in the matrix.
    """
    x, y = coord
    row = y_max - y # TODO: consider if x and y are negative
    col = x - x_min # TODO: I don't think this is sufficient
    return (row, col)

def create_matrix(x_max, x_min, y_max, y_min):
    """
    Given the max and min x and y coordinates, create a matrix of zeros.
    """
    matrix = []
    for _ in range(y_max - y_min + 1):
        matrix.append(['.'] * (x_max - x_min + 1))
    return matrix

def convert_to_visual(coords):
    """
    Given a list of coordinates, return a string representing the location of the Beacons
    at each of the coordinates.
    """

    x_max = max(coords, key=lambda x: x[0])[0]
    x_min = min(coords, key=lambda x: x[0])[0]
    y_max = max(coords, key=lambda x: x[1])[1]
    y_min = min(coords, key=lambda x: x[1])[1]
    temp = create_matrix(x_max, x_min, y_max, y_min)
    return temp