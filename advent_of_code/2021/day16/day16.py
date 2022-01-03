"""
Advent of Code 2021
Author: Carl Shan
Day 16: Packet Decoder
"""

from bitstring import BitArray
from functools import reduce

hex_str = open('day16.in').read().strip()

bit_str = BitArray(hex=hex_str).bin

# Return the sum of the version number of all packets
# Code below from: https://www.reddit.com/r/adventofcode/comments/rhj2hm/comment/hoqvaov/

def process_literal(bits):
    index = 0
    while True:
        if bits[index] == '1':
            index += 5
        elif bits[index] == '0':
            # Final group of bits
            index += 5
            break

    if index < len(bits): # padding remains
        while (index + 6) % 4 != 0: # find the first group of 4
            index += 1
    return index

total = 0
def get_version_num_tot(bits):
    global total
    version_num_tot = int(bits[:3], 2)
    total += version_num_tot
    bits = bits[3:]
    packet_id = int(bits[:3], 2)
    bits = bits[3:]
    if packet_id == 4:
        result = ""
        while True:
            result += bits[1:5]
            group = bits[0]
            bits = bits[5:]
            if group == '0': # last group of bits
                break
        return (bits, int(result, 2))
    else:
        length_type_id = bits[0]
        bits = bits[1:]
        values = []
        if length_type_id == '0':
            length = int(bits[:15], 2)
            bits = bits[15:]
            sub_packets = bits[:length]
            while sub_packets:
                sub_packets, value = get_version_num_tot(sub_packets)
                values.append(value)
            bits = bits[length:]
        else:
            num_subpackets = int(bits[:11], 2)
            bits = bits[11:]
            for _ in range(num_subpackets):
                bits, value = get_version_num_tot(bits)
                values.append(value)
        if packet_id == 0:
            return (bits, sum(values))
        elif packet_id == 1:
            return (bits, reduce(lambda f, s: f * s, values))
        elif packet_id == 2:
            return (bits, min(values))
        elif packet_id == 3:
            return (bits, max(values))
        elif packet_id == 5:
            return (bits, int(values[0] > values[1]))
        elif packet_id == 6:
            return (bits, int(values[0] < values[1]))
        elif packet_id == 7:
            return (bits, int(values[0] == values[1]))

result = get_version_num_tot(bit_str)
print(result)