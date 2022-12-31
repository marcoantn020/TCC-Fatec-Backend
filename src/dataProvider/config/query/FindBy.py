from typing import Any


class FindBy:

    @staticmethod
    def find(table: str, column_name: str, value: Any):
        return f"SELECT * FROM {table} WHERE {column_name} = '{value}';"
