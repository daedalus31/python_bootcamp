class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def print_info(self):
        print(f'Produkt "{self.name}", id: {self.product_id}, cena: {self.price} PLN')

    def __eq__(self, other):
        return self.product_id == other.product_id


class BasketItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity


class Basket:
    def __init__(self):
        self._items = []
        self._discount = None

    def set_discount_type(self, discount_type):
        self._discount = discount_type

    def _get_item_index(self, product):
        for index, item in enumerate(self._items):
            if item.product == product:
                return index
        return None

    def add_product(self, product, quantity):
        ind = self._get_item_index(product)
        if ind is not None:
            self._items[ind].quantity += quantity
        else:
            self._items.append(BasketItem(product, quantity))

    def calculate_total_price(self):
        res = 0.0
        for p in self._items:
            res += p.product.price * p.quantity
        if self._discount is not None:
            discount = self._discount.calculate_discount(res)
        else:
            discount = 0.0
        return res - discount

    def generate_report(self):
        report = 'Produkty w koszyku:\n'
        for p in self._items:
            report += f'- {p.product.name} ({p.product.product_id}), cena: {p.product.price:.2f} x {p.quantity}\n'
        report += f'W sumie {self.calculate_total_price():.2f}'
        return report

    def remove_product(self, product, quantity):
        ind = self._get_item_index(product)
        if ind is not None:
            if self._items[ind].quantity > quantity:
                self._items[ind].quantity -= quantity
            else:
                del self._items[ind]

    @staticmethod
    def with_products(product_list):
        result = Basket()
        for p in product_list:
            result.add_product(p, 1)
        return result


class Discount:
    def calculate_discount(self, price):
        raise NotImplementedError


class PercentageDiscount(Discount):
    def __init__(self, percentage):
        self._percentage = percentage

    def calculate_discount(self, price):
        return price * self._percentage * 0.01


class ValueDiscount(Discount):
    def __init__(self, value):
        self._value = value

    def calculate_discount(self, price):
        return self._value


def test_add_product():
    product = Product(1, 'woda', 2.00)
    basket = Basket()

    basket.add_product(product, 1)
    basket.add_product(product, 1)
    assert basket._items[0].product == product


def test_count_total_price_empty():
    basket = Basket()

    assert basket.calculate_total_price() == 0


def test_count_total_price_nonempty():
    product = Product(1, 'woda', 2.00)
    expensive_product = Product(2, 'złoto', 500.00)
    basket = Basket()

    basket.add_product(product, 1)
    basket.add_product(product, 1)
    basket.add_product(expensive_product, 1)

    assert basket.calculate_total_price() == 504.00


def test_report_empty():
    basket = Basket()

    assert basket.generate_report() == 'Produkty w koszyku:\nW sumie 0.00'


def test_report_nonempty():
    product = Product(1, 'woda', 2.00)
    expensive_product = Product(2, 'złoto', 500.00)
    basket = Basket()

    basket.add_product(product, 1)
    basket.add_product(product, 1)
    basket.add_product(expensive_product, 1)

    assert basket.generate_report() == 'Produkty w koszyku:\n- woda (1), cena: 2.00 x 2\n- złoto (2), cena: 500.00 x 1\nW sumie 504.00'


def test_removing_single_product():
    product = Product(1, 'woda', 2.00)
    expensive_product = Product(2, 'złoto', 500.00)
    basket = Basket()

    basket.add_product(product, 1)
    basket.add_product(product, 1)
    basket.add_product(expensive_product, 1)
    basket.remove_product(product, 1)

    assert basket.calculate_total_price() == 502.00


def test_removing_multiple_products():
    product = Product(1, 'woda', 2.00)
    expensive_product = Product(2, 'złoto', 500.00)
    basket = Basket()

    basket.add_product(product, 3)
    basket.add_product(expensive_product, 1)
    basket.remove_product(product, 2)
    basket.remove_product(expensive_product, 1)

    assert basket.calculate_total_price() == 2.00


def test_percentage_discount():
    product = Product(1, 'woda', 1.00)
    basket = Basket()
    basket.add_product(product, 10)
    basket.set_discount_type(PercentageDiscount(20.0))

    total = basket.calculate_total_price()

    assert total == 8.00


def test_value_discount():
    product = Product(1, 'woda', 1.00)
    basket = Basket()
    basket.add_product(product, 10)
    basket.set_discount_type(ValueDiscount(3.0))

    total = basket.calculate_total_price()

    assert total == 7.00


def test_basket_with_products():
    water = Product(1, 'woda', 1.00)
    cola = Product(2, 'cola', 3.00)

    basket = Basket.with_products([water, cola])

    assert basket.calculate_total_price() == 4.00
