"""
Advent of Code 2020
Author: Carl Shan
Day 17: Conway Cubes
"""

import numpy as np
import scipy
from scipy.ndimage import convolve

raw = open('day17.ex', 'r').read()
initial = open('day17.in', 'r').read().strip().split('\n')
state = np.array([[1 if letter == '#' else 0 for letter in elem] for elem in initial])


# Significant help from: https://www.reddit.com/r/adventofcode/comments/keqsfa/comment/gg45jot
def solve(state, steps, dim=3):
    mode = 'constant'
    kernel = np.ones(shape=tuple(3 for _ in range(dim)))  # creates cube or hypercube
    kernel[tuple(1 for _ in range(dim))] = 0        # removes center
    axis_len = len(state) + 12  # padding of 6 on each side
    universe = np.zeros(shape=tuple(axis_len for _ in range(dim)))
    universe[tuple(6 for _ in range(dim - 2))] = np.pad(state, 6)
    for _ in range(steps):
        neighbors = convolve(universe, kernel, mode=mode)
        universe = (neighbors == 3) | (universe & (neighbors == 2))

    return universe


# state = solve(state, 6, dim=3)  # Part 1
# print(np.sum(state))

state = solve(state, 6, dim=4)  # Part 2
print(np.sum(state))