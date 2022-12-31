from abc import ABC
from abc import abstractmethod
from src.core.usecase.utils import HttpResponse


class ScheduleUseCase(ABC):

    @abstractmethod
    def execute(self,
                patient_id: int,
                date_of_scheduling: str,
                hour_of_scheduling: str) -> HttpResponse:
        raise Exception("Method not implemented: execute")
