"""
Advent of Code 2020
Author: Carl Shan
Day 11: Seating System
"""

seats = open('day11.in', 'r').read().splitlines()


def in_bounds(coord, seats):
    x, y = coord
    return 0 <= x < len(seats[0]) and 0 <= y < len(seats)


def get_adjacent(coord, seats):
    x, y = coord
    candidates = [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
        (x - 1, y - 1),
        (x + 1, y + 1),
        (x + 1, y - 1),
        (x - 1, y + 1)
    ]
    return [c for c in candidates if in_bounds(c, seats)]


def get_elements_in_seats(coords, seats):
    elements = []
    for coord in coords:
        x, y = coord
        elements.append(seats[y][x])

    return elements



def one_round_part1(seats):
    """
    If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    If a seat is occuped (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    Otherwise, the seat's state does not change.
    """
    new_seats = []
    num_changes = 0
    for y, row in enumerate(seats):
        new_row = []
        for x, seat in enumerate(row):
            neighbors = get_adjacent((x, y), seats)
            neighbor_elements = get_elements_in_seats(neighbors, seats)

            if seat == 'L':
                if len(list(filter(lambda s: s == '#', neighbor_elements))) == 0:
                    new_row.append('#')
                    num_changes += 1
                else:
                    new_row.append('L')
            elif seat == '#':
                if len(list(filter(lambda s: s == '#', neighbor_elements))) >= 4:
                    new_row.append('L')
                    num_changes += 1
                else:
                    new_row.append('#')
            else:
                new_row.append(seat)
        new_seats.append(''.join(new_row))
    return new_seats, num_changes


def print_seats(seats):
    for row in seats:
        print(row)


def get_first_seat_in_dir(coord, seats, x_dir, y_dir):
    """
    Finds the first seat ('L' or '#') in the direction specified by x_dir and y_dir.
    """
    x, y = coord
    x += x_dir
    y += y_dir
    while in_bounds((x, y), seats):
        if seats[y][x] != '.':
            return (x, y)
        x += x_dir
        y += y_dir

    return None


def find_first_seat(coord, seats):
    """
    Finds the first seat ('L' or '#') in each of the 8 directions from the middle.
    """
    first_seat = [
        get_first_seat_in_dir(coord, seats, -1, -1),
        get_first_seat_in_dir(coord, seats, -1, 0),
        get_first_seat_in_dir(coord, seats, -1, 1),
        get_first_seat_in_dir(coord, seats, 0, -1),
        get_first_seat_in_dir(coord, seats, 0, 1),
        get_first_seat_in_dir(coord, seats, 1, -1),
        get_first_seat_in_dir(coord, seats, 1, 0),
        get_first_seat_in_dir(coord, seats, 1, 1)
    ]

    return [s for s in first_seat if s is not None]


def one_round_part2(seats):
    """
    If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    If a seat is occuped (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    Otherwise, the seat's state does not change.
    """
    new_seats = []
    num_changes = 0
    for y, row in enumerate(seats):
        new_row = []
        for x, seat in enumerate(row):
            first_seat = find_first_seat((x, y), seats)
            neighbor_elements = get_elements_in_seats(first_seat, seats)

            if seat == 'L':
                if len(list(filter(lambda s: s == '#', neighbor_elements))) == 0:
                    new_row.append('#')
                    num_changes += 1
                else:
                    new_row.append('L')
            elif seat == '#':
                if len(list(filter(lambda s: s == '#', neighbor_elements))) >= 5:
                    new_row.append('L')
                    num_changes += 1
                else:
                    new_row.append('#')
            else:
                new_row.append(seat)
        new_seats.append(''.join(new_row))
    return new_seats, num_changes



def run(seats, part=1):
    """
    The seats are represented as a matrix, where seats[x][y] represents the seat at the intersection of x and y.
    Each seat will be either occupied (#) or empty (L).
    """
    num_changes = None
    while num_changes != 0:
        if part == 1:
            f = one_round_part1
        else:
            f = one_round_part2
        seats, num_changes = f(seats)
        # print_seats(seats)
        # print('\n')

    return sum([row.count('#') for row in seats])


print(run(seats, part=2))