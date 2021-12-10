"""
Advent of Code 2021
Author: Carl Shan
Day 10
"""

AOC_INPUT = "day10.in"
data = open(AOC_INPUT).read().splitlines()

POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

BRACKET_PAIRS = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

def part1(data):
    tot_points = 0
    for line in data:
        stack = []
        for char in line:
            if char in BRACKET_PAIRS.keys():
                stack.append(char)
            elif char != BRACKET_PAIRS[stack.pop()]: # first mismatch
                tot_points += POINTS[char]
                break
    return tot_points

print(part1(data))

# Part 2
POINTS_2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

def part2(data):
    incomplete_lines = []
    for line in data:
        stack = []
        tot_score = 0
        for char in line:
            if char in BRACKET_PAIRS.keys():
                stack.append(char)
            elif char != BRACKET_PAIRS[stack[-1]]:
                break
            else:
                stack.pop()
        else: # did not encounter break
            while(len(stack) > 0):
                open_char = stack.pop()
                tot_score = 5 * tot_score + POINTS_2[BRACKET_PAIRS[open_char]]
            incomplete_lines.append(tot_score)

    sorted_lines = sorted(incomplete_lines)
    return sorted_lines[len(sorted_lines) // 2] # middle / median element

print(part2(data))
