'''
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.


Examples:

[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
'''


# def find_it(seq):
#     res = set([i for i in seq if seq.count(i) % 2 > 0])
#     res = int(str(res).strip('{}'))
#     return res

def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i


seq = [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]
print(find_it(seq))
