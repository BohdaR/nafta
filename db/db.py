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
                params += f"{column}=%s,"

            query = f"UPDATE {self.subject} set {params[0:-1]} WHERE id=%s;"
            self.__execute(query, (*kwargs.values(), int(pk)))
        return self.find(pk)

    def destroy(self, pk):
        record = self.find(pk)
        self.__execute(f'DELETE FROM {self.subject} WHERE id=%s;', (int(pk),))
        return record

    def __del__(self):
        self.connection.close()
