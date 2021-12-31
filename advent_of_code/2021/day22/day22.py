"""
Advent of Code 2021
Author: Carl Shan
Day 22: Reactor Reboot
"""

from collections import Counter

data = open('day22.in', 'r').read().strip().split('\n')

def parse_instructions(coords):
    # Parses the instructions into a 3-ple of (x, y, z)
    xs, ys, zs = coords.split(',')
    x_min = int(xs.split('=')[1].split('..')[0])
    x_max = int(xs.split('=')[1].split('..')[1])
    y_min = int(ys.split('=')[1].split('..')[0])
    y_max = int(ys.split('=')[1].split('..')[1])
    z_min = int(zs.split('=')[1].split('..')[0])
    z_max = int(zs.split('=')[1].split('..')[1])

    return ((x_min, x_max), (y_min, y_max), (z_min, z_max))

instructions = [
    (line.split(' ')[0], parse_instructions(line.split(' ')[1]))
    for line in data
]


def create_starting_cubes(size=50):
    cubes = dict()
    for x in range(-50, size+1):
        for y in range(-50, size+1):
            for z in range(-50, size+1):
                cubes[(x, y, z)] = False # False = off, True = on

    return cubes

def outside_initialization_area(x, y, z, initial=50):
    return (x >= -initial and x <= initial) and (y >= -initial and y <= initial) and (z >= -initial and z <= initial)

def execute_instructions(cubes, instructions):
    for step in instructions:
        onoff, ranges = step
        (x_min, x_max), (y_min, y_max), (z_min, z_max) = ranges

        for cube in cubes:
            x, y, z = cube
            if x_min <= x <= x_max and y_min <= y <= y_max and z_min <= z <= z_max:
                cubes[cube] = onoff == 'on'

    return cubes


# cubes = create_starting_cubes()
# cubes = execute_instructions(cubes, instructions)

# print(sum(cubes.values()))

# Part 2 - We need to take a different approach because the area each instruction affects is too large to store in memory

def get_intersection(cube1, cube2):
    """
    Given the coordinates of two cubes, returns the coordinates representing their intersection.
    """
    (x_min1, x_max1), (y_min1, y_max1), (z_min1, z_max1) = cube1
    (x_min2, x_max2), (y_min2, y_max2), (z_min2, z_max2) = cube2
    x_min = max(x_min1, x_min2)
    x_max = min(x_max1, x_max2)
    y_min = max(y_min1, y_min2)
    y_max = min(y_max1, y_max2)
    z_min = max(z_min1, z_min2)
    z_max = min(z_max1, z_max2)

    if x_min <= x_max and y_min <= y_max and z_min <= z_max:
        return ((x_min, x_max), (y_min, y_max), (z_min, z_max))
    else:
        return None


# The solution below is copied from: https://www.reddit.com/r/adventofcode/comments/rlxhmg/comment/hpizza8/
def part2(instructions):

    cubes = Counter()

    for step in instructions:
        updates = Counter()
        onoff, ranges = step
        onoff = 1 if onoff == 'on' else -1

        for cube, count in cubes.items():
            intersection = get_intersection(cube, ranges)
            if intersection:
                updates[intersection] -= count

        if onoff > 0:
            updates[ranges] += onoff

        cubes.update(updates)

    return cubes, sum((x1 - x0 + 1) * (y1 - y0 + 1) * (z1 - z0 + 1) * count
          for ((x0, x1), (y0, y1), (z0, z1)), count in cubes.items())

cubes, tot = part2(instructions)


