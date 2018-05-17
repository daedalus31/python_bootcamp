import json
import urllib.request


def load_rates(URL):
    with urllib.request.urlopen(URL) as response:
        data = response.read().decode('utf-8')
        data = json.loads(data)[0]['rates']
        return {r['code']: r for r in data}


def list_currencies(currency_rates):
    print('Waluty do wyboru: ')
    for c in currency_rates:
        print(f'{c} ({currency_rates[c]["currency"]})')


def buy_currency(currencies):
    currency_to_buy = input("Jaką walutę chcesz kupić? ").upper()
    try:
        pln_to_change = float(input("Ile PLN chcesz wymienić? "))
        bought_amount = pln_to_change / currencies[currency_to_buy]['mid']
        print(f'Możesz kupić {bought_amount:.2f} {currency_to_buy}')
    except KeyError:
        pass
    except TypeError:
        pass


def sell_currency(currencies):
    currency_to_sell = input("Jaką walutę chcesz sprzedać? ").upper()
    try:
        to_change = float(input(f'Ile {currency_to_sell} chcesz wymienić? '))
        bought_amount = to_change * currencies[currency_to_sell]['mid']
        print(f'Możesz dostać {bought_amount:.2f} PLN')
    except KeyError:
        pass
    except TypeError:
        pass


if __name__ == '__main__':
    URL = 'http://api.nbp.pl/api/exchangerates/tables/A/?format=json'
    currencies = load_rates(URL)
    list_currencies(currencies)
    action = input(f'Co chcez zrobić? [s/k]')
    if action == 'k':
        buy_currency(currencies)
    elif action == 's':
        sell_currency(currencies)
    else:
        print('Nieprawidłowa akcja!')
