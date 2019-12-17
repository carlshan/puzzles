# Let's call a triplet of natural numbers "obscure" if one cannot uniquely
# deduce them from their sum and product.
# For example, {2,8,9} is an obscure triplet,
# because {3,4,12} shares the same sum (19) and the same product (144).
#
# Find a triplet of ages {a,b,c} that is obscure and stays
# obscure for three more years: {a+1,b+1,c+1}, {a+2,b+2,c+2} and {a+3,b+3,c+3}.

# For a given triplet, find the sum and product
# Look inside a dictionary that is keyed on the sum and product
# if it already exists, this triplet is not obscure
# else, this triplet is obscure
# append it to a list
# search through all 100^3 combinations

# obscure_triplets = []
import itertools

sumprods = {}

endRange = 101

def product(t):
    if len(t) == 1:
        return t[0]
    else:
        return t[0] * product(t[1:])

# This generates the full list of all possible ages:
combinations = itertools.combinations(range(1, endRange), 3)
#print(combinations)
for triplet in combinations:
    sumCheck = sum(triplet)
    prodCheck = product(triplet)
    key = str(sumCheck) + ',' + str(prodCheck)
    if key not in sumprods: # we have not seen that particular sum and product yet
        sumprods[key] = [triplet]
    else:
        sumprods[key].append(triplet)



# Now we have all possible ages, and their sum and products
# The obscure ages are the ones where there are multiple triplets that belong

obscure_list_of_lists = {k: v for k, v in sumprods.items() if len(v) > 1}.values()

def extend(list_of_lists):
    extended_list = []
    for l in list_of_lists:
        extended_list.extend(l)
    return extended_list

obscures = extend(obscure_list_of_lists)

#print(obscures)

def is_answer(triplet):
    y1 = (triplet[0] + 1, triplet[1] + 1, triplet[2] + 1)
    y2 = (triplet[0] + 2, triplet[1] + 2, triplet[2] + 2)
    y3 = (triplet[0] + 3, triplet[1] + 3, triplet[2] + 3)
    return y1 in obscures and y2 in obscures and y3 in obscures

#answer = filter(lambda triplet: is_answer(triplet), obscures)
#print(list(answer))


### Checking my answer
answer1 = (7, 30, 54)
key1 = '91,11340'
print(sumprods[key1])

y1 = (8, 31, 55)
key2 = str(sum(y1)) + ',' + str(product(y1))
print(sumprods[key2])

y2 = (9, 32, 56)
key3 = str(sum(y2)) + ',' + str(product(y2))
print(sumprods[key3])

y3 = (10, 33, 57)
key4 = str(sum(y3)) + ',' + str(product(y3))
print(sumprods[key4])
