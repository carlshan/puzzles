"""
Advent of Code 2020
Author: Carl Shan
Day 14: Docking Data
"""

ins = open('day14.in', 'r').read().splitlines()


def parse_mask(mask):
    """
    Given an input mask of Xs, 0s and 1s, return dictionary of the binary.
    """
    mask_dict = dict()
    for i, val in enumerate(mask):
        if val in ('0', '1'):
            mask_dict[i] = val

    return mask_dict


def parse_instructions(ins):
    parsed = []
    for i in ins:
        cmd, val = i.split(' = ')
        if cmd.startswith('mask'):
            parsed.append((cmd, None, parse_mask(val)))
        elif cmd.startswith('mem'):
            address = int(cmd.replace('mem', '').replace('[', '').replace(']', ''))
            parsed.append(('mem', address, int(val)))

    return parsed


parsed = parse_instructions(ins)
memory = dict()


def pad_binary(binary):
    if len(binary) < 36:
        return '0' * (36 - len(binary)) + binary
    return binary


def convert_to_binary(num):
    """
    Given a number, convert it to the string binary representation.
    """
    return '{0:b}'.format(num)


def apply_mask(binary, mask_dict):
    """
    Given a binary string and a mask dictionary, apply the mask to the binary.
    """
    return ''.join([mask_dict.get(i, binary[i]) for i in range(len(binary))])


def execute_instructions(parsed, memory):

    for ins in parsed:
        cmd, address, val = ins
        if cmd == 'mask':
            mask_dict = val
        elif cmd == 'mem':
            binary = convert_to_binary(val)
            masked_val = int(apply_mask(pad_binary(binary), mask_dict), 2)
            memory[address] = masked_val

    return sum(memory.values())


print(execute_instructions(parsed, memory))
