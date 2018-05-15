class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def print_info(self):
        print(f'Produkt "{self.name}", id: {self.product_id}, cena: {self.price} PLN')


if __name__ == '__main__':
    cokolwiek = Product(2, 'cokolwiek', 56)
    cokolwiek.print_info()
