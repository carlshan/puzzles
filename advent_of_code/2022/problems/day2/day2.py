
def convert_to_nums(s):
    if s == 'A' or s == 'X': return 0
    elif s == 'B' or s == 'Y': return 1
    else: return 2

data = open("day2.data", 'r+').read().split('\n')
split = [elem.split() for elem in data]
nums = [
    [convert_to_nums(elem[0]), convert_to_nums(elem[1])]
    for elem in split
]

def calc_points(l):
    first = l[0]
    second = l[1] + 1
    diff = second - first

    return second + ((diff % 3) * 3)

points = [calc_points(elem) for elem in nums]

print(sum(points))