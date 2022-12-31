from abc import ABC
from abc import abstractmethod


class FindPatientByName(ABC):

    @abstractmethod
    def find(self, name: str):
        raise Exception("Method not implemented: find")
