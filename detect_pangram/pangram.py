'''
A pangram is a sentence that contains every single letter of the alphabet at 
least once. For example, the sentence "The quick brown fox jumps over the lazy 
dog" is a pangram, because it uses the letters A-Z at least once (case is 
irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, 
False if not. Ignore numbers and punctuation.
'''

# method 1
# def is_pangram(s):
#     alpha = "abcdefghijklmnopqrstuvwxyz"

#     for c in alpha:
#         if c not in s.lower():
#             return False
#         else:
#             return True


# method 2 that works (kinda)
import string

alpha = set(string.ascii_lowercase)


def is_pangram(s):
    return set(s.lower()) >= alpha


# driver
pangram = 'Aacdefghijklmnopqrstuvwxyz'
print(is_pangram(pangram))
