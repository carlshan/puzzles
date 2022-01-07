"""
Advent of Code 2020
Author: Carl Shan
Day 14: Docking Data
"""

ins = open('day14.ex2', 'r').read().splitlines()


def parse_mask(mask):
    """
    Given an input mask of Xs, 0s and 1s, return dictionary of the binary.
    """
    mask_dict = dict()
    for i, val in enumerate(mask):
        mask_dict[i] = val

    return mask_dict


def parse_instructions(ins):
    parsed = []
    for i in ins:
        cmd, val = i.split(' = ')
        if cmd.startswith('mask'):
            parsed.append((cmd, None, parse_mask(val)))
        elif cmd.startswith('mem'):
            address = int(''.join([c for c in cmd if c.isdigit()]))
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
    result = ""
    for i, val in enumerate(binary):
        if mask_dict[i] in ('X', '1'):
            result += mask_dict[i]
        else:
            result += binary[i]
    return result


def get_all_possible_masks(prev, nxt):
    """
    Given an address, return all possible addresses with the 'X' replaced with a 1 and with a 0.
    """

    # Base case: finished parsing whole string
    if len(nxt) == 0:
        return ['']

    # Base case: no more Xs
    if nxt.find('X') == -1:
        return [nxt]

    # Recursive case:
    all_masks = []
    if nxt[0] == 'X':  # X here, so we need to replace with 0 or 1
        prev1 = prev + '1'
        prev0 = prev + '0'

        masks = get_all_possible_masks('', nxt[1:])

        for m in masks:
            all_masks.append(prev1 + m)
            all_masks.append(prev0 + m)
    else:
        all_masks = get_all_possible_masks(prev + nxt[0], nxt[1:])

    return all_masks


def execute_instructions(parsed, memory, part=1):

    for ins in parsed:
        cmd, address, val = ins
        if cmd == 'mask':
            mask_dict = val
        elif cmd == 'mem':
            if part == 1:
                binary = convert_to_binary(val)
                masked_val = int(apply_mask(pad_binary(binary), mask_dict), 2)
                memory[address] = masked_val
            else:  # part 2
                binary = convert_to_binary(address)
                masked_address = apply_mask(pad_binary(binary), mask_dict)
                all_addresses = get_all_possible_masks('', masked_address)
                for addr in all_addresses:
                    memory[int(addr, 2)] = val

    return sum(memory.values())


print(execute_instructions(parsed, memory, part=2))
