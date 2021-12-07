from functools import reduce
import psycopg2
from random import choice

from holders_and_insured.users import User

conn = psycopg2.connect(dbname='insurance_advisor', user='vladislav',
                        password='M8aBBE97', host='localhost')

# policy_holders = list(map(lambda _: User(holder_id=None), range(50)))
# companies_values = reduce(lambda a, b: str(a) + ', ' + str(b), policy_holders)


with conn.cursor() as cursor:
    cursor.execute('SELECT id FROM policy_holders;')
    records = cursor.fetchall()
    # Records is list of single-element tuples, so we need to unpack them
    records = list(map(lambda a: a[0], records))

insured = list(map(lambda _: User(holder_id=choice(records)), range(125)))
insured_values = reduce(lambda a, b: str(a) + ', ' + str(b), insured)

with conn.cursor() as cursor:
    cursor.execute('INSERT INTO insured'
                   ' (first_name, last_name, document_number, birth_date, holder_id) VALUES '
                   + insured_values + ';')
    conn.commit()
    cursor.execute('SELECT * FROM insured;')
    records = cursor.fetchall()
    print(records)
