"""
1. For the first digit:
    - x = 1
    - y += the first digit
    - z += the first digit
2. For the second digit
    - set x = 0
    - x = 1
    - z *= 26
    - y = the second digit + 3
    - z += y
3. For the third digit
    - x = 1
    - z *= 26
    - y = the third digit + 8
    - z += y
4. For the fourth digit
    - x = 1
    - y = (the fourth digit + 5)
    - z += y
5. For the fifth digit
    - x = 1
    - z *= 26
    - y = the fifth digit
    - y += 13
    - z += y
6. For the sixth digit
    - x = 0
    - x = z % 26
    - z *= 26
    - y = the sixth digit
    - y += 9
    - z += y
7. For the seventh digit
    - x = 1
    - z *= 26
    - y = the seventh digit
    - y += 6
    - z += y
8. For the eighth digit
    - x = z % 26
    - z /= 26
    - x -= 14
    - x = 1 if x is NOT eighth digit, else 0
    - y = (25 * x) + 1
    - z *= y
    - y = (the eighth digit + 1) * x
    - z += y
9. For the ninth digit
    - x = 0
    - x = (z % 26) - 8
    - z /= 26
    - x = 1 if x is NOT ninth digit, else 0
    - y = (25 * x) + 1
    - z *= y
    - y = (the ninth digit + 1) * x
    - z += y
10. For the tenth digit
    - x = 1
    - z *= 26
    - y = the tenth digit + 2
    - z += y
11. For the eleventh digit
    - x = z % 26
    - z /= 26
    - x = 1 if x is NOT eleventh digit, else 0
    - y = (25 * x) + 1
    - z *= y
    - y = (the eleventh digit + 7) * x
    - z += y
12. For the twelfth digit
    - x = (z % 26) - 5
    - z /= 26
    - x = 1 if x is NOT twelfth digit, else 0
    - y = (25 * x) + 1
    - z *= y
    - y = (the twelfth digit + 5) * x
    - z += y
13. For the thirteenth digit
    - x = (z % 26) - 9
    - z /= 26
    - x = 1 if x is NOT thirteenth digit, else 0
    - y = (25 * x) + 1
    - z *= y
    - y = (the thirteenth digit + 8) * x
    - z += y
14. for the fourteenth digit
    - x = (z % 26) - 1
    - z /= 26
    - x = 1 if x is NOT fourteenth digit, else 0
    - y = (25 * x) + 1
    - z *= y
    - y = (the thirteenth digit + 15) * x
    - z += y

Finally, see if z == 0
"""

"""
Needed hints from: https://github.com/mrphlip/aoc/blob/master/2021/24.md

z = []
w = input()
z.push(w)

w = input()
z.push(w + 3)

w = input()
z.push(w + 8)

w = input()
if w != z.pop() - 5:
    z.push(w + 5)

w = input()
z.push(w + 13)

w = input()
z.push(w + 9)

w = input()
z.push(w + 6)

w = input()
if w != z.pop() - 14:
    z.push(w + 1)

w = input()
if w != z.pop() - 8:
    z.push(w + 1)

w = input()
z.push(w + 2)

w = input()
if w != z.pop():
    z.push(w + 7)

w = input()
if w != z.pop() - 5:
    z.push(w + 5)

w = input()
if w != z.pop() - 9:
    z.push(w + 8)

w = input()
if w != z.pop() - 1:
    z.push(w + 15)


A - 1 = N
B - 6 = M
C + 3 = D
E + 8 = L
F + 1 = I
G - 8 = H
J + 2 = K
"""
[
    2, # A
    7, # B
    1, # C
    4, # D
    1, # E
    1, # F
    9, # G
    1, # H
    2, # I
    1, # J
    3, # K
    9, # L
    1, # M
    1 # N
]