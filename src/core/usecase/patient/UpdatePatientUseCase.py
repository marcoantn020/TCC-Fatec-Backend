from abc import ABC
from typing import Union
from abc import abstractmethod
from src.core.usecase.utils import HttpResponse


class UpdatePatientUseCase(ABC):

    @abstractmethod
    def execute(self,
                patient_id: int,
                first_name: str,
                last_name: str,
                username: str,
                password: str,
                password_confirmation: str,
                birth_date: str,
                email: str,
                genre: str,
                zipcode: str,
                city: str,
                street: str,
                number: str,
                district: str,
                practice_activity: int,
                what_activity: str,
                is_admin: int = None
                ) -> HttpResponse:
        raise Exception("Method not implemented: execute")
