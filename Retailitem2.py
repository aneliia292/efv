from dataclasses import dataclass, field

@dataclass
class Retailitem:
    name: str
    discription: str
    kolvo: int
    price: float

    def __str__(self):
        return f'Имя - {self.name},{self.discription}, {self.kolvo}, {self.price}'
@dataclass
class CashRegister:
    item_list: list = field(default_factory=list)


    def purchase_item(self, purchase):
        self.item_list.append(purchase)
    def get_total(self):
        total_summ = 0
        for i in self.item_list:
            total_summ += i.price
        return total_summ

    def show_items(self):
        for i in self.item_list:
            print(i)

    def clear_register(self):
        self.item_list = ['eefbe']


cach_register = CashRegister()
item1 = Retailitem('name', 'discription', 10, 15.99)
item2 = Retailitem('name', 'discription', 10, 15.99)
item3 = Retailitem('name', 'discription', 10, 15.99)
# print(item1)
cach_register.purchase_item(item2)
cach_register.purchase_item(item1)
cach_register.show_items()
print(f'total: {cach_register.get_total()}')
cach_register.clear_register()
cach_register.show_items()