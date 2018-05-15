from collections import Counter


def znakow_ponad(napis, ile_wystapien):
    wynik = set()
    licznik = Counter(napis)
    for z in napis:
        if licznik[z] >= ile_wystapien:
            wynik.add(z)
    return wynik


def test_znakow_ponad_pusty():
    assert znakow_ponad('', 2) == set()


def test_znakow_ponad_ala():
    assert znakow_ponad('ala ma kota a kot ma ale', 3) == {'a', ' '}


def test_ponad_alfabet():
    assert znakow_ponad('abcdefghijklmnopqrstuwxyz', 2) == set()


def test_znakow_ponad_za_wysoki_prog():
    assert znakow_ponad('ala ma kota a kot ma ale', 50) == set()
