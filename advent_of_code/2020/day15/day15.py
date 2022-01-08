"""
Advent of Code 2020
Author: Carl Shan
Day 15: Rambunctious Recitation
"""
from collections import defaultdict

nums = open('day15.in', 'r').read().split(',')
nums = [int(x) for x in nums]


def play_game(nums, end=2020):
    most_recent_index = defaultdict(tuple)
    for i, num in enumerate(nums[:-1]):
        most_recent_index[nums[i]] = (i + 1, i + 1)  # (before_recent, most_recent)
    most_recent_num = nums[-1]
    for turn in range(len(nums), end):
        if most_recent_num not in most_recent_index:
            most_recent_index[most_recent_num] = (turn, turn)  # update most_recent
            most_recent_num = 0
            most_recent_index[0] = (most_recent_index[0][1], turn + 1)  # update when 0 is said
        else:
            most_recent_num = most_recent_index[most_recent_num][1] - most_recent_index[most_recent_num][0]
            if most_recent_num not in most_recent_index:
                most_recent_index[most_recent_num] = (turn + 1, turn + 1)  # update most_recent
            else:
                most_recent_index[most_recent_num] = (most_recent_index[most_recent_num][1], turn + 1)

    return most_recent_num


# The below is the same function, but optimized after reading on Reddit
# The series of numbers being generated are called Van Eyck numbers
def play_game_optimized(nums, end):
    most_recent = {num: i + 1 for i, num in enumerate(nums)}
    last = nums[-1]

    for turn in range(len(nums), end):
        most_recent[last], last = turn, turn - most_recent.get(last, turn)

    return last


part1 = 2020
part2 = 30000000
print(play_game_optimized(nums, part1))
print(play_game_optimized(nums, part2))
