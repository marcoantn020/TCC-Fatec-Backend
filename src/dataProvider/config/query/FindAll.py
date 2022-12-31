from typing import Any


class FindAll:

    @staticmethod
    def all(table: str, column_where: str = None, value: Any = None, limit: int = 10000, offset: int = 0, condition: str = "="):
        query = f"SELECT * FROM {table} "
        if column_where:
            query += f"WHERE {column_where} {condition} '{value}' "
        query += f"LIMIT {limit} OFFSET {offset};"
        return query
