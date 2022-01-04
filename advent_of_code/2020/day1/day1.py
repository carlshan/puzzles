"""
Advent of Code 2020
Author: Carl Shan
Day 1: Report Repair
"""

data = open('day1.in', 'r').read().strip().splitlines()
data = list(map(int, data))

from itertools import combinations
from functools import reduce

def solve(data, part=1, target=2020):
    combs = combinations(data, part + 1)
    for comb in combs:
        if sum(comb) == target:
            return reduce(lambda x, y: x * y, comb)

print(solve(data, 1))
print(solve(data, 2))