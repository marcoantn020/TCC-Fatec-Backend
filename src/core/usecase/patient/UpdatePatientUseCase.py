from abc import ABC
from typing import Any, Dict
from abc import abstractmethod

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
                ) -> Dict[str, Any]:
        raise Exception("Method not implemented: execute")
