import timeit

import_module = "import random"

test_code_1 = '''
def tower_builder_1(n_floors):
    tower = []
    for i in range(n_floors):
        tower.append(' '*(n_floors-i-1) + '*'*(2*i+1) + ' '*(n_floors-i-1))
    return tower
'''

test_code_2 = '''
def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]
'''

print("long-but-slow")
print(timeit.repeat(stmt=test_code_1, setup=import_module))

print("shor-but-fast")
print(timeit.repeat(stmt=test_code_2, setup=import_module))
