'''
An isogram is a word that has no repeating letters, consecutive or 
on-consecutive. Implement a function that determines whether a string that 
contains only letters is an isogram. Assume the empty string is an isogram. 
Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter case)
'''


# def is_isogram(string):
#     a = string.lower()
#     b = ''
#     for i in a:
#         if i not in b:
#             b += i
#     return False if b != a else True


# Refactored form

def is_isogram(string):
    return len(string) == len(set(string.lower()))
