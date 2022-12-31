from abc import ABC
from abc import abstractmethod
from src.core.usecase.utils import HttpResponse


class ScheduleCanceledUseCase(ABC):

    @abstractmethod
    def execute(self, id_patient: int, date: str) -> HttpResponse:
        raise Exception("Method not implemented: execute")
