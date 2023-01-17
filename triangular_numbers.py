'''
Triangular number is the amount of points that can fill equilateral triangle.

Example: the number 6 is a triangular number because all sides of a triangle
has the same amount of points.

alt text

Hint!
T(n) = n * (n + 1) / 2,
n - is the size of one side.
T(n) - is the triangular number.

Given a number 'T' from interval [1; 2147483646], find if it is triangular
number or not.
'''


def is_triangular(t):
    if t % 3 == 0:
        n = t / 3
        Tn = n * (n + 1) / 2
        return int(Tn)
    else:
        return False

print(is_triangular(1))
print(is_triangular(3))
print(is_triangular(6))
print(is_triangular(7))
