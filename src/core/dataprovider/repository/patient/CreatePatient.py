from abc import ABC
from abc import abstractmethod

from src.core.domain import Patient


class CreatePatient(ABC):

    @abstractmethod
    def create(self, patient: Patient) -> int:
        raise Exception("Method not implemented: create")
