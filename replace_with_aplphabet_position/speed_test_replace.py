import timeit
from string import ascii_lowercase


import_module = "import random"

test_code_1 = '''
def alphabet_position(text):
    _alpha = {}
    for index, letter in enumerate(ascii_lowercase, start=1):
        _alpha.update({letter: str(index)})
    text = text.lower()
    _num = []
    for character in text:
        if character in _alpha:
            _num.append(_alpha[character])
    return " ".join(_num)

'''

print("test_code_1")
print(timeit.repeat(stmt=test_code_1, setup=import_module))
