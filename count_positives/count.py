'''
Given an array of integers.

Return an array, where the first element is the count of positives numbers and 
the second element is sum of negative numbers.

If the input array is empty or null, return an empty array.

Example

For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should 
return [10, -65].
'''


def count_positives_sum_negatives(arr):
    positive = 0
    negative = 0
    result = []
    if not arr:
        return result
    else:
        for i in arr:
            if i < 0:
                negative += i
            elif i > 0:
                positive += 1
        result = [positive, negative]
    return result


# Function driver
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
y = []
print(count_positives_sum_negatives(y))
