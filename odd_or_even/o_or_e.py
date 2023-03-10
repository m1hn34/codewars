'''
Task:

Given a list of numbers, determine whether the sum of its 
elements is odd or even.

Give your answer as a string matching "odd" or "even".

If the input array is empty consider it as: [0] (array with a 
zero).

Example:

odd_or_even([0])          ==  "even"
odd_or_even([0, 1, 4])    ==  "odd"
odd_or_even([0, -1, -5])  ==  "even"
'''


def odd_or_even(arr):
    return "even" if sum(arr) % 2 == 0 else "odd"


# Debugging
print(odd_or_even([0, 1, 4]))
print("odd")
