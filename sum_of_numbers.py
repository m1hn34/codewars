# Given two integers a and b, which can be positive or negative, find the sum 
# of all the numbers between including them too and return it. If the two 
# numbers are equal return a or b.

# Note: a and b are not ordered!

# Examples

# get_sum(1, 0) == 1 // 1 + 0 = 1
# get_sum(1, 2) == 3 // 1 + 2 = 3
# get_sum(0, 1) == 1 // 0 + 1 = 1
# get_sum(1, 1) == 1 // 1 Since both are same
# get_sum(-1, 0) == -1 // -1 + 0 = -1
# get_sum(-1, 2) == 2 // -1 + 0 + 1 + 2 = 2

def get_sum(a, b):
    s = []
    if a < b:
        for i in range(a, b+1):
            s.append(i)
        return sum(s)
    if a > b:
        for i in range(b, a+1):
            s.append(i)
        return sum(s)
    else:
        return a

print(get_sum(1, 0))
print("should be 1\n")

print(get_sum(0, -1))
print("should be -1\n")

print(get_sum(1, 2))
print("should be 3\n")

print(get_sum(0 ,1))
print("should be 1\n")

print(get_sum(1, 1))
print("should be 1\n")

print(get_sum(-1, 0))
print("should be -1\n")

print(get_sum(-1, 2))
print("should be 2\n")
