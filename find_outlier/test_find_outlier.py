# Python3
# Pytest script for find_outlier.py


from find_outlier import find_outlier


def test_0():
    assert(find_outlier([2, 4, 6, 8, 10, 3]) == 3)
    assert(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]) == 11)
    assert(find_outlier([160, 3, 1719, 19, 11, 13, -21]) == 160)
