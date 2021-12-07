from functools import reduce

import psycopg2
from random import choice, sample

conn = psycopg2.connect(dbname='insurance_advisor', user='vladislav',
                        password='M8aBBE97', host='localhost')

with conn.cursor() as cursor:
    cursor.execute('SELECT id FROM zones WHERE id < 5;')
    records = cursor.fetchall()
    # Records is list of single-element tuples, so we need to unpack them
    big_zones = list(map(lambda a: a[0], records))
    cursor.execute('SELECT id FROM zones WHERE id >= 5;')
    records = cursor.fetchall()
    # Records is list of single-element tuples, so we need to unpack them
    small_zones = list(map(lambda a: a[0], records))
    cursor.execute('SELECT id FROM insurance_companies;')
    records = cursor.fetchall()
    # Records is list of single-element tuples, so we need to unpack them
    companies = list(map(lambda a: a[0], records))

orders = []

for company in companies:
    available_big_zones = sample(big_zones, 2)
    available_small_zones = sample(small_zones, 30)
    available_zones = available_big_zones + available_small_zones
    # zone_id | company_id | min_age | max_age | franchise
    for zone in available_zones:
        orders.append(f'({zone}, {company}, {choice([0, 3, 14, 16, 18])}, {choice([60, 80, 100])}, {choice([0, 5000])})')

orders_values = reduce(lambda a, b: str(a) + ', ' + str(b), orders)

with conn.cursor() as cursor:
    cursor.execute('INSERT INTO insurance_orders'
                   ' (zone_id, company_id, min_age, max_age, franchise) VALUES '
                   + orders_values + ';')
    conn.commit()
    cursor.execute('SELECT * FROM insurance_orders;')
    records = cursor.fetchall()
    print(records)
