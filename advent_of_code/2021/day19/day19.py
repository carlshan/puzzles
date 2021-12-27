"""
Advent of Code 2021
Author: Carl Shan
Day 19: Beacon Scanner
"""

from collections import defaultdict
from scipy.spatial.distance import pdist, cdist

raw_data = open('day19.ex3', 'r').read().strip().split('\n')

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

# Part 1
def at_least_n_pairwise_distances(coords1, coords2, n):
    """
    This function returns whether the two list of coordinates have at least n elements in common.
    """
    distances1 = pdist(coords1)
    distances2 = pdist(coords2)
    in_common = len(set(distances1).intersection(distances2))
    return in_common >= n, in_common

def count_num_unique_distances(data):
    """
    Returns the number of unique distances for all coordinates within each scanner.
    """
    total = set()

    for scanner in data:
        coords = data[scanner]
        total = total.union(set(pdist(coords)))

    return total


"""
To figure out which coords have at least 12 beacons in common, need to find the exact 12 coordinates for each scanner that they have in common.

Then, from those 12 coordinates we can work out the location (with respect to the first scanner) of each other scanner.
"""


threshold = 11 * 12 / 2 # 12 choose 2

# print(at_least_n_pairwise_distances(data[0], data[1], threshold))
print(count_num_unique_distances(data))