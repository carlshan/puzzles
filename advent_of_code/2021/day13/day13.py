"""
Advent of Code 2021
Author: Carl Shan
Day 13: Transparent Origami
"""

data = open('day13.in', 'r').read().strip().split('\n')
coords = [(int(elem[0]), int(elem[1])) for elem in [line.split(',') for line in data if line and line[0] != 'f']]
folds = [line for line in data if line and line[0] == 'f']

def apply_folds(coords, folds):

    for fold in folds:
        value = int(fold.split('=')[1])
        new_coords = set()
        for coord in coords:
            x, y = coord
            is_x = 'x' in fold
            to_reflect = x if is_x else y
            if to_reflect <= value:
                new_coords.add((x, y))
                continue
            diff = (to_reflect - value)
            if is_x:
                new_coords.add((x - 2 * diff, y))
            else:
                new_coords.add((x, y - 2 * diff))
        coords = list([coord for coord in new_coords if coord[0] >= 0 and coord[1] >= 0])


    return coords

def print_coords(coords):
    min_x = min(coord[0] for coord in coords)
    min_y = min(coord[1] for coord in coords)
    max_x = max(coord[0] for coord in coords)
    max_y = max(coord[1] for coord in coords)

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in coords:
                print('#', end='')
            else:
                print('.', end='')
        print()

folded_coords = apply_folds(coords, folds)
print_coords(folded_coords)
