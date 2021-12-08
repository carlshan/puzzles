"""
Advent of Code
Author: Carl Shan
Day 8
"""

aoc_input = open("day8.in", "r").readlines()
CORRECT_WIRING = {'abcefg': '0',
 'cf': '1',
 'acdeg': '2',
 'acdfg': '3',
 'bcdf': '4',
 'abdfg': '5',
 'abdefg': '6',
 'acf': '7',
 'abcdefg': '8',
 'abcdfg': '9'
}



def count_num_1478(line):
    output_values = line.strip().split(' | ')[1].split(' ')
    count = 0
    for value in output_values:
        if len(value.strip()) in (2, 4, 3, 7):
            count += 1

    return count

def part1(aoc_input):
    count = 0
    for line in aoc_input:
        num_line = count_num_1478(line)
        # print(line, ' : ', num_line)
        count += num_line
    return count

def in_one_but_not_two(str1, str2):
    """
    Returns the string that is in str1 but not in str2 (or vice versa)
    """
    return ''.join(sorted(list(set(str1) - set(str2)))) if len(str1) > len(str2) else ''.join(sorted(list(set(str2) - set(str1))))

def figure_out_a(two, three):
    """
    Given two strings of length 2 and 3 (representing 1 and 7), return the letter that is in three but not in two.

    This letter represents 'a'
    """
    return ''.join([letter for letter in three if letter not in two])


def figure_out_g(four, six1, six2, six3, known_a):
    """
    Given the four-letter string representing 4, and three six-letter strings (representing 0, 6 and 9) figure out the letter representing g.

    The letter representing 'g' is the letter in the six representing 9 that is not equal to known_a.

    First, figure out the six-letter string representing the number 9.

    The unique property here is that all four letters in four must be in the string representing 9.
    """
    true_nine = None
    for six in [six1, six2, six3]:
        for letter in four:
            if letter not in six:
                break
        else:
            true_nine = six

    return ''.join([letter for letter in true_nine if letter != known_a and letter not in four])

def figure_out_d(two, five1, five2, five3, known_a, known_g):
    for letter in two + known_a + known_g:
        five1 = five1.replace(letter, '')
        five2 = five2.replace(letter, '')
        five3 = five3.replace(letter, '')

    for letter in list(set(five1 + five2 + five3)):
        count = 0
        for five in [five1, five2, five3]:
            if letter in five:
                count += 1
        if count == 3:
            return letter

def figure_out_b(three, four, known_d):
    """
    This function must run after d is known.

    Given two strings of length 3 and 4 (reprsenting 7 and 4), return the letter representing b.
    """
    return ''.join([letter for letter in four if letter not in three and letter != known_d])

def figure_out_f(two, five1, five2, five3, known_a, known_b, known_d):
    """
    Given three known letters representing d, a, and b
    Figure out which of the five-letter strings is the number 5 (as it will have d a and b)

    Then compare this with the two-letter string (representing 1).

    Whatever character they have in common represents 'f'
    """
    dab = known_d + known_a + known_b
    true_five = None
    for five in [five1, five2, five3]:
        for letter in dab:
            if letter not in five:
                break
        else:
            true_five = five
            break

    return ''.join([letter for letter in two if letter in true_five])

def figure_out_c(two, known_f):
    """
    Given the two-letter string representing 1, figure out the letter representing c.
    """
    return ''.join([letter for letter in two if letter != known_f])


def figure_out_e(seven, known_a, known_b, known_c, known_d, known_f, known_g):
    """
    Given the seven-letter string representing 8, figure out the letter representing e.
    """
    return ''.join([letter for letter in seven if letter not in known_a + known_b + known_c + known_d + known_f + known_g])


def figure_out_all_letters(recorded_values):
    """
    Returns a map representing all letters representing 'a', 'b', 'c', 'd', 'e', 'f', and 'g'
    """
    # Representing 1
    two = ''.join([elem for elem in recorded_values if len(elem) == 2])
    three = ''.join([elem for elem in recorded_values if len(elem) == 3])
    four = ''.join([elem for elem in recorded_values if len(elem) == 4])
    five1, five2, five3 = [elem for elem in recorded_values if len(elem) == 5]
    six1, six2, six3 = [elem for elem in recorded_values if len(elem) == 6]
    seven = ''.join([elem for elem in recorded_values if len(elem) == 7])

    known_a = figure_out_a(two, three)
    known_g = figure_out_g(four, six1, six2, six3, known_a)
    known_d = figure_out_d(two, five1, five2, five3, known_a, known_g)
    known_b = figure_out_b(three, four, known_d)
    known_f = figure_out_f(two, five1, five2, five3, known_a, known_b, known_d)
    known_c = figure_out_c(two, known_f)
    known_e = figure_out_e(seven, known_a, known_b, known_c, known_d, known_f, known_g)

    return {
        known_a: 'a',
        known_b: 'b',
        known_c: 'c',
        known_d: 'd',
        known_e: 'e',
        known_f: 'f',
        known_g: 'g'
    }


def part2(aoc_input):
    tot = 0
    for line in aoc_input:
        recorded_values, output = line.strip().split(' | ')
        recorded_values = recorded_values.split(' ')
        output = output.split(' ')
        mappings = figure_out_all_letters(recorded_values)

        decoded_num = ''
        for num in output: # each num represents one digit
            decoded_digit = ''
            for letter in num:
                decoded_digit += mappings[letter]

            decoded_num += CORRECT_WIRING[''.join(sorted(decoded_digit))]
        decoded = int(decoded_num)
        print(recorded_values, decoded)
        tot += decoded

    return tot




# print(part1(aoc_input))
print(part2(aoc_input))