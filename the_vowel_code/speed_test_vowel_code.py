import timeit

import_module = "import random"

test_code_1 = '''
codes = {
    "a": "1",
    "e": "2",
    "i": "3",
    "o": "4",
    "u": "5",
}


def encode(st):
    coded = ""
    for char in st:
        if char.lower() in codes:
            coded += codes[char]
        else:
            coded += char
    return coded


def decode(st):
    decoded = ""
    key_list = list(codes.keys())
    val_list = list(codes.values())
    for char in st:
        if char.lower() in codes.values():
            decoded += key_list[val_list.index(char)]
        else:
            decoded += char
    return decoded
'''

test_code_2 = '''
def encode_1(s, t=str.maketrans("aeiou", "12345")):
    return s.translate(t)


def decode_2(s, t=str.maketrans("12345", "aeiou")):
    return s.translate(t)
'''

print("1st Method:")
print(timeit.repeat(stmt=test_code_1, setup=import_module))
print("")
print("2nd Method:")
print(timeit.repeat(stmt=test_code_2, setup=import_module))
