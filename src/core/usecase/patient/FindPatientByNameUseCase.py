from abc import ABC
from abc import abstractmethod
from src.core.usecase.utils import HttpResponse


class FindPatientByNameUseCase(ABC):

    @abstractmethod
    def execute(self, name: str) -> HttpResponse:
        raise Exception("Method not implemented: execute")
