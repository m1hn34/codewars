def is_prime(num):
    if num < 2:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
            return True


randomList = random.sample(range(-2147483648, 2147483648, 100))


def test_random():
    for i in randomList:
        assert(is_prime(i))
