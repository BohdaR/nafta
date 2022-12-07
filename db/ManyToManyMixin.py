from db.db import pluralizer


class ManyToManyMixin:
    def __get_join_query(self, pk, table_name, join_table):
        query = f'''
                SELECT DISTINCT {table_name}.*
                FROM {table_name}
                    INNER JOIN {join_table} join_table on {table_name}.id = join_table.{pluralizer.singular(table_name)}_id
                    INNER JOIN {self.subject} on join_table.{pluralizer.singular(self.subject)}_id = {self.subject}.id
                WHERE {self.subject}.id = %s
                '''
        return query

    def all_target_records(self, pk, target_table, join_table):
        query = f'{self.__get_join_query(pk, target_table, join_table)};'
        self.cursor.execute(query, (pk, ))
        return self.cursor.fetchall()

    def find_target_record(self, pk, target_table, join_table, target_record_id):
        query = f'{self.__get_join_query(pk, target_table, join_table)} AND {target_table}.id = %s;'
        self.cursor.execute(query, (pk, target_record_id))
        return self.cursor.fetchall()

    def add_target_record(self, pk, target_table, join_table, target_record_id):
        query = f'''
        INSERT INTO {join_table} ({pluralizer.singular(self.subject)}_id, {pluralizer.singular(target_table)}_id)
        VALUES (%s, %s) RETURNING {pluralizer.singular(self.subject)}_id, {pluralizer.singular(target_table)}_id
        '''

        self.cursor.execute(query, (pk, target_record_id))
        self.connection.commit()
        return self.cursor.fetchall()

    def remove_target_record(self, pk, target_table, join_table, target_record_id):
        record = self.find_target_record(pk, target_table, join_table, target_record_id)

        query = f'''
        DELETE FROM {join_table} 
        WHERE {join_table}.{pluralizer.singular(self.subject)}_id = %s
        AND {join_table}.{pluralizer.singular(target_table)}_id = %s;
        '''

        self.cursor.execute(query, (pk, target_record_id))
        self.connection.commit()

        return record
