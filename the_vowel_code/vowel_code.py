'''
Step 1: Create a function called encode() to replace all the lowercase vowels 
in a given string with numbers according to the following pattern:

a -> 1
e -> 2
i -> 3
o -> 4
u -> 5
For example, encode("hello") would return "h2ll4". There is no need to worry 
about uppercase vowels in this kata.

Step 2: Now create a function called decode() to turn the numbers back into 
vowels according to the same pattern shown above.

For example, decode("h3 th2r2") would return "hi there".

For the sake of simplicity, you can assume that any numbers passed into the 
function will correspond to vowels.
'''

# 1st Method
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


# 2nd Method
def encode_1(s, t=str.maketrans("aeiou", "12345")):
    return s.translate(t)


def decode_2(s, t=str.maketrans("12345", "aeiou")):
    return s.translate(t)


# driver
print(encode_1("How are you today?"))
print("H4w 1r2 y45 t4d1y?")
print("")
print(decode_2("H4w 1r2 y45 t4d1y?"))
print("How are you today?")
