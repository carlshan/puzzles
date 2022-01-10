"""
Advent of Code 2020
Author: Carl Shan
Day 16: Ticket Translation
"""

from collections import defaultdict
from functools import reduce

rules, ticket, nearby = open('day16.in', 'r').read().split('\n\n')
nearby = nearby.split('\n')[1:]


def get_min_max(rule):
    rule = rule.split('-')
    return int(rule[0]), int(rule[1])


def flatten(lst):
    return [item for sublist in lst for item in sublist]


def parse_rules(rules):
    rules = rules.split('\n')
    rules = [x.split(': ')[1] for x in rules]
    rules = [rule.split(' or ') for rule in rules]
    rules = [[get_min_max(x) for x in rule] for rule in rules]
    return flatten(rules)


def parse_ticket(ticket):
    ticket = ticket.split(',')
    return [int(x) for x in ticket]


def apply_rules(rules, tickets):

    invalid_values = []
    valid_tickets = []

    for ticket in tickets:
        parsed_ticket = parse_ticket(ticket)
        for val in parsed_ticket:
            for rule in rules:
                low, high = rule
                if low <= val <= high:
                    break
            else:  # did not break
                invalid_values.append(val)

    for ticket in tickets:   # if a ticket contains any invalid_value, it is invalid
        parsed_ticket = parse_ticket(ticket)
        if not any(val in invalid_values for val in parsed_ticket):  # is valid
            valid_tickets.append(ticket)

    return invalid_values, valid_tickets


parsed_rules = parse_rules(rules)

invalid_values, valid_tickets = apply_rules(parsed_rules, nearby)

print(sum(invalid_values))  # part 1

# Part 2

def parse_rules_dict(rules):
    """
    Returns a dictionary of {rule: [(low, high), (low, high)]} for the rules.
    """
    rules = rules.split('\n')
    rules = {x.split(': ')[0]: x.split(': ')[1].split(' or ') for x in rules}

    for field in rules:
        rules[field] = [get_min_max(x) for x in rules[field]]

    return rules


def ticket_passes_rule(rule_values, ticket_val):
    """
    Returns a boolean indicating whether the ticket_val passes at least one of the rule_values.
    """
    for low, high in rule_values:
        if low <= ticket_val <= high:
            return True
    return False


def apply_rules_to_ticket(rules_dict, ticket):
    """
    Given a ticket and rules_dict, returns a dictionary of {position: [rule_values]} for all rules that passed for each position.
    """
    parsed_ticket = parse_ticket(ticket)
    matched = defaultdict(list)
    for pos, val in enumerate(parsed_ticket):
        matched[pos] = [rule for rule, rule_values in rules_dict.items() if ticket_passes_rule(rule_values, val)]

    return matched


def get_invalid_matches(ticket_matches):
    """
    Given a dictionary of {position: [rule_values]}, returns a list of tuples of the form (position, [rule_values]) for
    the position that does not match all rules.
    """
    all_fields = set(rules_dict.keys())
    for pos, matches in ticket_matches.items():
        if len(matches) < 20:  # Does not match all rules
            return pos, all_fields - set(matches)  # We know which position CANNOT be matched to a rule.


def find_best_match(candidates, invalid_matches):
    """
    First, we find reduce the candidates down to only those that are not invalid.

    That will result in a dict of {pos: [rule]} where at least one position will only match with one rule.

    Then we loop:
        - Until all positions only have ONE valid rule, we continue to match.
    """
    for pos in candidates:
        for invalid_match in invalid_matches:
            if invalid_match[0] == pos:
                candidates[pos] -= invalid_match[1]

    matching_complete = False
    while not matching_complete:
        for pos, candidates_list in candidates.items():
            if len(candidates_list) == 1:  # Only one valid rule for this field
                for pos2, candidates_list2 in candidates.items():
                    if pos2 != pos:
                        candidates_list2 -= candidates_list
            else:
                continue

        # Check to see if all positions only have 1 rule
        matching_complete = all(len(candidates[pos]) == 1 for pos in candidates)

    return candidates


def solve_part2(my_ticket, correctly_matched):
    my_ticket = parse_ticket(my_ticket.split(':\n')[1])
    departure_positions = [pos for pos in correctly_matched if 'departure' in list(correctly_matched[pos])[0]]

    departure_values = [val for i, val in enumerate(my_ticket) if i in departure_positions]

    return reduce(lambda x, y: x * y, departure_values)


rules_dict = parse_rules_dict(rules)
all_ticket_matches = [apply_rules_to_ticket(rules_dict, ticket) for ticket in valid_tickets]
candidates = {pos: set(rules_dict.keys()) for pos, rule in enumerate(rules_dict)}
invalid_matches = [get_invalid_matches(ticket_matches) for ticket_matches in all_ticket_matches]
correctly_matched = find_best_match(candidates, invalid_matches)

print(solve_part2(ticket, correctly_matched))  # Part 2
