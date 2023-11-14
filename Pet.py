from dataclasses import dataclass

@dataclass
class Pet:
    def __init__(self, name, animal_type, age):
        self._name = name
        self._animal_type = animal_type
        self.age = age

    def set_name(self, name):
        print('Ввкдик')
        self._name = name

    def set_animal_type(self, animal_type):
        self._animal_type = animal_type

    def set_age(self, age):
        self._age = age

    def get_name(self):
        return self._name

    def get_animal_type(self):
        return self._animal_type

    def get_age(self):
        return self._age


pet1 = Pet('Шарик', 'Кот', 3)
print(pet1.get_name())
print(pet1.get_animal_type())
print(pet1.get_age())
