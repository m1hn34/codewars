# Speed test for the_same.py
import timeit

import_module = "import random"

test_code_1 = '''
def comp_1(arr1, arr2):
    if (arr1 and arr2) or (arr1 == arr2):
        arr1.sort()
        arr2.sort()
        b = []
        for i in arr1:
            if i < 0:
                i = i * -1
            b.append(i*i)
        b.sort()
        return b == arr2
    else:
        return False

'''

test_code_2 = '''
def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False

'''

print("1st Method")
print(timeit.repeat(stmt=test_code_1, setup=import_module))

print("2nd Method")
print(timeit.repeat(stmt=test_code_2, setup=import_module))
