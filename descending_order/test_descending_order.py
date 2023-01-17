from descending_order import descending_order




def test_0():
    assert(descending_order(0) == 0)

def test_1():
    assert(descending_order(15) == 51)

def test_2():
    assert(descending_order(123456789) == 987654321)

def test_3():
    assert(descending_order(2034) == 4320)

def test_4():
    assert(descending_order(10) == 10)

def test_5():
    assert(descending_order(666) == 666)
