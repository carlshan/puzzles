"""
Advent of Code 2020
Author: Carl Shan
Day 9: Encoding Error
"""

data = open('day9.in').read().splitlines()
data = list(map(int, data))

sums = set()


def get_all_sums(data):
    new_sums = set()
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            new_sums.add(data[i] + data[j])

    return new_sums


preamble_length = 25

sums = get_all_sums(data[:preamble_length])  # initializing


def find_first_invalid(data, start, sums):
    for i in range(start, len(data)):
        if data[i] not in sums:
            return data[i]
        else:
            sums = get_all_sums(data[i - start:i + 1])


print(find_first_invalid(data, preamble_length, sums))  # part 1

target = 776203571


def find_contiguous_sequence(data, target):
    """
    This function finds a contiguous series of elements in data of length at least 2 that sums to the target.
    """
    for i in range(len(data)):
        total_so_far = 0
        for j in range(i, len(data)):
            total_so_far += data[j]
            if total_so_far == target:
                return min(data[i:j]) + max(data[i:j])
            elif total_so_far > target:
                break


# print(find_contiguous_sequence(data, target))  # part 2