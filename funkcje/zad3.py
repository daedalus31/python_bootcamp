def policz_znaki(napis: str, otwarcie: str = '<', zamkniecie: str = '>') -> int:
    waga_znaku = 0
    wynik = 0
    for zn in napis:
        if zn == otwarcie:
            waga_znaku += 1
        elif zn == zamkniecie:
            waga_znaku -= 1
        else:
            wynik += waga_znaku
    return wynik


def test_policz_znaki_domyslny():
    assert policz_znaki('ala ma <ale> a kot ma ale') == 3


def test_policz_znaki_niedomyslny():
    assert policz_znaki('ala ma [ale] a kot ma ale', '[', ']') == 3


def test_policz_znaki_zaglebione():
    assert policz_znaki('ala ma [kota [a kot]] ma [ale]', '[', ']') == 18
    assert policz_znaki('a <a<a<a>>>') == 6
