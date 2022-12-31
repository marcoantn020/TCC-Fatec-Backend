from abc import ABC
from abc import abstractmethod
from src.core.usecase.utils.HttpResponse import HttpResponse


class LoginUseCase(ABC):

    @abstractmethod
    def execute(self, username: str, password: str) -> HttpResponse:
        raise Exception("Method not implemented: execute")
