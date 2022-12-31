from abc import ABC
from abc import abstractmethod

from src.core.domain.Patient import Patient


class UpdatePatient(ABC):

    @abstractmethod
    def update(self, patient: Patient) -> int:
        raise Exception("Method not implemented: update")
