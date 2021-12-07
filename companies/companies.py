from functools import reduce

import psycopg2
from random import randint, choice

cities = ['Москва', 'Санкт-Петербург', 'Казань', 'Новосибирск', 'Челябинск']
streets = ['Пушкина', 'Ленина', 'Достоевского', 'Жукова', 'Дзержинского',  'Гагарина']


class Company:
    def __init__(self, name, english_name):
        self.name = name
        self.email = f'support@{english_name}.ru'
        self.website = f'https://{english_name}.ru'
        self.phone = f'+7800{randint(100_00_00, 999_99_99)}'
        self.inn = str(randint(10 ** 11, 10 ** 12 - 1))
        self.bank_account = str(randint(10 ** 19, 10 ** 20 - 1))
        self.correspondent_account = str(randint(10 ** 19, 10 ** 20 - 1))
        self.bik = str(randint(10 ** 8, 10 ** 9 - 1))
        index = randint(10 ** 5, 10 ** 6 - 1)
        self.address = f'{index}, Россия, г. {choice(cities)}, ул. {choice(streets)},' \
                       f' д. {randint(1, 300)}, офис {randint(1, 5)}'

    # id | name | phone | email | inn | bank_account | correspondent_account | bik | address | website
    def __str__(self):
        return f"('{self.name}', '{self.phone}', '{self.email}', '{self.inn}', '{self.bank_account}', " \
               f"'{self.correspondent_account}', '{self.bik}', '{self.address}', '{self.website}')"


companies = [('ООО "Страходром"', 'strahodrom'), ('ГазМясСтрах', 'gms'), ('СК "Париж"', 'paris-sk'),
             ('Перфекто Страхование', 'perfecto'), ('СК "Твой Гарант"', 'your-garant'), ('Зарубежстрах', 'zarub-strah'),
             ('Капиталбанк страхование', 'capital-strah'), ('Страховой дом СКП', 'scp-strah'),
             ('Сигма страхование', 'sigmastrah')]

companies = list(map(lambda name: Company(name[0], name[1]), companies))


conn = psycopg2.connect(dbname='insurance_advisor', user='vladislav',
                        password='M8aBBE97', host='localhost')

companies_values = reduce(lambda zone1, zone2: str(zone1) + ', ' + str(zone2), companies)

# print(companies_values)

with conn.cursor() as cursor:
    pass
    cursor.execute('INSERT INTO insurance_companies'
                   ' (name, phone, email, inn, bank_account, correspondent_account, bik, address, website) VALUES '
                   + companies_values + ';')
    conn.commit()
    cursor.execute('SELECT * FROM insurance_companies;')
    records = cursor.fetchall()
    print(records)
