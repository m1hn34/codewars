# PyTest script for highest.py

from highest import highest_rank_1
 

def test_0():
    arr = [12, 10, 8, 12, 7, 6, 4, 10, 12]
    output = 12
    assert(highest_rank_1(arr) == output)

def test_1():
    arr = [12, 10, 8, 12, 7, 6, 4, 10, 10]
    output = 10
    assert(highest_rank_1(arr) == output)

def test_2():
    arr = [12, 10, 8, 12, 7, 6, 4, 10, 12, 10]
    output = 12
    assert(highest_rank_1(arr) == output)

def test_3():
    arr = [12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]
    output = 3
    assert(highest_rank_1(arr) == output)

def test_4():
    arr = [1, 2, 3]
    output = 3
    assert(highest_rank_1(arr) == output)

def test_5():
    arr = [1, 1, 2, 3]
    output = 1
    assert(highest_rank_1(arr) == output)

def test_6():
    arr = [1, 1, 2, 2, 3]
    output = 2
    assert(highest_rank_1(arr) == output)

