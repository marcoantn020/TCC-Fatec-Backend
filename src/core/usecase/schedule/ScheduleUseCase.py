from abc import ABC
from abc import abstractmethod
from typing import Any, Dict


class ScheduleUseCase(ABC):

    @abstractmethod
    def execute(self,
                patient_id: int,
                date_of_scheduling: str,
                hour_of_scheduling: str) -> Dict[str,Any]:
        raise Exception("Method not implemented: execute")
