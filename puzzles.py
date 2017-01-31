# This is a piece of scratch paper to work on arbitrary puzzles like e.g.,
# the ones on Project Euler
import math


# Exercises below from: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-s096-effective-programming-in-c-and-c-january-iap-2014/getting-started/MIT6_S096IAP14_diagnostic.pdf


def is_prime(n):
    # Returns if a number is prime
    # Definition of prime: only divisible by 1 and itself
    for elem in xrange(2, math.sqrt(n)):
        if n % elem == 0:
            return False
    return True


def helper_permute(lst):
    # Given a list of numbers, this function prints the permutations
    # of this list of numbers.
    if len(lst) == 1:
        return str(lst[0])
    elif len(lst) == 0:
        return ''
    else:
        val = str(lst[0]) + helper_permute(lst[1:])
        print val
        return str(val)


def print_permutations(n):
    if n == 1:
        print(1)
        return 1
    else:
        nums = range(1, n+1)
        for num in nums:
            first_element =1
    pass


def search(value, lst):
    for index, elem in enumerate(lst):
        if value == elem:
            return index
    return None


def binary_search(value, lst):
    # searches value in lst that takes O(log(value)) time
    pass
