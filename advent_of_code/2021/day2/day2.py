"""
Advent of Code 2021
Author: Carl Shan
Day 2
Problem: Calculate the horizontal position and depth you would have after following the planned course.
What do you get if you multiply your final horizontal position by your final depth?
"""

day2input = open("day2.in", "r")
data = day2input.readlines()

# Part 1
def get_position(data):
    total = 0
    for command in data:
        cmd, amt = command.split(" ")
        amt = int(amt)
        if (cmd == "up"):
            amt = -amt

        total += amt

    return total

depth_commands = [elem for elem in data if "down" in elem or "up" in elem]
horizontal_commands = [elem for elem in data if "forward" in elem]
print(get_position(depth_commands) * get_position(horizontal_commands))

# Part 2:
def get_aim(cmd, aim, amt):
    new_aim = aim
    if (cmd == "up"):
        new_aim -= amt
    else:
        new_aim += amt
    return new_aim

def get_position_with_aim(data):
    horizontal = 0
    depth = 0
    aim = 0
    for command in data:
        cmd, amt = command.split(" ")
        amt = int(amt)
        if (cmd in ("up", "down")): # is a depthcommand
            aim = get_aim(cmd, aim, amt)
        else: # is a horizontal command
            horizontal += amt
            depth += aim * amt

    return horizontal, depth

horizontal, depth = get_position_with_aim(data)
print(horizontal * depth)