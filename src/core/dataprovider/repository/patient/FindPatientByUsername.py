from abc import ABC
from abc import abstractmethod


class FindPatientByUsername(ABC):

    @abstractmethod
    def find(self, username: str):
        raise Exception("Method not implemented: find")
