# SpeedTest script for supermarket.py

import timeit

import_module = "import random"

test_code_1 = '''
def queue_time(customers, n):
    tills = [0] * n
    for i in customers:
        tills[0] += i
        tills.sort()
    return max(tills)
'''

test_code_2 = '''
def queue_time_2(customers, n):
    heap = [0] * n
    for time in customers:
        heapq.heapreplace(heap, heap[0] + time)
    return max(heap)
'''

print("1st Method")
print(timeit.repeat(stmt=test_code_1, setup=import_module))

print("2nd Method")
print(timeit.repeat(stmt=test_code_2, setup=import_module))
