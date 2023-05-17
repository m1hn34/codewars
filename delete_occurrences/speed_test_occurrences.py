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

print("1st Method")
print(timeit.repeat(stmt=test_code_1, setup=import_module))
