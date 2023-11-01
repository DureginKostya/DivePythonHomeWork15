import argparse
from logging_creating_human import log_dec, logger
from user_descriptors.ExaminationDataForCreateHuman import ExaminationData


class Person:
    last_name = ExaminationData()
    first_name = ExaminationData()
    patronymic = ExaminationData()
    age = ExaminationData()

    def __init__(self, last_name, first_name, patronymic, age):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.age = age

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age


class Employee(Person):
    id_employee = ExaminationData()

    def __init__(self, last_name, first_name, patronymic, age, id_employee):
        super().__init__(last_name, first_name, patronymic, age)
        self.id_employee = id_employee

    def get_level(self):
        number = self.id_employee
        sum_digit = 0
        while number > 0:
            sum_digit += number % 10
            number //= 10
        return sum_digit % 7


@log_dec
def par():
    parser = argparse.ArgumentParser(description='Create class Person or Employee')
    parser.add_argument('-c', '--class_', default='Person')
    parser.add_argument('-lst', '--last_name', default='')
    parser.add_argument('-fst', '--first_name', default='')
    parser.add_argument('-ptr', '--patronymic', default='')
    parser.add_argument('-a', '--age', type=int, default=-1)
    parser.add_argument('-id_emp', '--id_employee', type=int, default=None)
    args = parser.parse_args()
    if args.class_ == 'Employee':
        return Employee(args.last_name, args.first_name, args.patronymic, args.age, args.id_employee)
    return Person(args.last_name, args.first_name, args.patronymic, args.age)


if par():
    if isinstance(par(), Employee):
        logger.info(f'Created class Employee with parameters: '
                    f'Last_name: {par().last_name}, '
                    f'First_name: {par().first_name}, '
                    f'Patronymic: {par().patronymic}, '
                    f'Age: {par().age}, '
                    f'Id_employee: {par().id_employee}.')
    else:
        logger.info(f'Created class Person with parameters: '
                    f'Last_name: {par().last_name}, '
                    f'First_name: {par().first_name}, '
                    f'Patronymic: {par().patronymic}, '
                    f'Age: {par().age}.')
else:
    logger.info('Class not created')

"""
Проверочные данные:

python create_human.py -c Person -fst John -ptr Doe -a 30 

python create_human.py -c Person -lst Alice -fst Smith -ptr Johnson -a -5 

python create_human.py -c Employee -lst Bob -fst Johnson -ptr Brown -a 40 -id_emp 12345 

python create_human.py -c Person -lst Alice -fst Smith -ptr Johnson -a 25 
    
python create_human.py -c Employee -lst Bob -fst Johnson -ptr Brown -a 40 -id_emp 123456    
"""
