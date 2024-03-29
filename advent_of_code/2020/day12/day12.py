"""
Advent of Code 2020
Author: Carl Shan
Day 12: Rain Risk
"""

directions = open('day12.in', 'r').read().splitlines()
directions = [(elem[0], int(elem[1:])) for elem in directions]

start = 'east'
distances = {
    'E': 0,
    'N': 0,
    'W': 0,
    'S': 0
}


def get_manhattan_distance(distances):
    return abs(distances['E'] - distances['W']) + abs(distances['N'] - distances['S'])


def execute_instructions(instructions, distances):  # part 1
    facing = ['E', 'S', 'W', 'N']
    curr = 'E'
    new_distances = distances.copy()
    for ins in instructions:
        f, dist = ins
        if f == 'F':
            new_distances[curr] += dist
        elif f in ('L', 'R'):
            num_rotation = dist // 90 * (1 if f == 'R' else -1)
            curr = facing[(facing.index(curr) + num_rotation) % 4]
        else:  # is E, S, W or N
            new_distances[f] += dist
    return new_distances

distances1 = execute_instructions(directions, distances)  # part 1
print(get_manhattan_distance(distances1))

waypoint = {
    'E': 10,
    'N': 1,
    'S': 0,
    'W': 0
}


def rotate_waypoint(direction, amt, waypoint):
    facing = ['E', 'S', 'W', 'N']
    dirs = [(way, facing.index(way)) for way in waypoint.keys()]
    num_rotation = amt // 90 * (1 if direction == 'R' else -1)

    new_waypoint = {'E': 0, 'N': 0, 'S': 0, 'W': 0}
    for direction in dirs:
        way, ind = direction
        new_waypoint[facing[(ind + num_rotation) % 4]] = waypoint[way]

    return new_waypoint


def execute_instructions2(instructions, distances, waypoint):  # part 2
    facing = ['E', 'S', 'W', 'N']
    for ins in instructions:
        f, dist = ins
        if f == 'F':
            for key in distances:
                distances[key] += dist * waypoint[key]
        elif f in ('L', 'R'):
            waypoint = rotate_waypoint(f, dist, waypoint)
        else:  # is E, S, W or N
            waypoint[f] += dist
    return distances


distances2 = execute_instructions2(directions, distances, waypoint)  # part 2
print(get_manhattan_distance(distances2))