from abc import ABC
from abc import abstractmethod
from src.core.usecase.utils import HttpResponse


class FindPatientByIdUseCase(ABC):

    @abstractmethod
    def execute(self, id_logged: int) -> HttpResponse:
        raise Exception("Method not implemented: execute")
