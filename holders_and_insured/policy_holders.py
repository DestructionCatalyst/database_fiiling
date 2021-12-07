from functools import reduce
import psycopg2

from users import User

conn = psycopg2.connect(dbname='insurance_advisor', user='vladislav',
                        password='M8aBBE97', host='localhost')

policy_holders = list(map(lambda _: User(holder_id=None), range(50)))
companies_values = reduce(lambda a, b: str(a) + ', ' + str(b), policy_holders)


with conn.cursor() as cursor:
    cursor.execute('INSERT INTO policy_holders'
                   ' (first_name, last_name, document_number, birth_date, phone) VALUES '
                   + companies_values + ';')
    conn.commit()
    cursor.execute('SELECT * FROM policy_holders;')
    records = cursor.fetchall()
    print(records)
