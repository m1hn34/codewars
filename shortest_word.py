#pyhton3.7
'''
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data
types.
'''

# my solution

def find_short(s):
    wordList = s.split()
    l = len(min(wordList, key=lambda word: len(word)))
    return l  # l: shortest word length

# Shortest brilliant solution:


def find_short(s):
    return min(len(x) for x in s.split())


s = "bitcoin take over the world maybe who knows perhaps"
print(find_short(s))

s = "turns out random test cases are easier than writing out basic ones"
print(find_short(s))

s = "lets talk about javascript the best language"
print(find_short(s))

s = "i want to travel the world writing code one day"
print(find_short(s))

s = "Lets all go on holiday somewhere very cold"
print(find_short(s))
