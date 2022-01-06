"""
Advent of Code 2020
Author: Carl Shan
Day 4: Passport Processing
"""
data = open('day4.in').read().split('\n\n')


def parse_data(row):
    passports = dict()
    pairs = row.split(' ')
    for pair in pairs:
        key, val = pair.split(':')
        passports[key] = val
    return passports


data = [parse_data(row.replace('\n', ' ')) for row in data]


def byr_rules(passport):
    """
    Returns True if the passport is valid.

    A passport is valid if the birth year is at least 7 digits long and the
    birth year is a number that is within the range of 1920 to 2002.
    """
    return len(passport['byr']) == 4 and 1920 <= int(passport['byr']) <= 2002


def iyr(passport):
    """
    Returns True if the passport is valid.

    A passport is valid if the issue year is at least 9 digits long and the
    issue year is a number that is within the range of 2010 to 2020.
    """
    return len(passport['iyr']) == 4 and 2010 <= int(passport['iyr']) <= 2020


def eyr(passport):
    """
    Returns True if the passport is valid.

    A passport is valid if the expiration year is at least 5 digits long and
    the expiration year is a number that is within the range of 2020 to 2030.
    """
    return len(passport['eyr']) == 4 and 2020 <= int(passport['eyr']) <= 2030


def hgt(passport):
    """
    Returns True if the passport is valid.

    A passport is valid if the height is a number that is within the range of 150 to 193 if in cm, or between 59 and 76 if in inches.
    """
    if 'cm' == passport['hgt'][-2:]:
        return 150 <= int(passport['hgt'][:-2]) <= 193
    elif 'in' == passport['hgt'][-2:]:
        return 59 <= int(passport['hgt'][:-2]) <= 76
    else:
        return False


def hcl(passport):
    """
    Returns True if the passport is valid.

    A passport is valid if the hair color is a valid hexadecimal color code.
    """
    return passport['hcl'][0] == '#' and len(passport['hcl']) == 7 and all(c in '0123456789abcdef' for c in passport['hcl'][1:])


def ecl(passport):
    """
    Returns True if the passport is valid.

    A passport is valid if the eye color is one of the following:
        amb (ambiguous)
        blu (blue)
        brn (brown)
        gry (gray)
        grn (green)
        hzl (hazel)
        oth (other)
    """
    colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    counts = 0
    for color in colors:
        counts += int(color in passport['ecl'])
    return counts == 1


def pid(passport):
    """
    Returns True if the passport is valid.

    A passport is valid if the passport ID exactly 9 digits long and
    contains only digits.
    """
    return len(passport['pid']) == 9 and passport['pid'].isdigit()


def count_valid(data):
    """
    Returns the number of passports that are valid.

    A valid passport must contain each of the following required fields:
        byr (Birth Year)
        iyr (Issue Year)
        eyr (Expiration Year)
        hgt (Height)
        hcl (Hair Color)
        ecl (Eye Color)
        pid (Passport ID)
    """
    fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    counter = 0
    for passport in data:
        counter += int(len(fields.intersection(passport.keys())) == len(fields)
                        and byr_rules(passport)
                        and iyr(passport)
                        and eyr(passport)
                        and hgt(passport)
                        and hcl(passport)
                        and ecl(passport)
                        and pid(passport))

    return counter


print(count_valid(data))
