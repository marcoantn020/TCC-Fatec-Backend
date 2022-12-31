from typing import Any


class FindLike:

    @staticmethod
    def find(table: str, column_name: str, value: Any):
        return f"SELECT * FROM {table} WHERE {column_name} LIKE '{value}%';"
