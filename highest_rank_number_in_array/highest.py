'''
    Highest Rank Number in an Array

Complete the method which returns the number which is most frequent in the 
given input array. If there is a tie for most frequent number, return the 
largest number among them.

Note: no empty arrays will be given.

Examples:

[11, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
[11, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
[11, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3

'''

# Method 1
def highest_rank_1(arr):
    d = {}
    for n in arr:
        if n not in d:
            d[n] = 1
        else:
            d[n] += 1

    max_count = max(d.values())
    max_rank = []
    for n, count in d.items():
        if count == max_count:
            max_rank.append(n)

    return max(max_rank)

print("Method 1 -> " + str(highest_rank_1([1, 1, 2, 2, 3])))
print("Expected -> " + str(2))
print()



# Method 2
def highest_rank_2(arr):
    d = {}
    for n in arr:
        if n in d:
            d[n] += 1
        else:
            d[n] = 1

    max_d = max(d.values())
    max_n = [n for n, count in d.items() if count == max_d]

    return max(max_n)

print("Method 2 -> " + str(highest_rank_2([1, 1, 2, 2, 3])))
print("Expected -> " + str(2))
print()


# Method 3
def highest_rank_3(arr):
    return max(sorted(arr, reverse=True), key=arr.count)

print("Method 3 -> " + str(highest_rank_3([1, 1, 2, 2, 3])))
print("Expected -> " + str(2))
print()

