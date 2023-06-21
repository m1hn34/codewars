import timeit

import_module = "import random"

test_code_1 = '''
smileys = [
    ":)", ":D", ";)", ";D",
    ":-)", ":-D", ":~)", ":~D",
    ";-)", ";-D", ";~)", ";~D",
]


def count_smileys(arr):
    count = 0
    if len(arr) == 0:
        return 0
    else:
        for i in arr:
            if i in smileys:
                count += 1
        return count
'''


test_code_2 = '''
from re import findall

def count_smileys_2(arr):
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))
'''

print("test_code_1:")
print(timeit.repeat(stmt=test_code_1, setup=import_module))

print("test_code_2")
print(timeit.repeat(stmt=test_code_2, setup=import_module))
