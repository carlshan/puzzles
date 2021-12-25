"""
Advent of Code 2021
Author: Carl Shan
Day 21: Dirac Dice
"""
from collections import defaultdict

num_rolls = 1

def roll_dice():
    global num_rolls
    result = num_rolls % 100
    if result == 0: # handling the case of rolling 100
        return 100
    return result

def take_turn():
    """
    Each turn rolls the dice 3 times.
    """
    global num_rolls
    dice_rolls = []
    for _ in range(3):
        dice_rolls.append(roll_dice())
        num_rolls += 1
    return sum(dice_rolls)

def move_forward(curr, steps):
    """
    Given the curr position (1-10), move forward the given number of steps, wrapping around the board
    after 10.
    """
    pos = (curr + steps) % 10
    if pos == 0: # to handle the case of landing exactly on 10
        return 10
    return pos

def play_game():
    """
    Simulates playing the game of Dirac Dice in Part 1.
    """
    player_1_score = [0]
    player_2_score = [0]

    player_1_pos = [4]
    player_2_pos = [6]

    roll_counter = 0

    curr_player = 1 # player 1 starts

    while player_1_score[0] < 1000 and player_2_score[0] < 1000:
        steps          = take_turn()
        roll_counter   += 3
        curr           = player_1_pos   if curr_player == 1 else player_2_pos
        curr_score     = player_1_score if curr_player == 1 else player_2_score
        new_pos        = move_forward(curr[0], steps)
        curr[0]        = new_pos
        curr_score[0]  += curr[0]
        print("Player {} rolls a total of {} and moves to space {} for a total score of {}".format(curr_player, steps, new_pos, curr_score[0]))
        curr_player    = 2 if curr_player == 1 else 1 # swaps the player

    return roll_counter

# Part 2
# The game is now played with a new rule:
# The goal is to simply reach at least 21 points.
# However, there are now three possibilities for each roll: 1, 2 or 3.
# I will try a recursive implementation.

player_1_score = 0
player_2_score = 0

player_1_pos = 4
player_2_pos = 6

cache = defaultdict(int)
def play_dirac_dice(p1score, p2score, p1pos, p2pos):
    # Base case: if p1's score is 21 or more, p1 wins
    if p1score >= 21:
        return (1, 0) # represents the (# of universes where p1 wins, # of universes where p2 wins)

    # Base case: same for p2
    if p2score >= 21:
        return (0, 1)

    key = (p1score, p2score, p1pos, p2pos)
    if key in cache:
        return cache[key]

    # Recursive case:
    # If it's p1's turn, return the sum of all wins occuring under the three possible outcomes
    wins = (0, 0)
    for roll1 in [1, 2, 3]:
        for roll2 in [1, 2, 3]:
            for roll3 in [1, 2, 3]:
                x1, y1 = play_dirac_dice(p2score, p1score + move_forward(p1pos, roll1 + roll2 + roll3), p2pos, move_forward(p1pos, roll1 + roll2 + roll3))
                wins = (wins[0] + y1, wins[1] + x1)
    cache[key] = wins
    return wins

    # if is_p1_turn:

    #     return sum([play_dirac_dice(p1score + move_forward(p1pos, i), p2score, move_forward(p1pos, i), p2pos, not is_p1_turn) for i in range(1, 4)])
    # else:
    #     return sum([play_dirac_dice(p1score, p2score + move_forward(p2pos, i), p1pos, move_forward(p2pos, i), not is_p1_turn) for i in range(1, 4)])

print(play_dirac_dice(player_1_score, player_2_score, player_1_pos, player_2_pos))

