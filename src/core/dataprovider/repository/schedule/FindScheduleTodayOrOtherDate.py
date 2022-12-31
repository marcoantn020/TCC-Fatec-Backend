from abc import ABC
from abc import abstractmethod
from datetime import datetime


class FindScheduleTodayOrOtherDate(ABC):

    @abstractmethod
    def find(self, datetime_init: datetime, datetime_end: datetime):
        raise Exception("Method not implemented: find")
