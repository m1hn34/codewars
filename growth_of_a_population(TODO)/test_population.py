from population import nb_year


def test_0():
    assert(nb_year(1500, 5, 100, 5000) == 15)


def test_1():
    assert(nb_year(1500000, 2.5, 10000, 2000000) == 10)


def test_2():
    assert(nb_year(1500000, 0.25, 1000, 2000000) == 94)
