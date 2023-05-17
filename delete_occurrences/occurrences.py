'''
Given a list and a number, create a new list that contains each number of list
at most N times, without reordering.
For example if the input number is 2, and the input list is [1,2,3,1,2,1,2,3],
you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2
being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].
With list [20,37,20,21] and number 1, the result would be [20,37,21].
'''


# 1st method - fastest
from collections import Counter


def delete_nth_1(order, max_e):
    occurrences = {}
    result = []

    for elem in order:
        if elem in occurrences:
            if occurrences[elem] < max_e:
                occurrences[elem] += 1
                result.append(elem)
        else:
            occurrences[elem] = 1
            result.append(elem)

    # order[:] = result
    return result


# 2nd method
def delete_nth_2(order, max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e:
            ans.append(o)
    return ans


# 3rd method - slowest
def delete_nth(order, max_e):
    c = Counter()
    result = []
    for element in order:
        if c[element] < max_e:
            c[element] += 1
            result.append(element)
    return result
