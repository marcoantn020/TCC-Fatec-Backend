from abc import ABC
from abc import abstractmethod
from typing import Any, Dict


class CreatePatientUseCase(ABC):

    @abstractmethod
    def execute(self,
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
                what_activity: str
                ) -> Dict[str, Any]:
        raise Exception("Method not implemented: execute")
