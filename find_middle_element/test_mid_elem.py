# PyTest script for mid_elem.py


from mid_elem import gimme


def test_1():
    assert (gimme([2, 3, 1]) == 0)


def test_2():
    assert (gimme([5, 10, 14]) == 1)
