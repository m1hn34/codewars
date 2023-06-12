# Speed Test for reverse_order.py

import timeit

import_module = 'import random'

test_code_1 = '''
def reverse(st):
    words = st.split(' ')
    words.reverse()
    result = ' '.join(words)
    return result.strip()
'''

test_code_2 = '''
def reverse(st):
    reversed_string = ' '.join(st.split(' ')[::-1])
    return reversed_string.strip()
'''

print('test_code_1:')
print(timeit.repeat(stmt=test_code_1, setup=import_module))
print('test_code_2:')
print(timeit.repeat(stmt=test_code_2, setup=import_module))
