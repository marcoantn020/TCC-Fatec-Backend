from typing import Any


class Create:

    @staticmethod
    def execute(class_object: Any, table: str):
        query = f"INSERT INTO {table} ("
        for key in class_object:
            if key and class_object[key] is not None:
                if key == 'id':
                    continue
                query += f"{key},"
        query = query[:-1]
        query += ') VALUES ('

        for key in class_object:
            if key and class_object[key] is not None:
                if key == 'id':
                    continue
                query += f"'{class_object[key]}',"

        query = query[:-1]
        query += ");"
        return query
