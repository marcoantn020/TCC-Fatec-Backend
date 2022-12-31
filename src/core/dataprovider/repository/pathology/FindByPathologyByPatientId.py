from abc import ABC
from abc import abstractmethod


class FindByPathologyByPatientId(ABC):

    @abstractmethod
    def find(self, id_patient: int):
        raise Exception("Method not implemented: find")
