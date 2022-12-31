from datetime import datetime
from datetime import timedelta
from src.core.usecase.utils.MyCustomError import MyCustomError


class DateFormat:

    @staticmethod
    def str_to_datetime(value: str) -> datetime:
        try:
            return datetime.strptime(value, '%d/%m/%Y')
        except MyCustomError:
            MyCustomError(message=f"Digite a data no formato 00/00/00.")

    @staticmethod
    def datetime_to_str(value: datetime):
        try:
            return value.strftime("%d/%m/%Y")
        except Exception:
            raise MyCustomError(message=f"Datetime invalido")

    @staticmethod
    def get_date_and_hour_current():
        return datetime.now() - timedelta(hours=3)

    @staticmethod
    def datetime_to_str_schedule(value: datetime):
        if not value:
            return None
        return value.strftime('%d/%m/%Y %H:%M:%S')

    @staticmethod
    def str_to_datetime_schedule(value: str):
        if not value:
            return None
        return datetime.strptime(value, '%d/%m/%Y %H:%M:%S')


