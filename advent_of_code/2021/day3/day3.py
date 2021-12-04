"""
Advent of Code 2021
Author: Carl Shan
Day 3
Problem: Calculate the power consumption by multiplying the gamma rate and the epsilon rate
"""

day3input = open("day3.in", "r")
data = day3input.readlines()

test_data = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""".split("\n")




# Part 1
def get_bits_per_position(data, len_bits):
    bits = {i: [] for i in range(len_bits)}
    for line in data:
        for i in range(0, len_bits):
            bits[i].append(line[i])

    return bits

def get_most_common(bits):
    ones = [elem for elem in bits if elem == "1"]
    zeroes = [elem for elem in bits if elem == "0"]
    if len(ones) >= len(zeroes):
        return "1"
    return "0"

def get_least_common(bits):
    ones = [elem for elem in bits if elem == "1"]
    zeroes = [elem for elem in bits if elem == "0"]
    if len(zeroes) <= len(ones):
        return "0"
    return "1"

def get_gamma(data):
    len_bits = len(data[0].strip())
    bits = get_bits_per_position(data, len_bits)
    gamma = ""
    for i in range(len_bits):
        gamma += get_most_common(bits[i])
    return gamma

def invert_bits(sequence):
    result = ""
    for b in sequence:
        if b == "1":
            result += "0"
        else:
            result += "1"
    return result

gamma = get_gamma(data)
epsilon = invert_bits(gamma)
print(int(gamma, 2) * int(epsilon, 2))

# Part 2:
def get_rating(data, which='oxygen'):
    len_bits = len(data[0].strip())
    bits = get_bits_per_position(data, len_bits)
    most_common = {i: get_most_common(bits[i]) for i in range(len_bits)}
    least_common = {i: get_least_common(bits[i]) for i in range(len_bits)}
    if (which == 'oxygen'):
        remaining = [d for d in data if d[0] == most_common[0]]
    else:
        remaining = [d for d in data if d[0] == least_common[0]]
    for i in range(1, len_bits):
        bits = get_bits_per_position(remaining, len_bits)
        most_common = {j: get_most_common(bits[j]) for j in range(len_bits)}
        least_common = {i: get_least_common(bits[i]) for i in range(len_bits)}
        if which == 'oxygen':
            remaining = [d for d in remaining if d[i] == most_common[i]]
        else:
            remaining = [d for d in remaining if d[i] == least_common[i]]
        if(len(remaining) == 1): # if there's only one value left, we can return immediately
            break

    # Last one remaining is the relevant rating
    return remaining

oxygen_rating = get_rating(data, 'oxygen')[0]
co2_rating = get_rating(data, 'co2')[0]

print(int(oxygen_rating, 2) * int(co2_rating, 2))


