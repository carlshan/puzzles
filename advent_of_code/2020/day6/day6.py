"""
Advent of Code 2020
Author: Carl Shan
Day 6: Custom Customs
"""

answers = open('day6.in', 'r').read().split('\n\n')


def count_letters(answer):
    return len(set(answer.replace('\n', '')))


def total_counts(answers):
    counts = list(map(count_letters, answers))
    return sum(counts)


def count_all_yes(answers):
    def count_yes(answer):
        group_size = answer.count('\n') + 1
        count = 0
        for letter in set(answer):
            if answer.count(letter) == group_size:
                count += 1
        return count

    return sum(list(map(count_yes, answers)))

print(total_counts(answers)) # part 1
print(count_all_yes(answers)) # part 1