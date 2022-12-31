from abc import ABC
from abc import abstractmethod


class DeletePatient(ABC):

    @abstractmethod
    def delete(self, id_patient: int) -> None:
        raise Exception("Method not implemented: delete")
