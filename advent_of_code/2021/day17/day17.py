"""
Advent of Code 2021
Author: Carl Shan
Day 17: Trick Shot
"""

data = open('day17.in', 'r').read().strip()
x_start, x_stop = data.split(': ')[1].split(', ')[0].split('x=')[1].split('..')
y_start, y_stop = data.split(': ')[1].split(', ')[1].split('y=')[1].split('..')

x_start = int(x_start)
x_stop = int(x_stop)
y_start = int(y_start)
y_stop = int(y_stop)

# Generating all valid combinations of positions to check against
valid_positions = set()
for x in range(x_start, x_stop + 1):
    for y in range(y_start, y_stop + 1):
        valid_positions.add((x, y))

def highest_y(velocity_y):
    """
    Given the y-component of a velocity, returns the highest y-value that is reached.
    This occurs when the y-component of the velocity is 0.

    So to get the position we can sum the y-component of the velocity from 1 to its value.
    """
    return sum(range(velocity_y + 1))

def y_after_n_steps(velocity_y, n):
    """
    Returns the y-position after n steps, assuming we started with velocity_y
    """
    start_y = 0
    for _ in range(n):
        start_y += velocity_y
        velocity_y -= 1
    return start_y

def step_x(velocity_x):
    new_x = velocity_x

    if new_x < 0:
        new_x += 1
    elif new_x > 0:
        new_x -= 1

    return new_x

def steps_to_land(velocity_x, x_start, x_stop):
    """
    Given a starting velocity_x, returns a list of the number of steps it takes to land in between start_x and stop_x
    """
    steps = []
    x_pos = 0
    num_steps = 0
    while x_pos <= x_stop:
        x_pos += velocity_x
        velocity_x = step_x(velocity_x)
        num_steps += 1
        if x_pos >= x_start:
            steps.append(num_steps)

        if velocity_x == 0: # End of moving in the x-direction
            break

    return steps


def step(velocity):
    """
    Given x, y representing the velocity in the x and y-directions,
    returns the new velocity after one step.

    The new velocity is calculated as:
        - The x velocity changes by 1 towards the value 0 (and stays the same if it is already 0)
        - The y velocity decreases by 1
    """
    x, y = velocity
    new_x = x
    new_y = y - 1

    if new_x < 0:
        new_x += 1
    elif new_x > 0:
        new_x -= 1

    return (new_x, new_y)

def change_pos(pos, velocity):
    return (pos[0] + velocity[0], pos[1] + velocity[1])

def is_valid(start_pos, velocity, valid_positions):
    """
    Given a velocity, returns if it eventually lands in the valid_positions after 100 steps.
    """
    pos = start_pos
    for _ in range(1, 1000):
        pos = change_pos(pos, velocity)
        # print(pos)
        if pos in valid_positions:
            return True
        velocity = step(velocity)
    return False

def part1(valid_positions, x_stop):
    # Brute force solution
    start_pos = (0, 0)
    highest = 0
    for x in range(1, x_stop + 1):
        for y in range(0, 1000):
            velocity = (x, y)
            if is_valid(start_pos, velocity, valid_positions):
                # print(velocity, highest_y(y))
                highest = max(highest, highest_y(y))
    return highest


def part2(valid_positions, x_stop, y_start):
    # Brute force solution
    start_pos = (0, 0)
    counter = 0
    for x in range(1, x_stop + 1):
        for y in range(y_start, -y_start):
            velocity = (x, y)
            if is_valid(start_pos, velocity, valid_positions):
                counter += 1
    return counter

# print(part1(valid_positions, x_stop))
print(part2(valid_positions, x_stop, y_start))