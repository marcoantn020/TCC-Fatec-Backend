from abc import ABC
from abc import abstractmethod
from datetime import datetime


class FindMedicalAttendanceByDate(ABC):

    @abstractmethod
    def find(self, date_of_schedule: datetime):
        raise Exception("Method not implemented: find")
