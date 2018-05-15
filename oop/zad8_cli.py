from oop.zad8 import CashMachine, CashMachineFullError, BanknotesNotAvailableError, \
    BadMoneyAmountError


class CashMachineCLI:
    def __init__(self):
        self._cash_machine = CashMachine()

    def run(self):
        while True:
            print(
                f'Pojemność bankomatu: {self._cash_machine.banknote_limit()} banknotów.\n')
            op = input(
                'Podaj typ operacji: (n)owy bankomat, (d)ostępność, (w)ypłata, w(p)łata, (k)oniec: ')
            if op == 'n':
                try:
                    self._cash_machine = CashMachine(
                        int(input('Podal limit banknotów: ')))
                except ValueError:
                    print('Niewłaściwa liczba określająca limit banknotów!')
            elif op == 'd':
                if self._cash_machine.is_available():
                    print('Bankomat dostępny.')
                else:
                    print('Bankomat niedostępny!')
            elif op == 'w':
                try:
                    banknotes = self._cash_machine.withdraw_money(
                        int(input('Podaj kwotę wypłaty: ')))
                    print(f'Wypłacona banknoty: {banknotes}')
                except ValueError:
                    print('Niewłaściwa kwota - podaj liczbę całkowitą!')
                except BadMoneyAmountError:
                    print('Niewłaściwa kwota - podaj liczbę podzielną przez 10!')
                except BanknotesNotAvailableError:
                    print('Żądanej kwoty nie da się wypłacić!')
            elif op == 'p':
                try:
                    banknotes = [int(n) for n in
                                 input('Podaj listę banknotów: ').split()]
                    self._cash_machine.put_money(banknotes)
                except ValueError:
                    print('Niepoprawna wartość banknotów!')
                except CashMachineFullError:
                    print('Bankomat pełny!')
            elif op == 'k':
                break
            else:
                print('Niepoprawna operacja!')


if __name__ == '__main__':
    cli = CashMachineCLI()
    cli.run()
