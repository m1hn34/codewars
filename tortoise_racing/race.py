'''
Two tortoises named A and B must run a race. A starts with an average speed of 
720 feet per hour. Young B knows she runs faster than A, and furthermore has 
not finished her cabbage.

When she starts, at last, she can see that A has a 70 feet lead but B's speed 
is 850 feet per hour. How long will it take B to catch A?

More generally: given two speeds 
v1 (A's speed, integer > 0) and 
v2 (B's speed, integer > 0) and a lead
g (integer > 0)
how long will it take B to catch A?

The result will be an array [hour, min, sec] which is the time needed in hours,
minutes and seconds (round down to the nearest second) or a string in some 
languages.

If v1 >= v2 then return nil, nothing, null, None or {-1, -1, -1} for C++, C, 
Go, Nim, Pascal, COBOL, Erlang, [-1, -1, -1] for Perl,[]
for Kotlin or "-1 -1 -1".

Examples:
(form of the result depends on the language)

race(720, 850, 70) => [0, 32, 18] or "0 32 18"
race(80, 91, 37)   => [3, 21, 49] or "3 21 49"
'''
import datetime
import math


# Method 1 with datetime.timedelta


def race(v1, v2, g):
    intercept_time = ''
    if v1 >= v2:
        return None
    else:
        intercept_time = datetime.timedelta(hours=(g/(v2-v1)))
        intercept_time = str(intercept_time).split(":")
        intercept_time = list(map(float, intercept_time))
        result = [round(elem) for elem in intercept_time]
        return result

# Method 2 without math.floor


def race_2(v1, v2, g):
    # your code
    if v1 > v2:
        return None
    speedDiff = v2-v1
    totalSec = g/(speedDiff/3600)
    s = math.floor(totalSec % 60)
    m = math.floor((totalSec % 3600)/60)
    h = math.floor(totalSec/3600)

    return [h, m, s]

# Method without modules


def race_3(v1, v2, g):
    if v2 <= v1:
        return None
    total = g / (v2 - v1)
    return [int(total), int(total * 60) % 60, int(total * 3600) % 60]


# debug
print(race(720, 850, 70))
