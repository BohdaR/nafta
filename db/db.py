import re

import psycopg2
import psycopg2.extras
import os
from dotenv import load_dotenv
from flask import abort
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

    def __execute(self, query, params=None):
        try:
            self.cursor.execute(query, params)
        except psycopg2.Error as error:
            abort(400, description={'massage': f'Bad request. Please check your input data. Error - {error.pgcode}'})

        self.connection.commit()

    def __get_condition_template(self, conditions):
        params = []
        if len(conditions) != 0:
            for i in conditions:
                match i[1]:
                    case 'like':
                        params.append(f"{self.subject}.{i[0]} LIKE %s ESCAPE ''")
                    case 'greater':
                        params.append(f"{self.subject}.{i[0]} > %s")
                    case 'less':
                        params.append(f"{self.subject}.{i[0]} < %s")
                    case 'greater_or_equal':
                        params.append(f"{self.subject}.{i[0]} >= %s")
                    case 'less_or_equal':
                        params.append(f"{self.subject}.{i[0]} <= %s")
                    case 'not_equal':
                        params.append(f"{self.subject}.{i[0]} <> %s")
                    case _:
                        params.append(f"{self.subject}.{i[0]} = %s")
            query = f"WHERE {' AND '.join(params)}"
            return query

    def __get_join_query(self, columns, params):
        query = f'''
                SELECT {self.subject}.id,
                    {','.join(map(lambda i: f'{self.subject}.{i}', columns))},
                    {','.join(map(lambda i: f'{i[0][0]}.{i[0][1]} as {i[1]}', params.items()))}
                FROM {self.subject}
                {' '.join(map(lambda i: f'INNER JOIN {i[0][0]} on {i[0][0]}.id = {self.subject}.{pluralizer.singular(i[0][0])}_id', params.items()))}
                '''
        return query

    def join(self, columns, params, conditions=None):
        if conditions:
            query = f'{self.__get_join_query(columns, params)} {self.__get_condition_template(list(conditions.keys()))}'
            self.__execute(query, tuple(conditions.values()))
        else:
            self.__execute(self.__get_join_query(columns, params))
        return self.cursor.fetchall()

    def all(self):
        self.__execute(f'SELECT * FROM {self.subject} ORDER BY id')
        return self.cursor.fetchall()

    def find(self, pk):
        self.__execute(f'SELECT * FROM {self.subject} WHERE id=%s;', (int(pk),))
        return self.cursor.fetchall()

    def find_by(self, column, value):
        self.__execute(f"SELECT * FROM {self.subject} WHERE {column}=%s;", (value,))
        return self.cursor.fetchall()

    def filter(self, column, value):
        self.__execute(f"SELECT * FROM {self.subject} WHERE {column} LIKE %s ESCAPE ''", (value,))
        return self.cursor.fetchall()

    def create(self, data: dict):
        columns = ','.join(map(str, data.keys()))
        values = ','.join(map(lambda i: f"'{i}'", data.values()))
        query = f"INSERT INTO {self.subject} ({columns}) VALUES ({values}) RETURNING id, {columns};"

        self.__execute(query)
        return self.cursor.fetchone()

    def update(self, pk, **kwargs):
        if len(kwargs) > 0:
            params = ''
            for column, value in kwargs.items():
                params += f"{column}='{value}',"

            query = f"UPDATE {self.subject} set {params[0:-1]} WHERE id=%s;"
            self.__execute(query, (int(pk),))
        return self.find(pk)

    def destroy(self, pk):
        record = self.find(pk)
        self.__execute(f'DELETE FROM {self.subject} WHERE id=%s;', (int(pk),))
        return record

    def __del__(self):
        self.connection.close()
