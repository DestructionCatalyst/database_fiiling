from functools import reduce
import option_descriptions as desc
import psycopg2
from random import choice, randint, sample

conn = psycopg2.connect(dbname='insurance_advisor', user='vladislav',
                        password='M8aBBE97', host='localhost')

with conn.cursor() as cursor:
    # Get all holders and orders
    cursor.execute('SELECT id FROM policy_holders;')
    records = cursor.fetchall()
    # Records is list of single-element tuples, so we need to unpack them
    holders = list(map(lambda a: a[0], records))
    cursor.execute('SELECT id FROM insurance_orders;')
    records = cursor.fetchall()
    # Records is list of single-element tuples, so we need to unpack them
    orders = list(map(lambda a: a[0], records))
    # Add deal for every holder
    for holder in holders:
        order = choice(orders)
        cursor.execute(f'SELECT option_id FROM availible_options WHERE order_id = {order};')
        records = cursor.fetchall()
        # Records is list of single-element tuples, so we need to unpack them
        options = list(map(lambda a: a[0], records))
        selected_options = [options[0], choice(options[1:])]
        start_date = f'2021-11-{str(randint(25, 30))}'
        end_date = f'2021-12-{str(randint(1, 31)).zfill(2)}'
        cursor.execute(f'INSERT INTO insurance_deals'
                       f' (order_id, holder_id, start_date, end_date) VALUES '
                       f' ({order}, {holder}, \'{start_date}\', \'{end_date}\');')
        conn.commit()
        cursor.execute('SELECT MAX(id) FROM insurance_deals;')
        # Add options for every deal
        records = cursor.fetchall()
        deal = records[0][0]
        for option in selected_options:
            cursor.execute(f'INSERT INTO selected_options (option_id, deal_id) VALUES ({option}, {deal});')
