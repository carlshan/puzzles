"""
Advent of Code 2021
Author: Carl Shan
Day 23: Amphipod
"""

"""Example 1:
#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
"""

VALID_STATE = [
    '.',
    '.',
    ['A', 'A'],
    '.',
    ['B', 'B'],
    '.',
    ['C', 'C'],
    '.',
    ['D', 'D'],
    '.',
    '.'
]

# The amount it costs to move each type of amphipod a single step.
ENERGY_COSTS = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000,
}

AMPHIPOD_LISTS = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8,
}

data = open('day23.in2', 'r').read().strip().split('\n')

def parse_input(data):
    parsed = ['.', '.', [], '.', [], '.', [], '.', [], '.', '.']
    ind = 2
    for line in data[2:]:
        clean = list(line.strip().replace('#', ''))
        for c in clean:
            parsed[ind].append(c)
            if ind == 8:
                ind = 2
            else:
                ind += 2

    return parsed

initial_state = parse_input(data)

def in_final_state(state):
    """
    Returns a boolean indicating whether the amphipods are in their correct state or not.
    """

    amphipods = ['A', 'B', 'C', 'D']
    ind = 0
    for elem in state:
        if isinstance(elem, list):
            if len(elem) > 0 and len(elem) != len(list(filter(lambda x: x == amphipods[ind], elem))):
                return False

            ind = (ind + 1) % len(amphipods)

    return True

def get_valid_hallway_moves_helper(state, l, increment, valid_moves):
    temp = l + increment
    while temp < len(state) and state[temp] not in ('A', 'B', 'C', 'D'):
        if state[temp] == '.':
            valid_moves.append((temp, None))
        if isinstance(state[temp], list) and l == AMPHIPOD_LISTS[state[l]]: # The amphipod can move into the list
            if state[temp][0] == '.' and state[temp][1] == '.':
                valid_moves.append((temp, 1))
            elif state[temp][0] == '.' and state[temp][1] != '.':
                valid_moves.append((temp, 0))
            else:
                pass

        temp += increment

def get_valid_moves(state, l, i=None):
    """
    Given a state, find all valid moves for the amphipod at index l. If index l is a list, then we need to get valid moves for the amphipod at index i in l.
    """
    valid_moves = []

    if state[l] == '.':
        raise Exception('Invalid move: Attempting to move an empty space')

    if i is not None and l not in (2, 4, 6, 8): # amphipods can only be in one of these lists
        raise ValueError('Invalid list index')

    if i is not None and i not in (0, 1): # amphipods can only be in one of these indices
        raise ValueError('Invalid amphipod index')

    # Handle case of amphipod in hallway
    # In that case, we need to find all the empty adjacent spaces that are not blocked by an existing amphipod and add them to the valid moves
    if i is None and l not in (2, 4, 6, 8):
        get_valid_hallway_moves_helper(state, l, 1, valid_moves)  # considers all moves to the right
        get_valid_hallway_moves_helper(state, l, -1, valid_moves) # considers all moves to the left
    elif i is not None: # Handle case of amphipod in a list
        assert l in (2, 4, 6, 8)
        if i == 0:
            if state[l][1] == '.':
                valid_moves.append((l, 1))
        elif i == 1:
            if state[l][0] == '.':
                valid_moves.append((l, 0))



def minimum_energy(state):
    """
    Given a state of amphipods, return the minimum amount of energy required
    to move each of the 'A', 'B', 'C', and 'D' amphipods to their relevant list.

    This function works recursively.

    Constraints:
        - Amphipods, once in the hallway, will not be able to enter a list unless it's their relevant list (the first for 'A', second for 'B', and so on)
        - Amphipods will stay in that spot until it can move into a room
        - Amphipods cannot "skip" over another one in the hallway to move into their relevant list
    """

    # Base success case: There are no amphipods left in the hallway and all the amphipods are in the correct list.
    # Return 0 as it requires no energy to move the amphipods to their correct lists.
    if in_final_state(state):
        return 0

    # Recursive case:
    # For each amphipod, try each possible move.