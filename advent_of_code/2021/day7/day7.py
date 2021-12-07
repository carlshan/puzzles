"""
Advent of Code 2021
Author: Carl Shan
Day 7
"""

aoc_input = open("day7.in", "r").read().splitlines()[0]
data = list(map(int, aoc_input.split(",")))

# Part 1 - Brute force O(n^2) solution
def get_fuel_cost1(pos1, pos2):
    return abs(pos1 - pos2)

def get_fuel_cost2(pos1, pos2):
    diff = abs(pos1 - pos2)
    return diff * (diff + 1) // 2

def get_min_fuel(data):
    min_fuel = 0
    for pos1 in data:
        total_fuel = 0
        for pos2 in data:
            # fuel = get_fuel_cost1(pos1, pos2)
            fuel = get_fuel_cost2(pos1, pos2)
            total_fuel += fuel
        if total_fuel < min_fuel or min_fuel == 0:
            min_fuel = total_fuel

    return min_fuel

# print(get_min_fuel(data))

# Part 2: Different fuel cost
print(get_min_fuel(data))

