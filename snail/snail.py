# Snail Sort

# Given an n x n array, return the array elements arranged from outermost 
# elements to the middle element, traveling clockwise.

# array = [[1, 2, 3],
#          [4, 5, 6],
#          [7, 8, 9]]
# snail(array)  # => [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array 
# consecutively:

# array = [[1, 2, 3],
#          [8, 9, 4],
#          [7, 6, 5]]
# snail(array)  # => [1,2,3,4,5,6,7,8,9]


# NOTE: The idea is not sort the elements from the lowest value to the highest
# the idea is to traverse the 2-d array in a clockwise snailshell pattern.

# NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an 
# array[[]].


# My solution

def snail(snail_map):
    result = []
    if snail_map == [[]]:
        result = 'empty'
    else:
        result = result + snail_map[0]
        result = result + (x[-1] for x in snail_map[2])
    return result


# Function driver

snail_map = [[]]

array = [[1, 2, 3],
         [8, 9, 4],
         [7, 6, 5]]

# print(snail(array))
print(len(array))
