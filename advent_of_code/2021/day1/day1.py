"""
Advent of Code 2021
Author: Carl Shan
Day 1
Problem: Count the number of times a depth measurement increases from the previous measurement. (There is no measurement before the first measurement.)
"""

day1input = open("day1.in", "r")
data = list(map(int, day1input.readlines()))

test_data = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263
]

# Count the number of times the sum of measurements with a sliding window of 3 increases
def count_num_increases_window(data, window):
    num_increases = 0
    for i in range(len(data) - window):
        curr = sum(data[i : i + window])
        nxt = sum(data[i + 1: i + 1 + window])
        if (nxt > curr):
            num_increases += 1

    return num_increases

# Part 1:
print(count_num_increases_window(test_data, 1))
print(count_num_increases_window(data, 1))

# Part 2:
print(count_num_increases_window(test_data, 3))
print(count_num_increases_window(data, 3))
