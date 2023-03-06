# PyTest script for supermarket.py

from supermarket import queue_time_2 as queue_time


def test_1():
    a = []
    b = 1
    c = 0
    assert (queue_time(a, b) == c)


def test_2():
    a = [5]
    b = 1
    c = 5
    assert (queue_time(a, b) == c)


def test_3():
    a = [2]
    b = 5
    c = 2
    assert (queue_time(a, b) == c)


def test_4():
    a = [1, 2, 3, 4, 5]
    b = 1
    c = 15
    assert (queue_time(a, b) == c)


def test_5():
    a = [1, 2, 3, 4, 5]
    b = 100
    c = 5
    assert (queue_time(a, b) == c)


def test_6():
    a = [2, 2, 3, 3, 4, 4]
    b = 2
    c = 9
    assert (queue_time(a, b) == c)


def test_7():
    a = [5, 3, 4]
    b = 1
    c = 12
    assert (queue_time(a, b) == c)


def test_8():
    a = [10, 2, 3, 3]
    b = 2
    c = 10
    assert (queue_time(a, b) == c)


def test_9():
    a = [2, 3, 10]
    b = 2
    c = 12
    assert (queue_time(a, b) == c)
