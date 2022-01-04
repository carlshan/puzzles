"""
Advent of Code 2020
Author: Carl Shan
Day 2: Password Philosophy
"""

data = open('day2.in', 'r').read().strip().splitlines()

def parse(line):
    first, password = line.split(': ')
    lowhigh, letter = first.split(' ')
    low, high = lowhigh.split('-')
    return (int(low), int(high), letter, password)

def solve(data, part = 1):
    invalid_passes = []
    for line in data:
        low, high, letter, password = parse(line)
        count = password.count(letter)
        if part == 1:
            if count < low or count > high:
                invalid_passes.append(password)
        else:
            combined = password[low - 1] + password[high - 1]
            if combined.count(letter) != 1:
                invalid_passes.append(password)

    return invalid_passes

invalid = solve(data, part=2)
num_valid = len(data) - len(invalid)
print(num_valid)
