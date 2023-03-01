# SpeedTest script for encrypt.py

import timeit

import_module = "import random"

test_code_1 = '''
def encrypt_this(text):
    text = text.split(' ')
    encrypted = []
    for word in text:
        if len(word) < 3:
            encrypted.append(
                str(ord(word[0])) + word[1])
            encrypted.append(" ")
        else:
            encrypted.append(
                str(ord(word[0])) + word[-1] + word[2:-1:] + word[1]
            )
            encrypted.append(" ")
    text = "".join(encrypted)
    return text.strip()
'''


print("1st Method")
print(timeit.repeat(stmt=test_code_1, setup=import_module))
