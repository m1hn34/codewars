'''
Welcome.

In this kata you are required to, given a string, replace every letter with its
position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12
15 3 11" ( as a string )
'''


from string import ascii_lowercase


# 1st Method
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


# Debug
print(alphabet_position("The sunset sets at twelve o' clock."))
print("20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
