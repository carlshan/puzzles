"""
Advent of Code 2021
Author: Carl Shan
Day 16: Packet Decoder
"""

from bitstring import BitArray

hex_str = open('day16hex.ex1').read().strip()

bit_str = BitArray(hex=hex_str).bin

bits_to_hex = {'0000': '0',
                '0001': '1',
                '0010': '2',
                '0011': '3',
                '0100': '4',
                '0101': '5',
                '0110': '6',
                '0111': '7',
                '1000': '8',
                '1001': '9',
                '1010': 'A',
                '1011': 'B',
                '1100': 'C',
                '1101': 'D',
                '1110': 'E',
                '1111': 'F'}

hex_to_bits = {'0': '0000',
                '1': '0001',
                '2': '0010',
                '3': '0011',
                '4': '0100',
                '5': '0101',
                '6': '0110',
                '7': '0111',
                '8': '1000',
                '9': '1001',
                'A': '1010',
                'B': '1011',
                'C': '1100',
                'D': '1101',
                'E': '1110',
                'F': '1111'}

def handle_literal(bits, index):
    literal = ""
    while True:
        if index > len(bits):
            break
        elif bits[index] == '1':
            literal += bits[index + 1 : index + 5]
            index += 5
        elif bits[index] == '0': # last group of bits
            literal += bits[index + 1 : index + 5]
            break

    return int(literal, 2)

def handle_operator(bits, index):
    if bits[index] == '0':
        total_length_in_bits = int(bits[index + 1 : index + 1 + 15], 2)
        index += 16
        start = index
        while index < start + total_length_in_bits:
            index = handle_operator(bits, index)
    else:
        total_sub_packets = int(bits[1:12], 2)
        for i in range(total_sub_packets):
            pass # do something here


def decode_bits(bits):
    packet_version = int(bits[:3], 2)
    packet_type = int(bits[3:6], 2)
    if packet_type == 4: # this is a literal value
        return handle_literal(bits[6:], 0)
    else: # is an operator packet
        return handle_operator(bits[6:], 0)


# TODO: Finish this problem