"""
Advent of Code 2020
Author: Carl Shan
Day 18: Operation Order
"""

import operator
OPS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

equations = open('day18.in', 'r').read().split('\n')


def clean_eq(eq):
    """
    Cleans an equation by removing spaces.
    """
    return eq.replace(' ', '')


def get_ind_of_closing_paren(eq, start):
    """
    Returns the index of the closing parenthesis of the equation.
    """
    paren_count = 0
    for i in range(start, len(eq)):
        if eq[i] == '(':
            paren_count += 1
        elif eq[i] == ')':
            paren_count -= 1
            if paren_count == 0:
                return i
    return None  # Did not find ind


def add_parentheses_to_addition(eq):
    """
    Given an equation that contains addition, subtraction with existing parentheses,
    wrap each addition operation with parentheses.
    """
    eq = clean_eq(eq)
    i = 0
    while i < len(eq):
        char = eq[i]
        if char == '+':
            # Find the index of the previous operand
            # Find the index of the next operand
            # Wrap everything between the previous and next with parentheses
            prev_ind = i - 1
            while prev_ind >= 0:
                prev_char = eq[prev_ind]
                if prev_char == ')':  # we should stop here
                    prev_ind = None   # break out of loop with an invalid index
                    break
                elif prev_char.isdigit():
                    break

            next_ind = i + 1
            while next_ind < len(eq):
                next_char = eq[next_ind]
                if next_char == '(':  # we should stop here
                    next_ind = None
                    break
                elif next_char.isdigit():
                    next_ind += 1     # this can be greater than the length of the string if we are at the end
                    break
            if prev_ind is not None and next_ind is not None:
                prev_ind = max(prev_ind, 0)  # handling case of negative
                eq = eq[:prev_ind] + '(' + eq[prev_ind:next_ind] + ')' + eq[next_ind:]
                i = next_ind + 3
            else:
                i += 1
        else:
            i += 1
    return eq


def recursively_eval_eq(eq):
    eq = clean_eq(eq)
    # Base case: no more operations
    if len(eq) == 0:
        return tot

    # Recursive case: operations remaining
    stack = []
    i = 0
    while i < len(eq):
        char = eq[i]
        if char.isdigit():
            stack.append(int(char))
            i += 1
        elif char in OPS:
            # Pop the top two values from the stack
            # and apply the operation
            op1 = stack.pop()
            if eq[i + 1].isdigit():
                op2 = int(eq[i + 1])
                i += 2
            else:  # Handle the case of parentheses
                closing_ind = get_ind_of_closing_paren(eq, i)
                op2 = recursively_eval_eq(eq[i + 2:closing_ind])
                i = closing_ind + 1
            stack.append(OPS[char](op1, op2))
        else:  # Encountered parentheses
            closing_ind = get_ind_of_closing_paren(eq, i)
            stack.append(recursively_eval_eq(eq[i + 1:closing_ind]))
            i = closing_ind + 1

    return stack.pop()


def solve1(equations):
    tot = sum(recursively_eval_eq(eq) for eq in equations)
    return tot


def solve2(equations):
    tot = sum(recursively_eval_eq(add_parentheses_to_addition(eq)) for eq in equations)
    return tot


print(solve2(equations))