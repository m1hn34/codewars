# Complete the solution so that the function will break up camel casing, using
# a space between words.

# Example

# solution("camelCasing") == "camel Casing"


# My solution - detailed - using re

import re


def solution(s):
    splitted = re.sub('([A-Z][a-z]+)', r' \1',
                      re.sub('([A-Z]+)', r' \1', s)).split()
    result = ''
    for word in splitted:
        result += word
        result += ' '
    return result.strip()


# My solution - without re

def solution2(s):
    result = ''
    for c in s:
        if c.isupper():
            return result.join(' ' + c)
        else:
            return c

# Short solution - simpler

def solution3(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)


# Function driver

print(solution2('camelCase'))
