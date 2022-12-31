from abc import ABC
from abc import abstractmethod


class UpdatePatientToActive(ABC):

    @abstractmethod
    def update(self, is_active: int, id_patient: int):
        raise Exception("Method not implemented: update")
