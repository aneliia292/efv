class Employee:
    def __init__(self, name, number_id, departament, job):
        self.name = name
        self.number_id = number_id
        self.departament = departament
        self.job = job

    def set_name(self, name):
        self.name = name

    def set_number_id(self, number_id):
        self.number_id = number_id

    def set_departament(self, departament):
        self.departament = departament

    def set_job(self, job):
        self.job = job



    def __str__(self):
        return f'{self.name}, {self.number_id}, {self.departament}, {self.job}'

def e_list(key, value, dict):
    dict[key] = value
    return dict


def e_search(dict, name, counter):
    res = {}
    for key in dict:
        if name ==  dict[key].name:
            res = (dict[key])
    if res:
        print(dict[key])
    else:
        print('нет такого')


def e_change(name, departament, job, Emp):
    Emp.set.name(name)
    Emp.set.departament(departament)
    Emp.set.job(job)


def e_delete(key, dict):
    del dict[key]


counter = 0
reestr = {}
chel = Employee('Сьюзан Мейерс', '47899', 'Бухгалерия','Вице-президент')
e_list(counter, chel, reestr)
counter += 1
chel2 = Employee('Марк Джоунс', '39119', 'ИТ','Программист')
e_list(counter, chel2, reestr)
counter += 2
chel3 = Employee('Джой Роджерс', '81774', 'Производственный ','Инженер')
e_list(counter, chel3, reestr)


e_search(reestr, 'Марк Джоунс')
e_change('wvrwrtb', 'ebtbw', 'wbwb', reestr[0])
print(reestr[0])
e_delete(0, reestr)
print(reestr[0])

