'''
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: 
a = 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the 
original string.

All letters will be lowercase and all inputs will be valid.
'''


# 1st Method - long & slow
def word_value(input_word):
    values = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26
    }
    value = 0
    for letter in input_word:
        value += values[letter]
    return value


def high_1(x):
    word_list = x.split(" ")

    word_values = []
    for word in word_list:
        word_values.append(word_value(word))

    max_value = max(word_values)
    index_of_max = word_values.index(max_value)

    return word_list[index_of_max]


# 2nd Method - short & fast
def high(x):
    highest_score = 0
    for word in x.split(' '):
        score = sum(ord(c)-96 for c in word)
        if score > highest_score:
            highest_score = score
            highest_word = word
    return highest_word


# debug
a = 'what time are we climbing up the volcano'
b = 'volcano'
print(high(a) == b)
print(True)
