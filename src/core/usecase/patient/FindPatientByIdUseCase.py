from abc import ABC
from abc import abstractmethod
from typing import Any, Dict


class FindPatientByIdUseCase(ABC):

    @abstractmethod
    def execute(self, id_logged: int) -> Dict[str, Any]:
        raise Exception("Method not implemented: execute")
