from abc import ABC
from abc import abstractmethod


class ScheduleCanceledUseCase(ABC):

    @abstractmethod
    def execute(self, id_patient: int, date: str) -> None:
        raise Exception("Method not implemented: execute")
