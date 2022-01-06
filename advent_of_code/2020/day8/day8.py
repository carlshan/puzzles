"""
Advent of Code 2020
Author: Carl Shan
Day 8: Handheld Halting
"""

instructions = open('day8.in', 'r').read().splitlines()


def parse_instruction(ins):
    op, val = ins.split(' ')
    return (op, int(val))


parsed = [parse_instruction(ins) for ins in instructions]


def execute_instructions(instructions):
    acc = 0
    executed = []
    i = 0
    while True:
        if i in executed:
            return acc, False # ran into infinite loop
        executed.append(i)
        if i == len(instructions):
            return acc, True # finished execution
        op, val = instructions[i]
        if op == 'jmp':
            i += val
        else:
            i += 1
        if op == 'acc':
            acc += val

    return acc

# print(execute_instructions(parsed)) # part 1
all_jmp_or_nop = [
    i for i, (op, val) in enumerate(parsed) if op == 'jmp' or op == 'nop'
]


def build_new_instructions(i, instructions):
    new_instructions = instructions[:]
    new_instructions[i] = ('nop', 0) if new_instructions[i][0] == 'jmp' else ('jmp', new_instructions[i][1])
    return new_instructions


all_instructions = [ # all possible instructions with jmp swapping to nop and nop swapping to jmp
    build_new_instructions(i, parsed) for i in all_jmp_or_nop
]

def try_all_instructions(all_instructions):
    for instruction in all_instructions:
        if execute_instructions(instruction)[1]:
            return execute_instructions(instruction)[0]

print(try_all_instructions(all_instructions))