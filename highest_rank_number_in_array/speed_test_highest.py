# Timeit test script for highest.py

import timeit

import_module = "import random"

test_code_1 = '''
def highest_rank_1(arr):
    d = {}
    for n in arr:
        if n not in d:
            d[n] = 1
        else:
            d[n] += 1

    max_count = max(d.values())
    max_rank = []
    for n, count in d.items():
        if count == max_count:
            max_rank.append(n)

    return max(max_rank)
'''

test_code_2 = '''
def highest_rank_2(arr):
    d = {}
    for n in arr:
        if n in d:
            d[n] += 1
        else:
            d[n] = 1

    max_d = max(d.values())
    max_n = [n for n, count in d.items() if count == max_d]

    return max(max_n)
'''

test_code_3 = '''
def highest_rank_3(arr):
    return max(sorted(arr, reverse=True), key=arr.count)
'''

print("Method 1")
print(timeit.repeat(stmt=test_code_1, setup=import_module))

print("Method 2")
print(timeit.repeat(stmt=test_code_2, setup=import_module))

print("Method 3")
print(timeit.repeat(stmt=test_code_3, setup=import_module))

