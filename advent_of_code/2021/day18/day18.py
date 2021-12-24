"""
Advent of Code 2021
Author: Carl Shan
Day 18: Snailfish
"""

data = open('day18.ex', 'r').read().split('\n')

snailfish = list(map(eval, data))


test_explode1 = [[[[[9,8],1],2],3],4]
test_explode2 = [7,[6,[5,[4,[3,2]]]]]
test_explode3 = [[6,[5,[4,[3,2]]]], 1]
test_explode4 = [[3,[2,[1,[7,3]]]], [6,[5,[4,[3,2]]]]]
test_explode5 = [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]

"""
Ideas:
- Recursive

Store the first and second in a list
and check if the lists are empty.

If so, continue recursing until the top.

However, if not, at the first instance when we can find a number adjacent we add the relevant left or right number.
"""

def explode(snailfish, depth, left, right):
    # Recursive attempt
    # It works for test_explode1 and 2 but not for the rest
    first = snailfish[0]
    second = snailfish[1]
    if type(first) == int and type(second) == int and depth > 3:
        left.append(first)
        right.append(second)
        return None
    elif type(first) == list and type(second) == int:
        explode(first, depth + 1, left, right)
        if left: # what do I do here?
            pass
        if right:
            snailfish[1] += right.pop()
            # snailfish[0] = 0
        return None
    elif type(first) == int and type(second) == list:
        explode(second, depth + 1, left, right)
        if left:
            snailfish[0] += left.pop()
            # snailfish[1] = 0
        if right: # what do I do here?
            pass
        return None
    else: # both lists
        return None, None

print(test_explode1)
explode(test_explode1, 1, [], [])
print(test_explode1)

print(test_explode2)
explode(test_explode2, 1, [], [])
print(test_explode2)

def explode_iterative(snailfish):
    # Iterative attempt
    left = []
    right = []
    first, second = snailfish
    while type(first) != int and type(second) != int:
        if type(first) == int:
            left.append(first)
            first, second = second
        elif type(second) == int:
            right.append(second)
            first, second = first
        else: # both are lists
            pass