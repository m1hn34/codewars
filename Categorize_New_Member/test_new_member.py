# Pytest for new_member.py

from new_member import open_or_senior


def test_0():
    assert(open_or_senior(
        [(45, 12), (55, 21), (19, -2), (104, 20)]) == ['Open', 'Senior', 'Open', 'Senior'])
    assert(open_or_senior(
        [(16, 23), (73, 1), (56, 20), (1, -1)]) == ['Open', 'Open', 'Senior', 'Open'])
