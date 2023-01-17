#python3.7

'''
Write a function that accepts an array of 10 integers (between 0 and 9), that
returns a string of those numbers in the form of a phone number.

Example:
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
# => returns "(123) 456-7890"

The returned format must be correct in order to complete this challenge. 
Don't forget the space after the closing parentheses!
'''
# My method

def create_phone_number(n):
    phString = ""
    for i in n:
        phString += str(i)
    phNumber = "(" + phString[0:3] + ") " + phString[3:6] + "-" + phString[6:10]
    return phNumber

# Best method
#
# def create_phone_number(n):
#     return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) + "\n(123) 456-7890\n")
# print(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) + "\n(111) 111-1111\n")
# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) + "\n(123) 456-7890\n")
# print(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]) + "\n(023) 056-0890\n")
# print(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) + "\n(000) 000-0000\n")
