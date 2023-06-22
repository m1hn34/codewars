import timeit

import_module = "import random"

test_case_1 = """
import re


def solution(s):
    splitted = re.sub('([A-Z][a-z]+)', r' \1',
                      re.sub('([A-Z]+)', r' \1', s)).split()
    result = ''
    for word in splitted:
        result += word
        result += ' '
    return result.strip()

"""


test_case_2 = """
def solution2(s):
    result = ''
    for c in s:
        if c.isupper():
            return result.join(' ' + c)
        else:
            return c
"""


test_case_3 = """
def solution3(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)
"""


print("1st Method:")
print(timeit.repeat(stmt=test_case_1, setup=import_module))

print("2nd Method:")
print(timeit.repeat(stmt=test_case_2, setup=import_module))

print("3rd Method")
print(timeit.repeat(stmt=test_case_3, setup=import_module))
