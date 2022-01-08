"""
Advent of Code 2020
Author: Carl Shan
Day 15: Rambunctious Recitation
"""

nums = open('day15.in', 'r').read().split(',')
nums = [int(x) for x in nums]


from collections import defaultdict

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


print(play_game(nums, 30000000))
