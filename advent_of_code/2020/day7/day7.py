"""
Advent of Code 2020
Author: Carl Shan
Day 7: Handy Haversacks
"""

rules = open('day7.in', 'r').read().splitlines()


def parse_rule(rule):
    rule = rule.split(' contain ')
    bag = rule[0].replace('bags', '').replace('bag', '').strip()
    if 'no other bags' in rule[1]:
        return bag, []
    else:
        items = rule[1].split(', ')
        return bag, [item.strip().replace('.', '') for item in items]


def parse_items(items):
    bags = []
    for item in items:
        num = int(item[:item.find(' ')].strip())
        color = item[item.find(' ') + 1:].replace('bags', '').replace('bag', '').strip()
        bags.append((color, num))
    return bags


def create_mapping(rules):
    mapping = {}
    for rule in rules:
        bag, items = parse_rule(rule)
        contains = parse_items(items)
        mapping[bag] = contains
    return mapping


def create_inverse_mapping(mapping):
    inverse_mapping = {}
    for bag, contains in mapping.items():
        for b in contains:
            color, num = b
            if color not in inverse_mapping:
                inverse_mapping[color] = []
            inverse_mapping[color].append(bag)
    return inverse_mapping


def find_outermost_bag(color, inverse_mapping):
    parents = []
    if color not in inverse_mapping:
        parents.append(color)
    else:
        parents.append(color)
        for bag in inverse_mapping[color]:
            parents += find_outermost_bag(bag, inverse_mapping)

    return parents


def contains_gold_bag(rules):
    mapping = create_mapping(rules)
    inverse_mapping = create_inverse_mapping(mapping)
    unique_colors = set()
    count = 0
    for rule in rules:
        if 'shiny gold bag' in rule and 'shiny gold bag' != rule[:len('shiny gold bag')]:
            color = rule.split(' contain ')[0]

    return count


def find_number_of_bags(color, mapping):
    """
    Finds the total number of bags contained in a single shiny gold bag.
    """
    children_bags = mapping[color]
    total = 0
    for child_bag in children_bags:
        child_color, num = child_bag
        total = total + num + num * find_number_of_bags(child_color, mapping)

    return total

# print(contains_gold_bag(rules)) # part 1
mapping = create_mapping(rules)
inverse_mapping = create_inverse_mapping(mapping)
parents = find_outermost_bag('shiny gold', inverse_mapping)
# print(len(set(parents)) - 1) # subtracting 1 for 'shiny gold'

print(find_number_of_bags('shiny gold', mapping)) # part 2