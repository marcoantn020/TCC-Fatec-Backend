from abc import ABC
from abc import abstractmethod
from typing import Dict, Any


class LoginUseCase(ABC):

    @abstractmethod
    def execute(self, username: str, password: str) -> Dict[str, Any]:
        raise Exception("Method not implemented: execute")
