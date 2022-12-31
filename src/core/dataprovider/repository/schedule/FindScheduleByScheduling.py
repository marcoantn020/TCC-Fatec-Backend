from abc import ABC
from abc import abstractmethod
from datetime import datetime


class FindScheduleByScheduling(ABC):

    @abstractmethod
    def find(self, date_of_scheduling: datetime):
        raise Exception("Method not implemented: schedule")
