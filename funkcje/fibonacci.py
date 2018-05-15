def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


def test_fib_0():
    assert fib(0) == 0


def test_fib_1():
    assert fib(1) == 1


def test_fib_6():
    assert fib(6) == 8
