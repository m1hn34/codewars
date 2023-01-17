from is_prime import is_prime

def test_basic():
    assert(is_prime(0) == False)
    assert(is_prime(1) == False)
    assert(is_prime(2) == True)
    assert(is_prime(73) == True)
    assert(is_prime(75) == False)
    assert(is_prime(-1) == False)

def test_primes():
    assert(is_prime(3) == True)
    assert(is_prime(5) == True)
    assert(is_prime(7) == True)
    assert(is_prime(41) == True)
    assert(is_prime(5099) == True)

def test_not_primes():
    assert(is_prime(4) == False)
    assert(is_prime(6) == False)
    assert(is_prime(8) == False)
    assert(is_prime(9) == False)
    assert(is_prime(45) == False)
    assert(is_prime(-5) == False)
    assert(is_prime(-8) == False)
    assert(is_prime(-41) == False)




