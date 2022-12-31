from abc import ABC
from abc import abstractmethod
from src.core.usecase.utils import HttpResponse


class FindScheduleByDateUseCase(ABC):

    @abstractmethod
    def execute(self, date: str) -> HttpResponse:
        raise Exception("Method not implemented: execute")
