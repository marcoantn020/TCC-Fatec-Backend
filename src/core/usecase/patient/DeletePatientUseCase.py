from abc import ABC
from abc import abstractmethod
from src.core.usecase.utils import HttpResponse


class DeletePatientUseCase(ABC):

    @abstractmethod
    def execute(self, patient_id: int, is_admin: int) -> HttpResponse:
        raise Exception("Method not implemented: execute")
