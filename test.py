import psycopg2


conn = psycopg2.connect(dbname='insurance_advisor', user='vladislav',
                        password='M8aBBE97', host='localhost')


with conn.cursor() as cursor:
    cursor.execute(f'SELECT id FROM zones WHERE name = \'Шенгенская зона\';')
    records = cursor.fetchall()
    print(records[0][0])
