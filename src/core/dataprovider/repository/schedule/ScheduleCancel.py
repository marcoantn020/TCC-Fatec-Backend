from abc import ABC
from abc import abstractmethod
from datetime import datetime


class ScheduleCancel(ABC):

    @abstractmethod
    def cancel(self, id_patient: int, date: datetime, date_cancel: datetime):
        raise Exception("Method not implemented: cancel")
