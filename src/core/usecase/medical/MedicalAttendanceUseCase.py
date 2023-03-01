from abc import ABC
from abc import abstractmethod
from typing import Any, Dict


class MedicalAttendanceUseCase(ABC):

    @abstractmethod
    def execute(self,
                id_patient: int,
                left_foot_professional_observation: str,
                right_foot_professional_observation: str,
                type_pressure_left_foot: str,
                type_pressure_right_foot: str,
                left_foot_mono_filament_test: str,
                right_foot_mono_filament_test: str,
                left_foot_dermatological_pathology: str,
                right_foot_dermatological_pathology: str,
                pathology_present_in_nail_left_foot: str,
                pathology_present_in_nail_right_foot: str,
                performed_procedure: str,
                date_of_schedule: str) -> Dict[str, Any]:
        raise Exception("method not implemented: execute")
