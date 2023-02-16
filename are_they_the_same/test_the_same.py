# PyTest script for the_same.py


from the_same import comp


def test_1():
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    assert (comp(a1, a2) == True)


def test_2():
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    assert (comp(a1, a2) == False)


def test_3():
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
    assert (comp(a1, a2) == False)


def test_4():
    a1 = [1, 2, 3]
    a2 = [1, 9, 4]
    assert (comp(a1, a2) == True)


def test_5():
    a1 = [-161, -144, -144, -121, -11, 19, 19, 19]
    a2 = [121, 361, 361, 361, 14641, 20736, 20736, 25921]
    assert (comp(a1, a2) == True)


def test_6():
    a1 = []
    a2 = []
    assert (comp(a1, a2) == True)


def test_7():
    a1 = None
    a2 = []
    assert (comp(a1, a2) == False)
