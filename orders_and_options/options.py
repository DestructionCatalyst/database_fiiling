from functools import reduce
import option_descriptions as desc
import psycopg2
from random import choice, randint, sample

conn = psycopg2.connect(dbname='insurance_advisor', user='vladislav',
                        password='M8aBBE97', host='localhost')

with conn.cursor() as cursor:
    cursor.execute('SELECT id FROM insurance_orders;')
    records = cursor.fetchall()
    # Records is list of single-element tuples, so we need to unpack them
    orders = list(map(lambda a: a[0], records))


class OptionType:
    def __init__(self, name, description, amount_variants, min_base_price, max_base_price, min_daily_price, max_daily_price):
        self.name = name
        self.description = description
        self.amount_variants = amount_variants
        self.min_base_price = min_base_price
        self.max_base_price = max_base_price
        self.min_daily_price = min_daily_price
        self.max_daily_price = max_daily_price

    # name | description | insurance_amount | base_price | daily_price
    def __str__(self):
        return f"('{self.name}', '{self.description}', {choice(self.amount_variants)}, " \
               f"{randint(self.min_base_price, self.max_base_price)}, " \
               f"{randint(self.min_daily_price, self.max_daily_price)})"


med_insurance = OptionType('Медицинское страхование', desc.med, [2_500_000, 3_000_000, 3_320_000, 4_150_000, 8_300_000],
                           70, 150, 30, 50)

extra_options = [OptionType('Страхование от несчастных случаев', desc.accidents, [83_000, 250_000, 415_000, 830_000],
                            20, 50, 10, 40),
                 OptionType('Страхование багажа', desc.baggage, [41_500, 83_000, 125_000, 166_000], 10, 40, 5, 30),
                 OptionType('Страхование перелета', desc.flight, [41_500, 83_000, 125_000, 166_000], 10, 40, 5, 30),
                 OptionType('Страхование багажа', desc.baggage, [41_500, 83_000, 125_000, 166_000], 10, 40, 5, 30),
                 OptionType('Страхование потери документов', desc.document_lost, [41_500, 83_000, 125_000, 166_000],
                            10, 40, 5, 30),
                 OptionType('Юридическая помощь', desc.jury_help, [41_500, 83_000, 125_000, 166_000], 10, 40, 5, 30),
                 OptionType('Страхование на случай осложнения беременности ', desc.pregnancy,
                            [41_500, 83_000, 125_000, 166_000], 10, 40, 5, 30),
                 OptionType('Страхование гражданской ответственности', desc.gr_otv, [41_500, 83_000, 125_000, 166_000],
                            10, 40, 5, 30),
                 OptionType('Поездка на личном автомобиле', desc.auto, [41_500, 83_000, 125_000, 166_000], 10, 40, 5, 30),
                 ]

with conn.cursor() as cursor:
    for order in orders:
        available_options = [med_insurance] + sample(extra_options, 2)
        for option in available_options:
            cursor.execute('INSERT INTO insurance_options'
                           ' (name, description, insurance_amount, base_price, daily_price) VALUES '
                           + str(option) + ';')
            conn.commit()
            cursor.execute('SELECT MAX(id) FROM insurance_options;')
            records = cursor.fetchall()
            option_id = records[0][0]
            cursor.execute(f'INSERT INTO availible_options (option_id, order_id) VALUES ({option_id}, {order});')
            conn.commit()


