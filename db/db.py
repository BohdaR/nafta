import re

import psycopg2
import psycopg2.extras
import os
from dotenv import load_dotenv
from pluralizer import Pluralizer

pluralizer = Pluralizer()
load_dotenv()
env = os.environ


class Database:
    def __init__(self):
        self.connection = psycopg2.connect(**{
            'database': env['DB_NAME'],
            'host': env['DB_HOST'],
            'port': env['DB_PORT'],
            'user': env['DB_USER'],
            'password': env['DB_PASS'],
        })
        self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        self.subject = '_'.join(map(
            lambda i: i.lower(),
            re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', type(self).__name__)))

    def __get_condition_template(self, conditions):
        query = f"WHERE {' AND '.join(map(lambda i: f'{self.subject}.{i}=%s', conditions))}"
        return query

    def __get_join_query(self, columns, params):
        query = f'''
                SELECT {self.subject}.id,
                    {','.join(map(lambda i: f'{self.subject}.{i}', columns))},
                    {','.join(map(lambda i: f'{i[0][0]}.{i[0][1]} as {i[1]}', params.items()))}
                FROM {self.subject}
                {' '.join(map(lambda i: f'INNER JOIN {i[0][0]} on {i[0][0]}.id = {self.subject}.{pluralizer.singular(i[0][0])}_id', params.items()))}
                '''
        print(query)
        return query

    def join(self, columns, params, conditions=None):
        if conditions:
            query = f'{self.__get_join_query(columns, params)} {self.__get_condition_template(list(conditions.keys()))}'
            print(query)
            self.cursor.execute(query, tuple(conditions.values()))
        else:
            self.cursor.execute(self.__get_join_query(columns, params))
        return self.cursor.fetchall()

    def all(self):
        self.cursor.execute(f'SELECT * FROM {self.subject}')
        return self.cursor.fetchall()

    def find(self, pk):
        self.cursor.execute(f'SELECT * FROM {self.subject} WHERE id=%s;', (int(pk),))
        return self.cursor.fetchall()

    def find_by(self, column, value):
        self.cursor.execute(f'SELECT * FROM {self.subject} WHERE {column}=%s;', (int(value),))
        return self.cursor.fetchall()

    def create(self, data: dict):
        columns = ','.join(map(str, data.keys()))
        values = ','.join(map(lambda i: f"'{i}'", data.values()))

        query = f"INSERT INTO {self.subject} ({columns}) VALUES ({values}) RETURNING id, {columns};"
        self.cursor.execute(query)
        self.connection.commit()

        return self.cursor.fetchone()

    def update(self, pk, **kwargs):
        params = ''
        for column, value in kwargs.items():
            params += f"{column}='{value}',"

        query = f"UPDATE {self.subject} set {params[0:-1]} WHERE id=%s;"
        self.cursor.execute(query, (int(pk),))
        self.connection.commit()

        return self.find(pk)

    def destroy(self, pk):
        record = self.find(pk)
        self.cursor.execute(f'DELETE FROM {self.subject} WHERE id=%s;', (int(pk),))
        self.connection.commit()
        return record

    def __del__(self):
        self.connection.close()
