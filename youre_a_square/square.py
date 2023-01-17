'''
Task

Given an integral number, determine if it's a square number:

In mathematics, a square number or perfect square is an integer that is the 
square of an integer; in other words, it is the product of some integer with 
itself.

Examples

-1  =>  false
 0  =>  true
 3  =>  false
 4  =>  true
25  =>  true
26  =>  false
'''


import math


def is_square(n):
    # sqrt = math.sqrt(n)
    if type(math.sqrt(n)) == int:
        return True
    else:
        return False  # fix me


# function driver

print(is_square(-1))
