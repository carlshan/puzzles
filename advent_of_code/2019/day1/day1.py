fileName = "day1.in"
data = map(lambda s: int(s.replace('\n', '')), open(fileName, 'r+').readlines())

# Part 1
import math

def get_fuel(mass):
    return math.floor(mass / 3) - 2

print(sum(map(get_fuel, data)))

# Part 2
def get_fuel_recur(mass, acc=0):
    result = get_fuel(mass)
    if math.floor(result / 3) < 2:
        return result + acc
    else:
        return get_fuel_recur(result, result+acc)

print(sum(map(get_fuel_recur, data)))
