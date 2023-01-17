'''
Your job is to write a function which increments a string, to create a new 
string.

If the string already ends with a number, the number should be incremented by 
1.
If the string does not end with a number. the number 1 should be appended to 
the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be 
considered.
'''
import string


def increment_string(strng):
    # string variable with all digits (0-9)
    digits = string.digits
    # string viarable that will contain the trailing digits from 'strng'
    temp_number = ""
    # string variable that will contain all other characters from 'strng'
    temp_name = ""
    result = ""
    if strng == "":
        return "1"
    elif strng[-1] not in digits:
        return strng + "1"
    else:
        for i in strng:
            if i in digits:
                temp_number += i
            else:
                temp_name += i
        # concatenate strng with temp incremented by 1
        result = temp_name + \
            format(int(temp_number) + 1, '0'+str(len(temp_number))+'d')
        return result


# debug
print(increment_string("foobar099"))
