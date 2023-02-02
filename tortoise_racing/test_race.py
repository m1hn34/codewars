from race import race


def test_1():
    assert (race(720, 850, 70) == [0, 32, 18])


def test_2():
    assert (race(80, 91, 37) == [3, 21, 49])


def test_3():
    assert (race(820, 81, 550) == None)
