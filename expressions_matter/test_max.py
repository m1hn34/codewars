# PyTest script for max.py

from max import expression_matter


def test_1():
    assert (expression_matter(2, 1, 2) == 6)


def test_2():
    assert (expression_matter(2, 1, 1) == 4)


def test_3():
    assert (expression_matter(2, 2, 4) == 16)


def test_4():
    assert (expression_matter(3, 3, 3) == 27)


def test_5():
    assert (expression_matter(1, 1, 1) == 3)


def test_6():
    assert (expression_matter(1, 2, 3) == 9)


def test_7():
    assert (expression_matter(1, 3, 1) == 5)


def test_8():
    assert (expression_matter(2, 2, 2) == 8)


def test_9():
    assert (expression_matter(5, 1, 3) == 20)


def test_10():
    assert (expression_matter(3, 5, 7) == 105)


def test_11():
    assert (expression_matter(5, 6, 1) == 35)


def test_12():
    assert (expression_matter(1, 6, 1) == 8)


def test_13():
    assert (expression_matter(2, 6, 1) == 14)


def test_14():
    assert (expression_matter(6, 7, 1) == 48)


def test_15():
    assert (expression_matter(2, 10, 3) == 60)


def test_16():
    assert (expression_matter(1, 8, 3) == 27)


def test_17():
    assert (expression_matter(9, 7, 2) == 126)


def test_18():
    assert (expression_matter(1, 1, 10) == 20)


def test_19():
    assert (expression_matter(9, 1, 1) == 18)


def test_20():
    assert (expression_matter(10, 5, 6) == 300)


def test_21():
    assert (expression_matter(1, 10, 1) == 12)
