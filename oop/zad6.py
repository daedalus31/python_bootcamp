from functools import total_ordering
from math import sqrt


@total_ordering
class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return sqrt(self.x ** 2 + self.y ** 2) < sqrt(other.x ** 2 + other.y ** 2)

    def __str__(self):
        return f'[{self.x}; {self.y}]'


def test_vec_addition():
    v1 = Vector(x=1, y=2)
    v2 = Vector(x=3, y=4)

    v3 = v1 + v2

    assert v3.x == 4
    assert v3.y == 6


def test_vec_subtraction():
    v1 = Vector(x=3, y=4)
    v2 = Vector(x=1, y=2)

    v3 = v1 - v2

    assert v3.x == 2
    assert v3.y == 2


def test_vec_multiply_by_number():
    v1 = Vector(x=3, y=10)

    v2 = v1 * 10

    assert v2.x == 30
    assert v2.y == 100


def test_vector_comparison():
    v1 = Vector(2, 3)
    v2 = Vector(2, 5)
    v3 = Vector(4, 8)
    v4 = v1 + v2

    assert v1 < v2
    assert v2 > v1
    assert v4 == v3


def test_printing_vector():
    v = Vector(4, 6)
    assert str(v) == '[4; 6]'
