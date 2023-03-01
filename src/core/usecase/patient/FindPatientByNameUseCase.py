from abc import ABC
from abc import abstractmethod
from typing import Any, Dict


class FindPatientByNameUseCase(ABC):

    @abstractmethod
    def execute(self, name: str) -> Dict[str, Any]:
        raise Exception("Method not implemented: execute")
