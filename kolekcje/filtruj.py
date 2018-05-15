def filtruj(dane, sprawdzenie):
    return [el for el in dane if sprawdzenie(el)]


def test_filtruj():
    assert filtruj([3, 2, 4, 1, 5], lambda x: x >= 3) == [3, 4, 5]
