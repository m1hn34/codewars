"""
You will be given a number(int) and you will need to return it as a string in
Expanded Form.


For example:
expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'

NOTE: all numbers will be whole numbers greater than 0.
"""


def expanded_form(num):
    expand = []
    for i, d in enumerate(str(num)[::-1]):
        if int(d) != 0:
            expand.append(d + "0" * i)
    return " + ".join(expand[::-1])


print(expanded_form(9999999999))
# print("70000 + 300 + 4")
