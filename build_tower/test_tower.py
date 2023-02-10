# PyTest script for tower.py

from tower import tower_builder


def test_1():
    assert (tower_builder(1) == ["*", ])


def test_2():
    assert (tower_builder(2) == [" * ", "***"])


def test_3():
    assert (tower_builder(3) == ['  *  ', ' *** ', '*****'])
