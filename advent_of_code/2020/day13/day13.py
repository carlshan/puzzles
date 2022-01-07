"""
Advent of Code 2020
Author: Carl Shan
Day 13: Shuttle Search
"""

raw = open("day13.in").read().splitlines()
timestamp = int(raw[0])
buses = [int(elem) for elem in raw[1].split(',') if elem != 'x']


def part1(timestamp, buses):
    earliest_times = [(timestamp // bus) * bus + bus for bus in buses]
    earliest = earliest_times.index(min(earliest_times))
    return min(earliest_times), buses[earliest]


earliest, bus_id = part1(timestamp, buses)
print(f"Part 1: {(earliest - timestamp) * bus_id}")

buses2 = [int(elem) if elem != 'x' else 0 for elem in raw[1].split(',')]


def count_zeros(buses):
    offsets = [(buses[0], 0)]
    for i in range(1, len(buses)):
        if buses[i] != 0:
            offsets.append((buses[i], i))

    return offsets


zeros = count_zeros(buses2)

test_zeros = [
    (1789, 0),
    (37, 1),
    (47, 2),
    (1889, 3)
]

def find_offset(start, offset, goal, inc):
    found = False
    curr = start
    while not found:
        curr += inc
        if (curr + offset) % goal == 0:
            found = True

    return curr


# Part 2
def part2(zeros):
    """
    This works in the following manner:
    Start the timestamp at 0
    For each bus and offset, find the first number from the current timestamp that is evenly divisible (once accounting for the offset)
        - To do so, increment the timestamp by a step value
    Once a timestamp for a given bus has been found, increase the jump value by multiplying the bus_id.

    Why does this work?

    It's because once we have found one timestamp value that satisfies the condition for the first two buses, we can
    increase the timestamp by the product of the two bus_ids to find the next value that also satisfies the condition.
    """
    step = zeros[0][0]
    timestamp = 0

    for bus, offset in zeros[1:]:
        while (timestamp + offset) % bus != 0:
            timestamp += step
        step *= bus

    return timestamp


print(part2(zeros))
