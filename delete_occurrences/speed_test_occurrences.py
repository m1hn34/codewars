# SpeedTest script for occurrences.py

import timeit

import_module = "import random"

test_code_1 = '''
def delete_nth(order, max_e):
    occurrences = {}
    result = []

    for elem in order:
        if elem in occurrences:
            if occurrences[elem] < max_e:
                occurrences[elem] += 1
                result.append(elem)
        else:
            occurrences[elem] = 1
            result.append(elem)
    
        return result
'''

test_code_2 = '''
def delete_nth(order, max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e:
            ans.append(o)
    return ans
'''

test_code_3 = '''
from collections import Counter

def delete_nth(order, max_e):
    c = Counter()
    result = []
    for element in order:
        if c[element] < max_e:
            c[element] += 1
            result.append(element)
    return result
'''

print("1st Method")
print(timeit.repeat(stmt=test_code_1, setup=import_module))

print("2nd Method")
print(timeit.repeat(stmt=test_code_2, setup=import_module))

print("3rd Method")
print(timeit.repeat(stmt=test_code_3, setup=import_module))
