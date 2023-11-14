from dataclasses import dataclass

class information:
    def __init__(self, name, address, age, phone_number):
        self.name = name
        self.address = address
        self.age = age
        self.phone_number = phone_number


    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_age(self):
        return self.age

    def get_phone_number(self):
        return self.phone_number

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def set_age(self, age):
        self.age = age

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def __str__(self):
        return f'{self.name},{self.age},{self.address},{self.phone_number}'

personal_info = information('Саша', 'ул.Норд-Драйв 7а', '23', '+79874920177')
print(personal_info)
personal_info2 = information('Паша', 'Парковая 56', '16', '+89174582432')
print(personal_info2)
personal_info3 = information('Иван', 'ул.Ленина 15', '33', '+89899595777')
print(personal_info3)
