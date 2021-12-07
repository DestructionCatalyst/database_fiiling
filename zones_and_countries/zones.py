import psycopg2
from functools import reduce


conn = psycopg2.connect(dbname='insurance_advisor', user='vladislav',
                        password='M8aBBE97', host='localhost')

zones = ['Шенгенская зона',
         'Острова Карибского бассейна',
         'Юго-Восточная Азия',
         'Острова Океании']

zones_values = reduce(lambda zone1, zone2: zone1 + ', ' + zone2, map(lambda zone: '(\'' + zone + '\')', zones))

with conn.cursor() as cursor:
    cursor.execute('INSERT INTO zones (name) VALUES ' + zones_values + ';')
    conn.commit()
    cursor.execute('SELECT * FROM zones;')
    records = cursor.fetchall()
    print(records)


