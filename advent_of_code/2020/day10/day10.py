"""
Advent of Code 2020
Author: Carl Shan
Day 10: Adapter Array
"""

jolts = open('day10.in', 'r').read().splitlines()
jolts = list(map(int, jolts))
jolts.append(max(jolts) + 3)
jolts.append(0)

jolts = sorted(jolts)


def calc_differences(jolts):
    """
    Returns the number of adjacent elements with a difference of 1 multiplied by the number of elements with a difference of 3.
    """

    differences = []
    for i in range(len(jolts) - 1):
        differences.append(jolts[i + 1] - jolts[i])

    return differences


differences = calc_differences(jolts)
print(differences.count(1) * differences.count(3))  # part 1

target = max(jolts)

memo = {}
def count_num_ways_to_sum(target, jolts, memo):
    """
    Recursively returns the number of ways to sum to the target using the jolts array.
    """
    if target == 1:
        return 1

    if target == 2:
        return 2

    if target == 3:
        return 4

    if target in memo:
        return memo[target]

    ways = 0

    for i in range(1, 4):
        if target - i in jolts:
            ways += count_num_ways_to_sum(target - i, jolts, memo)


    memo[target] = ways

    return ways


jolts.remove(0)
print(count_num_ways_to_sum(target, jolts, memo))  # part 2