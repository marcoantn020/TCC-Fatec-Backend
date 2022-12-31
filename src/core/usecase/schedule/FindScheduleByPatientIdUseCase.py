from abc import ABC
from abc import abstractmethod
from src.core.usecase.utils import HttpResponse


class FindScheduleByPatientIdUseCase(ABC):
    @abstractmethod
    def execute(self, patient_id: int, finish: int) -> HttpResponse:
        raise Exception("Method not implemented: execute")
