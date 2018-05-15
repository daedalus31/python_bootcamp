import math


def is_prime(num):
    if num <= 1:
        return False
    for d in range(2, int(math.floor(math.sqrt(num)))):
        if num % d == 0:
            return False
    return True


def test_is_prime():
    assert not is_prime(1)
    assert is_prime(2)

    assert is_prime(17)
    assert not is_prime(45)
