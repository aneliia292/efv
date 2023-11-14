from dataclasses import dataclass

@dataclass
class Patient:
    address: str
    town: str
    mail: int
    phone: int
    fio: str

    def get_address(self, address):
        return self.address

    def get_town(self, town):
        return self.town

    def get_mail(self, mail):
        return self.mail

    def get_phone(self, phone):
        return self.phone

    def get_fio(self, fio):
        return self.fio

    def get_proctdures(self):
        for i in range()



    def set_address(self, address):
        self.address = address

    def set_town(self, town):
        self.address = town

    def set_mail(self, mail):
        self.address = mail

    def set_phone(self, phone):
        self.address = phone

    def set_fio(self, fio):
        self.address = fio


    def __str__(self):
        return f'{self.address},{self.town}, {self.mail}, {self.phone}, {self.fio}'

patient = Patient('Норд-Драйв7а', 'Елабуга, Resbublika Tatarstan', 'Alabuga@gmail.com', '+89876534222', 'Филипов Павел Максимович')


@dataclass
class Procedure:
    name_proceduri: str
    data_proc: str
    doctor: str
    price: int

    def get_name_proceduri(self, name_proceduri):
        return self.name_proceduri

    def get_data_proc(self, data_proc):
        return self.data_proc

    def get_doctor(self, doctor):
        return self.doctor

    def get_proctdures(self):
        for i in range()



    def set_name_proceguri(self, name_proceguri):
        self.name_proceduri = name_proceguri

    def set_data_proc(self, data_proc):
        self.data_proc = data_proc

    def set_doctor(self, doctor):
        self.doctor = doctor

    def set_price(self, price):
        self.price = price



    def __str__(self):
        return f'Название процедуры: {self.name_proceduri}, дата рождения: {self.data_proc}, доктор: {self.doctor}, цена: {self.price}'



patient = Patient('Shihkino')