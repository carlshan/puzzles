"""
Advent of Code 2020
Author: Carl Shan
Day 5: Binary Boarding
"""

seats = open('day5.in', 'r').read().split('\n')


def get_row(seat):
    row = seat[:7]
    binary = ''.join(list(map(lambda b: '1' if b == 'B' else '0', row)))
    return int(binary, 2)


def get_col(seat):
    col = seat[7:]
    binary = ''.join(list(map(lambda b: '1' if b == 'R' else '0', col)))
    return int(binary, 2)


def get_seat_id(seat):
    return get_row(seat) * 8 + get_col(seat)


def largest_seat_id(seats):
    seat_ids = list(map(get_seat_id, seats))
    return max(seat_ids)


def find_missing_seat(seats):

    seat_ids = list(map(get_seat_id, seats))
    seat_ids = sorted(seat_ids)

    for i in range(len(seat_ids) - 1):
        if seat_ids[i] + 2 == seat_ids[i + 1]:
            return seat_ids[i] + 1

print(largest_seat_id(seats)) # part 1
print(find_missing_seat(seats)) # part 2
