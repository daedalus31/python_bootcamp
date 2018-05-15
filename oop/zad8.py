import pytest


class CashMachineError(Exception):
    pass


class CashMachineFullError(CashMachineError):
    pass


class BanknotesNotAvailableError(CashMachineError):
    pass


class BadMoneyAmountError(CashMachineError):
    pass


class CashMachine:
    def __init__(self, banknote_limit=100):
        self._available_banknotes = []
        self._banknote_limit = banknote_limit

    def banknote_limit(self):
        return self._banknote_limit

    def is_available(self):
        return bool(self._available_banknotes)

    def put_money(self, banknotes):
        if len(self._available_banknotes) + len(banknotes) > self._banknote_limit:
            raise CashMachineFullError()
        self._available_banknotes += banknotes

    def withdraw_money(self, amount):
        if amount % 10 != 0:
            raise BadMoneyAmountError
        money_to_withdraw = []
        for banknote in sorted(self._available_banknotes, reverse=True):
            if sum(money_to_withdraw) + banknote < amount:
                money_to_withdraw.append(banknote)
            elif sum(money_to_withdraw) + banknote == amount:
                money_to_withdraw.append(banknote)
                for bn in money_to_withdraw:
                    self._available_banknotes.remove(bn)
                return money_to_withdraw
        raise BanknotesNotAvailableError()


def test_bad_amount_of_money():
    with pytest.raises(BadMoneyAmountError):
        cm = CashMachine()
        cm.withdraw_money(121)


def test_banknotes_not_available():
    cm = CashMachine()
    cm.put_money([100])
    with pytest.raises(BanknotesNotAvailableError):
        cm.withdraw_money(80)


def test_banknotes_limit():
    cm = CashMachine(150)
    banknotes = [100] * 154

    with pytest.raises(CashMachineFullError):
        cm.put_money(banknotes)
