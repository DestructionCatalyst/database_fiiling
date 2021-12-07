import psycopg2
from functools import reduce
from countries_list import countries, zone_sets


conn = psycopg2.connect(dbname='insurance_advisor', user='vladislav',
                        password='M8aBBE97', host='localhost')

zones_for_countries = []


def country_to_value(country):
    for zone in zone_sets:
        if country in zone:
            return '(\'' + country + '\', ' + str(zone_sets[zone]) + ')'
    with conn.cursor() as cursor:
        cursor.execute('INSERT INTO zones (name) VALUES (\'' + country + '\');')
        conn.commit()
        cursor.execute(f'SELECT id FROM zones WHERE name = \'{country}\';')
        records = cursor.fetchall()
        return '(\'' + country + '\', ' + str(records[0][0]) + ')'


countries_values = reduce(lambda country1, country2: country1 + ', ' + country2,
                          map(country_to_value, countries))

with conn.cursor() as cursor:
    cursor.execute('INSERT INTO countries (name, zone_id) VALUES ' + countries_values + ';')
    conn.commit()
    cursor.execute('SELECT * FROM countries;')
    records = cursor.fetchall()
    print(records)

