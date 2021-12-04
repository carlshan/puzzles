

def convert_binary(number):
    """
        Converts number into string for binary notation.
    """
    binary = ['0'] * 8
    binarize = number
    while binarize >= 1:
        exponent = largest_power_of_2(binarize)
        index = exponent
        binary[index] = '1'
        binarize = binarize - 2**exponent
    return binary[::-1]

def largest_power_of_2(number):
    """
        Returns the largest power of 2 that goes into this number
    """
    power = 0
    while number - 2**power > 0:
        power += 1
    if number - 2**power < 0:
        return power-1
    return power
