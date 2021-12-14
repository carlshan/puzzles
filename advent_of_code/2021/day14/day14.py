"""
Advent of Code 2021
Author: Carl Shan
Day 14: Extended Polymerization
"""

from collections import Counter, defaultdict

data = open("day14.in", 'r').read().strip().split('\n')
start = data[0]
rules = data[2:]

def process_rules(rules):
    """
    Process the rules into a dict
    """
    rule_dict = {}
    for rule in rules:
        pair, become = rule.split(' -> ')
        rule_dict[pair] = become
    return rule_dict

def react(polymer, rule_dict):
    """
    Process the polymer and return the result
    """
    result = ""
    for i in range(len(polymer) - 1):
        pair = polymer[i] + polymer[i + 1]
        if result == "": # Only add the first character on the first iteration
            result += polymer[i]
        if pair in rule_dict:
            result += rule_dict[pair]
        result += polymer[i + 1]
    return result

def generate_polymer(start, rules, nsteps):
    rule_dict = process_rules(rules)
    polymer = start
    for _ in range(nsteps):
        polymer = react(polymer, rule_dict)
    return polymer

def part1(start, rules, nsteps):
    polymer = generate_polymer(start, rules, nsteps)
    c = Counter(polymer)

    return c.most_common()[0][1] - c.most_common()[-1][1]


# print(part1(start, rules, 10))

# Part 2:
# To save on space, we can try to only save the number of pairs of characters, rather than
# the entire string.

# The idea for this part came from: https://www.reddit.com/r/adventofcode/comments/rfzq6f/comment/hohc8vc/?utm_source=share&utm_medium=web2x&context=3
def part2(start, rules, nsteps):
    rules = process_rules(rules)
    polymer = start
    pairs = Counter(map(str.__add__, start, start[1:]))
    chars = Counter(polymer)
    # For each step, increment the pairs and characters
    for _ in range(nsteps):
        copy = pairs.copy() # making a copy so we don't modify the original pair_counts while looping
        for pair in copy:
            new_char = rules[pair]
            counts = copy[pair]
            chars[new_char]            += counts
            pairs[pair[0] + new_char]  += counts
            pairs[new_char + pair[1]]  += counts
            pairs[pair]                -= counts

    return chars

char_counts = part2(start, rules, 40)
print(max(char_counts.values()) - min(char_counts.values()))



