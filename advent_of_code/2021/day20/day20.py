"""
Advent of Code
Author: Carl Shan
Day 20: Trench Map
"""

from collections import Counter
import numpy as np
from scipy.ndimage import convolve

enhance, _, *image = open('day20.in', 'r').read().strip().splitlines()
image = [list(row) for row in image]

def get_locations_of_char(image, char):
    """
    Creates a set of coordinates for each pixel that matches the character.
    """
    locations = set()
    for y in range(len(image)):
        for x in range(len(image[y])):
            if image[y][x] == char:
                locations.add((y, x))
    return locations

def in_image(image, coord):
    """
    Given an image and a coordinate, return whether the coordinate is within the image.
    """
    x, y = coord
    return 0 <= y < len(image) and 0 <= x < len(image[0])

def get_image_data(image, coord, locs, default):
    """
    Given an input coordinate, return the 9 characters surrounding and including this point on the input image.
    """
    image_data = ""
    x, y = coord

    for i in range(y - 1, y + 2):
        for j in range(x - 1, x + 2):
            if (i, j) in locs:
                image_data += '#'
            else:
                image_data += '.'
                # if in_image(image, (i, j)):
                #     image_data += '.'
                # else:
                #     image_data += default
    return image_data

def convert_to_binary(char):
    if char == '#':
        return '1'
    return '0'

def get_output_char(image, coord, enhance, locs, default):
    """
    Given the coordinates of a point on the output image,
    find the 9 characters surrounding and including this point on the input image
    and apply the enhancement algorithm to find the output coordinate.
    """
    image_data = "".join(map(convert_to_binary, get_image_data(image, coord, locs, default)))
    ind = int(image_data, 2)
    return enhance[ind]

def generate_output_image(image, enhance, default):
    """
    Given an image, apply the enhacement algorithm to each coordinate in the input image.
    """
    output_image = []
    padded = np.pad(image, (2, 2), 'constant', constant_values=default)
    locs = get_locations_of_char(padded, '#')
    for y in range(len(padded)):
        output_image.append([])
        for x in range(len(padded[y])):
            output_image[y].append(get_output_char(image, (x, y), enhance, locs, default))
    return output_image

def count_pixels(image, char):
    """
    Given an image and a character, count the number of pixels that match the character.
    """
    return sum(1 for row in image for pixel in row if pixel == char)

# Applying the enhancement twice

output1 = generate_output_image(image, enhance, '.')
output2 = generate_output_image(output1, enhance, '.')

print(count_pixels(output2, '#')) # this isn't returning the right answer for part 1 yet :(

"""
# Solution below credited to: https://www.reddit.com/r/adventofcode/comments/rkf5ek/comment/hp9mvao/
enhance, _, *image = open('day20.in', 'r').read().strip().splitlines()
enhance = np.array([int(p=="#") for p in enhance])
image = np.pad([[int(p=="#") for p in row]
                for row in image], (51, 51))

bin2dec = 2**np.arange(9).reshape(3, 3)

for i in range(50):
    image = enhance[convolve(image, bin2dec)]
    if i + 1 in (2, 50): print(image.sum())
"""