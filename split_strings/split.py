'''
Complete the solution so that it splits the string into pairs of two 
characters. If the string contains an odd number of characters then it should 
replace the missing second character of the final pair with 
an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
'''


def solution(s):
    s = list(s)
    if len(s) % 2 != 0:
        s.insert(len(s), "_")
    res = [i + j for i, j in zip(s[::2], s[1::2])]
    return res


# Function driver
s = 'abcde'
print(solution(s))
