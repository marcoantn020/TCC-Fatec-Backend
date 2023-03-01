from abc import ABC
from abc import abstractmethod
from typing import Any, Dict


class FindAllPatientUseCase(ABC):

    @abstractmethod
    def execute(self, limit: int, offset: int) -> Dict[str, Any]:
        raise Exception("Method not implemented: execute")
