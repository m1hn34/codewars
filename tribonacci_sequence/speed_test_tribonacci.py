import timeit

import_module = "import random"

test_code = '''
def tribonacci(signature, n):
    #trib = []
    if n == 0 or len(signature) < 3:
        return []
    elif n < len(signature):
        return signature[0:n]
    else:
        while len(signature) < n:
            signature.append(sum(signature[-3:]))
        return signature
'''

test_code_2 = '''
def tribonacci_2(signature, n):
    res = signature[:n]
    for i in range(n - 3):
        res.append(sum(res[-3:]))
    return res
'''

print("long-but-fast")
print(timeit.repeat(stmt=test_code, setup=import_module))

print("short-but-slow")
print(timeit.timeit(stmt=test_code_2, setup=import_module))
