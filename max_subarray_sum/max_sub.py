'''
The maximum sum subarray problem consists in finding the maximum sum of a 
contiguous subsequence in an array or list of integers:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]

Easy case is when the list is made up of only positive numbers and the maximum 
sum is the sum of the whole array. If the list is made up of only negative 
numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or
array is also a valid sublist/subarray.
'''


# def max_sequence(items):
#     iter_items = iter(items)
#     try:
#         temp_sum = next(iter_items)
#     except StopIteration:
#         temp_sum = 0
#     max_sum = temp_sum
#     for item in iter_items:
#         temp_sum = max(temp_sum + item, item)
#         max_sum = max(temp_sum, max_sum)
#     return max(max_sum, 0)


# def max_sequence(arr):
#     curr_max_sum = float('-inf')
#     global_max = float('-inf')
#     if not arr:
#         return 0
#     elif max(arr) <= 0:
#         return 0
#     else:
#         for i in arr:
#             curr_max_sum = max(curr_max_sum + i, i)
#             global_max = max(curr_max_sum, global_max)
#         return global_max


def max_sequence(arr):
    temp_sum = 0
    max_sum = 0
    if not arr or max(arr) <= 0:
        return 0
    else:
        for i in arr:
            temp_sum = max(temp_sum + i, i)
            max_sum = max(temp_sum, max_sum)
        return max_sum


# function driver
print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print('should be 6')
print(max_sequence([]))
print('should be 0')
print(max_sequence([-1, -2, -3, -4]))
print('should aslo be 0')
