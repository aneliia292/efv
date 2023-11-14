from dataclasses import dataclass

@dataclass
class Retailitem:
    def __init__(self, thing, sklad, price):
        self.thing = thing
        self.sklad = sklad
        self.price = price

    def __str__(self):
        return f'{self.thing}, {self.sklad}, {self.price}'


product = Retailitem ('Пиджак', '12', 59)
print(product)
product2 = Retailitem ('Джинсы', '40', 34)
print(product2)
product3 = Retailitem ('Рубашка', '20', 24)
print(product3)

