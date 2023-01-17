# Python 3.9

'''
Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and 
A..Z.
'''


def accum(s):
    l = list((s))
    r = ''
    for i, j in enumerate(s):  # enumerate() will generate a tuple '(0, a)'
        r += j.upper() + j.lower() * i + '-'
    return r.strip('-')


# one-liner (same speed)
# def accum(s):
#     return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))


# driver
print(accum('ZpglnRxqenU'))
print('Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu')
