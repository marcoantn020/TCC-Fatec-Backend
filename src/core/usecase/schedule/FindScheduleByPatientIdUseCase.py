from abc import ABC
from abc import abstractmethod
from typing import Any, Dict


class FindScheduleByPatientIdUseCase(ABC):
    @abstractmethod
    def execute(self, patient_id: int, finish: int) -> Dict[str, Any]:
        raise Exception("Method not implemented: execute")
