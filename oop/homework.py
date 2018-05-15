import pytest


class BrakPaliwaError(Exception):
    pass


class ZlePaliwoError(Exception):
    pass


class StacjaPaliw:
    def __init__(self, nazwa_stacji, typy_paliw, adres_stacji):
        self._nazwa = nazwa_stacji
        self._adres = adres_stacji
        self._magazyn_paliw = {t: {'litrow': 0, 'cena': None} for t in typy_paliw}
        self._stali_klienci = {}

    def zatankuj(self, typ_paliwa, ile_litrow, numer_rejestracyjny=None):
        typ_paliwa = typ_paliwa.upper()
        try:
            if ile_litrow <= self._magazyn_paliw[typ_paliwa]['litrow']:
                self._rejestruj_zakup(numer_rejestracyjny, ile_litrow)
                wynik = self._policz_cene(numer_rejestracyjny, ile_litrow, typ_paliwa)
                self._magazyn_paliw[typ_paliwa]['litrow'] -= ile_litrow
            else:
                raise BrakPaliwaError()
        except KeyError:
            raise ZlePaliwoError()
        return wynik

    def uzupelnij(self, typ_paliwa, ile_litrow):
        typ_paliwa = typ_paliwa.upper()
        try:
            self._magazyn_paliw[typ_paliwa]['litrow'] += ile_litrow
        except KeyError:
            raise ZlePaliwoError()

    def ustal_cene(self, typ_paliwa, cena):
        typ_paliwa = typ_paliwa.upper()
        try:
            self._magazyn_paliw[typ_paliwa]['cena'] = cena
        except KeyError:
            raise ZlePaliwoError()

    def wypisz_paliwa(self):
        wynik = []
        for symbol_paliwa in self._magazyn_paliw:
            paliwo = self._magazyn_paliw[symbol_paliwa]
            if paliwo['cena'] is not None and paliwo['litrow'] > 0:
                wynik.append(f' - {symbol_paliwa}: {paliwo["cena"]:.2f} PLN')
            elif paliwo['cena'] is None and paliwo['litrow'] > 0:
                wynik.append(f' - {symbol_paliwa}: JEST, ALE CENA NIEUSTALONA')
            else:
                wynik.append(f' - {symbol_paliwa}: NIEDOSTĘPNE')
        return wynik

    def _rejestruj_zakup(self, numer_rejestracyjny, ile_litrow):
        if numer_rejestracyjny is not None:
            numer_rejestracyjny = numer_rejestracyjny.upper()
            if numer_rejestracyjny not in self._stali_klienci:
                self._stali_klienci[numer_rejestracyjny] = ile_litrow
            else:
                self._stali_klienci[numer_rejestracyjny] += ile_litrow

    def _policz_cene(self, numer_rejestracyjny, ile_litrow, typ_paliwa):
        cena_bazowa = self._magazyn_paliw[typ_paliwa]['cena'] * ile_litrow
        if numer_rejestracyjny in self._stali_klienci and self._stali_klienci[
            numer_rejestracyjny] > 1000:
            return cena_bazowa * 0.9
        return cena_bazowa

    def przedstaw_sie(self):
        return f'{self._nazwa}, adres: {self._adres}'


@pytest.fixture
def stacja():
    return StacjaPaliw('Testowa Stacja', ['PB95', 'PB98', 'LPG', 'ON'],
                       'ul. Testowa 1, Testowice')


def test_stacja_bez_paliwa(stacja):
    with pytest.raises(BrakPaliwaError):
        stacja.zatankuj('ON', 200)


def test_bez_paliwa_po_tankowaniu(stacja):
    stacja.uzupelnij('on', 500)
    stacja.ustal_cene('on', 4.50)

    stacja.zatankuj('on', 200)
    stacja.zatankuj('on', 200)
    with pytest.raises(BrakPaliwaError):
        stacja.zatankuj('ON', 200)


def test_zle_paliwo(stacja):
    with pytest.raises(ZlePaliwoError):
        stacja.uzupelnij('biodiesel', 450)


def test_dodania_paliwa(stacja):
    stacja.uzupelnij('LPG', 200)
    stacja.ustal_cene('LPG', 2.00)

    assert stacja.zatankuj('LPG', 120) == 240.00


def test_wypisywania_paliw(stacja):
    stacja.uzupelnij('ON', 400)
    stacja.ustal_cene('ON', 4.60)
    stacja.uzupelnij('PB95', 5000)
    stacja.ustal_cene('PB95', 4.80)
    stacja.uzupelnij('LPG', 4000)

    assert set(stacja.wypisz_paliwa()) == {' - PB95: 4.80 PLN', ' - PB98: NIEDOSTĘPNE',
                                           ' - LPG: JEST, ALE CENA NIEUSTALONA',
                                           ' - ON: 4.60 PLN'}


def test_rabatu(stacja):
    stacja.uzupelnij('on', 5000)
    stacja.ustal_cene('on', 5.00)

    assert stacja.zatankuj('on', 500, 'ABC2345D') == 2500.00
    assert stacja.zatankuj('on', 500, 'ABC2345D') == 2500.00
    assert stacja.zatankuj('on', 100, 'ABC2345D') == 450.00


class InterfejsStacjiPaliw:
    def __init__(self):
        self._stacja = StacjaPaliw('Testowa Stacja', ['PB95', 'PB98', 'LPG', 'ON'],
                                   'ul. Testowa 1, Testowice')

    def run(self):
        while True:
            print(f'Witamy na stacji {self._stacja.przedstaw_sie()}')
            akcja = input(
                'Co chcesz zrobić? [w - wypisz paliwa, t - tankuj paliwo, u - uzupełnij paliwo, c - ustal cenę paliwa, k - koniec] ')
            if akcja == 'w':
                self._wypisz_paliwa()
            elif akcja == 't':
                paliwo = input('Podaj typ paliwa: ')
                litry = int(input('Podal ilość paliwa: '))
                nr_rej = input('Podaj numer rejestracyjny (opcjonalnie): ')
                self._zatankuj_paliwo(paliwo, litry, nr_rej)
            elif akcja == 'u':
                paliwo = input('Podaj oznaczenie paliwa: ')
                litry = int(input('Ile litrów chcesz uzupełnić?'))
                self._uzupelnij_paliwo(paliwo, litry)
            elif akcja == 'c':
                paliwo = input('Podaj oznaczenie paliwa: ')
                cena = float(input('Podaj cenę litra paliwa: '))
                self._ustal_cene_paliwa(paliwo, cena)
            elif akcja == 'k':
                break
            else:
                print('Nieprawidłowa akcja!')

    def _wypisz_paliwa(self):
        for p in self._stacja.wypisz_paliwa():
            print(p)

    def _uzupelnij_paliwo(self, paliwo, ile_litrow):
        try:
            self._stacja.uzupelnij(paliwo, ile_litrow)
        except ZlePaliwoError:
            print(f'Stacja nie obsługuje paliwa {paliwo.upper()}!')

    def _ustal_cene_paliwa(self, paliwo, cena):
        try:
            self._stacja.ustal_cene(paliwo, cena)
        except ZlePaliwoError:
            print(f'Stacja nie obsługuje paliwa {paliwo.upper()}!')

    def _zatankuj_paliwo(self, paliwo, litry, nr_rej):
        try:
            numer_rej = nr_rej if nr_rej else None
            cena = self._stacja.zatankuj(paliwo, litry, numer_rej)
            print(f'Do zapłaty {cena:.2f} PLN')
        except BrakPaliwaError:
            print(
                f'Przepraszamy, brak paliwa {paliwo.upper()} w wystarczającej ilości!')
        except ZlePaliwoError:
            print(f'Stacja nie obsługuje paliwa {paliwo.upper()}!')


if __name__ == '__main__':
    interfejs_stacji = InterfejsStacjiPaliw()
    interfejs_stacji.run()
