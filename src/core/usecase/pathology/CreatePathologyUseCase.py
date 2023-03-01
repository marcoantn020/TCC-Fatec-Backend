from abc import ABC
from abc import abstractmethod
from typing import Any, Dict


class CreatePathologyUseCase(ABC):

    @abstractmethod
    def execute(self,
                id_patient: int,
                has_diabetes: int,
                observations_diabetes: str,
                have_hypertension: int,
                observations_hypertension: str,
                take_medicines: int,
                observations_medicines: str,
                allergic_to_medicine: int,
                which_medicine: str,
                have_cancer: int,
                which_type_cancer: str,
                has_pacemaker: int,
                has_pin: int,
                is_cadiaco: int,
                have_foot_surgery: int,
                which_foot: str,
                about_the_foot_of_the_patient_has_callus: int,
                about_the_foot_of_the_patient_has_callosity: int,
                about_the_foot_of_the_patient_has_fissure: int,
                about_the_foot_of_the_patient_has_dryness: int,
                about_the_foot_of_the_patient_has_psoriasis: int,
                about_the_foot_of_the_patient_has_pantar_wart: int,
                about_the_nail_of_the_patient_has_onychocryptosis: int,
                about_the_nail_of_the_patient_has_onycholysis: int,
                about_the_nail_of_the_patient_has_onychomycosis: int,
                about_the_nail_of_the_patient_has_onychophoresis: int,
                sensitive_to_pain: str,
                type_of_sock: str,
                type_of_shoe: str,
                shoe_number: str
                ) -> Dict[str, Any]:
        raise Exception("Method not implemented: execute")
