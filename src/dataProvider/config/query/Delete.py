from typing import Any


class Delete:

    @staticmethod
    def execute(table: str, column_name: str, value: Any):
        return f"DELETE FROM {table} WHERE {column_name} = {value};"
