import timeit

import_module = "import random"

test_code_1 = '''
def expanded_form(num):
    expand = []
    for i, d in enumerate(str(num)[::-1]):
        if int(d) != 0:
            expand.append(d + "0" * i)
    return " + ".join(expand[::-1])
'''

test_code_2 = '''
def expanded_form(n):
    result = []
    for a in range(len(str(n)) - 1, -1, -1):
        current = 10 ** a
        quo, n = divmod(n, current)
        if quo:
            result.append(str(quo * current))
    return ' + '.join(result)
'''

test_code_3 = '''
def expanded_form(num):
    exp = []
    zeri = len(str(num))
    for cifra in str(num):
        zeri -= 1
        if cifra != '0':
            exp.append(cifra + '0'*zeri)
    return ' + '.join(exp)
'''

test_code_4 = '''
from math import floor,log
def expanded_form(num):
    x = 10**floor(log(num)/log(10))
    a = num//x
    b = num%x
    s = str(a*x)
    if (b!=0): s += " + " + expanded_form(b)
    return(s)
'''

print("Method 1")
print(timeit.repeat(stmt=test_code_1, setup=import_module))

print("Method 2")
print(timeit.repeat(stmt=test_code_2, setup=import_module))

print("Method 3")
print(timeit.repeat(stmt=test_code_3, setup=import_module))

print("Method 4")
print(timeit.repeat(stmt=test_code_4, setup=import_module))
