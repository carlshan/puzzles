"""
Advent of Code 2021
Author: Carl Shan
Day 24: Arithmetic Logic Unit
"""

instructions = open('day24.in', 'r').read().strip().split('\n')

def add(symbol, a, b, vars):
    tot = a + b
    vars[symbol] = tot

def mul(symbol, a, b, vars):
    tot = a * b
    vars[symbol] = tot

def div(symbol, a, b, vars):
    tot = a // b
    vars[symbol] = tot

def mod(symbol, a, b, vars):
    tot = a % b
    vars[symbol] = tot

def eq(symbol, a, b, vars):
    vars[symbol] = int(a == b)

OPS = {
    'add': add,
    'mul': mul,
    'div': div,
    'mod': mod,
    'eql': eq,
}

def parse_instruction(instruction):
    """
    Parse an instruction into a tuple of the form (op, a, b)
    """
    instruction = instruction.split(' ')
    op = instruction[0]
    a = instruction[1]
    b = instruction[-1]
    if op == 'inp': # input operation only takes 1 argument
        return (op, a, None)
    return (op, a, b)

VARS = {
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0
}

def run_instruction(instruction, vars, candidate, i):
    """
    Run a single instruction
    """
    op, a, b = parse_instruction(instruction)
    if op == 'inp':
        vars[a] = int(candidate[i])
    else:
        if b in ('w', 'x', 'y', 'z'):
            OPS[op](a, vars[a], vars[b], vars)
        else:
            OPS[op](a, vars[a], int(b), vars)

def get_next_candidate(candidate):
    return str(int(candidate) - 1)

def part1():
    """
    Generate all possible 14 digit numbers not containing the number 0 in any place.

    Then, run all instructions for this number.

    At the end of all instructions, see if the value of vars['z'] is equal to 1.

    If so, check to see if it's the largest number found so far.

    Return the largest number after trying all 14-digit numbers.
    """
    candidate = '9' * 14
    largest = 0
    while len(candidate) == 14:
        if '0' in candidate:
            candidate = get_next_candidate(candidate)
            continue
        vars = VARS.copy()
        i = 0
        for instruction in instructions:
            run_instruction(instruction, vars, candidate, i)
            if 'inp' in instruction:
                i += 1
        if vars['z'] == 0:
            largest = max(largest, int(candidate))
            print(candidate)
            break
        candidate = get_next_candidate(candidate)
    return largest

print(part1())