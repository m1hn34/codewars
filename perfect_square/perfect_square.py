'''
Given an integral number, determine if it's a "square number"

    "In mathematics, a "square number" or "perfect square" is an integer that
    is the square of an integer; in other words, it is the product of some
    integer with itself.

Examples:
    -1 => False     # Negative numbers are not perfect squares
    0 => True       # Zero is a pefrect square
    3 => False      # 3 is not a perfect square
    4 => True       # 4 is a perfect square 2 * 2
    25 => True      # 25 is a perfect square 5 * 5
    26 => False     # 26 is not a perfect square
'''

# 1st method using standard library

import math

def is_square_1(n):
    if n < 0:
        return False
    if n == 0:
        return True
    root = int(math.sqrt(n))

    return root ** 2 == n


# 2nd method using binary search algorithm (FASTEST)

def is_square_2(n):
    if n < 0:
        return False
    if n == 0:
        return True

    start = 1
    end = n
    while start <= end:
        mid = (start + end) // 2
        square = mid * mid

        if square == n:
            return True
        elif square < n:
            start = mid + 1
        else:
            end = mid - 1

    return False

# 3rd method // shorter

def is_square(n):
    return n >= 0 and (n**0.5) % 1 == 0


# Debugging


print()
print(is_square(25))
print()

