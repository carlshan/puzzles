"""
Advent of Code 2021 - Day 6
Author: Carl Shan

Count lanternfish.
"""

import math

aoc_input = list(map(int, open("day6small.in", "r").read().splitlines()[0].split(',')))

def tick_one_day(data):
    """
    Updates the data for one day.
    """

    new_fish = []

    for i in range(len(data)):
        fish = data[i]
        if fish == 0:
            new_fish.append(8)
            data[i] = 6
        else:
            data[i] = fish - 1

    return data + new_fish


def num_fish_produced(i, end):
    """
    Given that a fish was born on day i, return the number of direct children it will be able to produce.
    The calculation is:
        - The fish produces one child on day i + 8
        - In the remaining time until the end (end - i - 8), the fish will produce a child every 6 days.
    """
    return 1 + math.floor((end - i - 8)/6)


def num_fish_produced_all(i, end, initial_state=None, memo=None):
    """
    Now, return the total number of descendents for a fish that was produced on day i.

    This is a recursive call:
        - if i is < (end - 9), then the fish will not have time to reproduce and we can return 0
        - else we can return the number of direct children produced by the first fish, and all the direct children produced by all subsequent fish
        - we need to handle this case differently if the fish is an initial fish, however, as their first child will directly have a child
    """
    if (i, end, initial_state) in memo:
        return memo[(i, end, initial_state)]
    # Base case:
    # this fish has no time to reproduce
    if i > (end - 9):
        return 0
    # Recursive case:
    # The number descendents a fish has is the number of
    # fish its first child (born 9 days later) has
    # plus the number of descedents all subsequent fish (born at 7 day intervals)
    # have.
    if initial_state is not None:
        first_child_birth_date = initial_state + 1
    else:
        first_child_birth_date = i + 9

    second_child_day = first_child_birth_date + 7
    num_descendents_of_first_child = 1 + num_fish_produced_all(first_child_birth_date, end, None, memo)
    num_descendents_of_subsequent_children = 0
    # For each child, add the total number of descendents produced by it.
    for birth_date in range(second_child_day, end + 1, 7):
        num_descendents_of_subsequent_children +=  1 + num_fish_produced_all(birth_date, end, None, memo)

    total = num_descendents_of_first_child + num_descendents_of_subsequent_children
    memo[(i, end, initial_state)] = total
    return total

def num_fish_per_day(data, end):
    # Creates an array holding the number of fish, on each day, with the gestation
    # period equal to the index of the array
    # i.e. [5, 3, 11 ...]
    # means there are 5 fish with their timer equal to 0, 3 fish equal to 1, 11 equal to 2

    num_fish = [data.count(i) for i in range(9)]
    print("Initial State: {}".format(num_fish))
    for i in range(1, end + 1):
        num_fish[7] += num_fish[0]
        num_fish = num_fish[1:] + [num_fish[0]] # rotate
        print("Day {}: {}".format(i, num_fish))

    return sum(num_fish)


NUM_DAYS = 80
MEMO = dict()

# The total number of fish in the pond is the number of descendents + the number of original fish
# print(sum([num_fish_produced_all(0, NUM_DAYS, initial, MEMO) for initial in aoc_input]) + len(aoc_input))
print(num_fish_per_day(aoc_input, NUM_DAYS))

# Below is the brute force solution for the first part
# for i in range(1, NUM_DAYS):
#     aoc_input = tick_one_day(aoc_input)
#     # print("After {} day: ".format(i), aoc_input, " with {} fish.".format(len(aoc_input)))

# print(len(aoc_input))
