class CashMachine:
    def __init__(self):
        self._available_banknotes = []

    def is_available(self):
        return bool(self._available_banknotes)

    def put_money(self, banknotes):
        self._available_banknotes += banknotes

    def withdraw_money(self, amount):
        money_to_withdraw = []
        for banknote in sorted(self._available_banknotes, reverse=True):
            if sum(money_to_withdraw) + banknote < amount:
                money_to_withdraw.append(banknote)
            elif sum(money_to_withdraw) + banknote == amount:
                money_to_withdraw.append(banknote)
                for bn in money_to_withdraw:
                    self._available_banknotes.remove(bn)
                return money_to_withdraw
        return []


class CashMachineWithLimit(CashMachine):
    def __init__(self, limit):
        super().__init__()
        self.limit = limit

    def withdraw_money(self, amount):
        if amount > self.limit:
            amount = self.limit
        return super().withdraw_money(amount)


def test_cash_machine_with_limit():
    cm = CashMachineWithLimit(300)
    cm.put_money([100, 50, 100, 200])

    banknotes = cm.withdraw_money(400)

    assert banknotes == [200, 100]


def test_empty_is_not_available():
    cm = CashMachine()
    assert not cm.is_available()


def test_not_empty_is_available():
    cm = CashMachine()
    cm.put_money([100])

    assert cm.is_available()


def test_withdraw_existing_money():
    cm = CashMachine()
    cm.put_money([50, 50, 100, 200])

    money = cm.withdraw_money(350)

    assert sum(money) == 350


def test_withdraw_many_times():
    cm = CashMachine()
    cm.put_money([50, 50, 100, 200])
    cm.withdraw_money(350)

    money = cm.withdraw_money(350)

    assert money == []


def test_withdraw_too_much_money():
    cm = CashMachine()
    cm.put_money([50, 50, 100, 200])

    money = cm.withdraw_money(800)

    assert money == []


def test_impossible_amount_of_money():
    cm = CashMachine()
    cm.put_money([50, 50, 100, 200])

    money = cm.withdraw_money(120)

    assert money == []
