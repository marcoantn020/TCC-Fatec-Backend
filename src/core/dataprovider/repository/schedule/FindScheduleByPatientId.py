from abc import ABC
from abc import abstractmethod


class FindScheduleByPatientId(ABC):

    @abstractmethod
    def find(self, id_patient: int, finish: int):
        raise Exception("Method not implemented: find")
