# Speed test for perfect_square.py

import timeit

import_module = "import random"

test_code_1 = '''
import math

def is_square(n):
    if n < 0:
        return False
    if n == 0:
        return True
    root = int(math.sqrt(n))

    return root ** 2 == n
'''

test_code_2 = '''
def is_square(n):
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
'''

test_code_3 = '''
def is_square(n):
    return n >= 0 and (n**0.5) % 1 == 0
'''

print("1st Method")
print(timeit.repeat(stmt=test_code_1, setup=import_module))

print("2nd Method")
print(timeit.repeat(stmt=test_code_2, setup=import_module))

print("3rd Method")
print(timeit.repeat(stmt=test_code_3, setup=import_module))

