from typing import Any


class Update:

    @staticmethod
    def execute(class_object: Any, table: str, column_where: str, value: Any = None):
        query = f'UPDATE {table} SET '
        for key in class_object:
            if key and class_object[key]:
                if key == 'id':
                    continue
                query += f"{key}='{class_object[key]}',"
        query = query[:-1]
        if value:
            query += f" WHERE {column_where} = '{value}';"
        else:
            query += f" WHERE {column_where} = {class_object['id']};"
        return query

    @staticmethod
    def one_column(table: str, column: str, value_column: Any, column_where: str, value: Any = None):
        return f"UPDATE {table} SET {column}='{value_column}' WHERE {column_where}='{value}'"
