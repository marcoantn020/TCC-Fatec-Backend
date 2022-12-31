from abc import ABC
from abc import abstractmethod
from src.core.usecase.utils import HttpResponse


class FindAllPatientUseCase(ABC):

    @abstractmethod
    def execute(self, limit: int, offset: int) -> HttpResponse:
        raise Exception("Method not implemented: execute")
