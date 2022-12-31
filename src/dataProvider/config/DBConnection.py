import mysql.connector
from mysql.connector import Error
from src.config.config import config

from src.core.usecase.utils.MyCustomError import MyCustomError


class DBConnection:
    _connect = None
    __access = {
        "host": config["database"]["HOST"],
        "username": config["database"]["USERNAME"],
        "password": config["database"]["PASSWORD"],
        "db": config["database"]["DB"]
    }

    def __init__(self) -> None:
        self._connect = mysql.connector.connect(**self.__access)

    def write_query(self, query: str):
        try:
            cursor = self._connect.cursor()
            cursor.execute(query)
            last_id = cursor.lastrowid
            self._connect.commit()
        except Error as err:
            print("\n")
            print(err)
            print("\n")
            raise MyCustomError(message="Server Error", status_code=500)
        else:
            return last_id

    def read_query(self, query: str):
        try:
            result = None
            cursor = self._connect.cursor(dictionary=True)
            cursor.execute(query)
            result = cursor.fetchall()
        except Error as err:
            print("\n")
            print(err)
            print("\n")
            raise MyCustomError(message="Server Error", status_code=500)
        else:
            return result


connection: DBConnection = DBConnection()
