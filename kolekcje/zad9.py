price_list = {
    'ziemniaki':{
        'price': 2.1,
        'quantity': 900.0,
    },
    'marchew': {
        'price': 1.5,
        'quantity': 120.0,
    },
}

while True:
    print('Witamy w PyWarzywa, co chcesz zrobić?')
    command = input(
        'sprzedaj [s], dodaj [d], wyświetl cennik [c], usuń produkt [u], zakończ [k]: ')

    if command == 'k':
        break
    elif command == 'c':
        for veg in price_list:
            print(
                f'{veg}: {price_list[veg]["price"]:.2f} PLN, dostępne {price_list[veg]["quantity"]} kg')
    elif command == 'u':
        to_delete = input('Podaj produkt do usunięcia: ')
        if to_delete in price_list:
            del price_list[to_delete]
        else:
            print(f'Produkt "{to_delete}" nie występuje w cenniku!')
    elif command == 'd':
        product_name = input('Podaj nazwę produktu: ')
        price = input('Podaj cenę produktu: ')
        quantity = input('Ile produktu chcesz dodać? ')
        price_list[product_name] = {'price': float(price),
                                    'quantity': float(quantity)}
    elif command == 's':
        product_name = input('Co chcesz sprzedać? ')
        quantity = int(input(f'Ile chcesz kupić produktu "{product_name}"? '))
        if product_name in price_list and price_list[product_name][
            'quantity'] >= quantity:
            print(f'Do zapłaty: {price_list[product_name]["price"]*quantity:.2f} PLN')
            price_list[product_name]['quantity'] -= quantity
        else:
            print(
                f'Brak produktu {product_name} w sklepie w poszukiwanej ilości!')
