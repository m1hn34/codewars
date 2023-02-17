# SpeedTest script for encrypt.py

import timeit

import_module = "import random"

test_code_1 = '''

'''


print("1st Method")
print(timeit.repeat(stmt=test_code_1, setup=import_module))
