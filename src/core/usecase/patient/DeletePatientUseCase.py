from abc import ABC
from abc import abstractmethod
from typing import Any, Dict


class DeletePatientUseCase(ABC):

    @abstractmethod
    def execute(self, patient_id: int, is_admin: int) -> Dict[str, Any]:
        raise Exception("Method not implemented: execute")
