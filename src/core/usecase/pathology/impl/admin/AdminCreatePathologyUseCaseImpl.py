from datetime import datetime
from src.core.usecase.pathology.CreatePathologyUseCase import CreatePathologyUseCase
from src.core.usecase.utils import HttpResponse
from src.core.usecase.utils.MyCustomError import MyCustomError
from src.core.usecase.utils.Validations import Validations
from src.core.dataprovider.repository.pathology.CreatePathology import CreatePathology
from src.core.dataprovider.repository.pathology.UpdatePatientToActive import UpdatePatientToActive
from src.core.dataprovider.repository.pathology.FindByPathologyByPatientId import FindByPathologyByPatientId
from src.core.dataprovider.repository.patient.FindPatientById import FindPatientById
from src.core.domain.Pathology import Pathology


class AdminCreatePathologyUseCaseImpl(CreatePathologyUseCase):

    __create_pathology: CreatePathology
    __find_patient_by_id: FindPatientById
    __update_patient_to_active: UpdatePatientToActive
    __find_by_pathology_by_patient_id: FindByPathologyByPatientId

    def __init__(self,
                 create_pathology: CreatePathology,
                 find_patient_by_id: FindPatientById,
                 update_patient_to_active: UpdatePatientToActive,
                 find_by_pathology_by_patient_id: FindByPathologyByPatientId) -> None:
        self.__create_pathology = create_pathology
        self.__find_patient_by_id = find_patient_by_id
        self.__update_patient_to_active = update_patient_to_active
        self.__find_by_pathology_by_patient_id = find_by_pathology_by_patient_id

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
                ) -> HttpResponse:

        self.__check_patient_already_pathology_registrate(id_patient=id_patient)
        self.__validate_have_foot_surgery(have_foot_surgery=have_foot_surgery, which_foot=which_foot)

        date = datetime.now()
        pathology: Pathology = Pathology(
            id_patient=id_patient,
            has_diabetes=has_diabetes,
            observations_diabetes=observations_diabetes,
            have_hypertension=have_hypertension,
            observations_hypertension=observations_hypertension,
            take_medicines=take_medicines,
            observations_medicines=observations_medicines,
            allergic_to_medicine=allergic_to_medicine,
            which_medicine=which_medicine,
            have_cancer=have_cancer,
            which_type_cancer=which_type_cancer,
            has_pacemaker=has_pacemaker,
            has_pin=has_pin,
            is_cadiaco=is_cadiaco,
            have_foot_surgery=have_foot_surgery,
            which_foot=which_foot,
            about_the_foot_of_the_patient_has_callus=about_the_foot_of_the_patient_has_callus,
            about_the_foot_of_the_patient_has_callosity=about_the_foot_of_the_patient_has_callosity,
            about_the_foot_of_the_patient_has_fissure=about_the_foot_of_the_patient_has_fissure,
            about_the_foot_of_the_patient_has_dryness=about_the_foot_of_the_patient_has_dryness,
            about_the_foot_of_the_patient_has_psoriasis=about_the_foot_of_the_patient_has_psoriasis,
            about_the_foot_of_the_patient_has_pantar_wart=about_the_foot_of_the_patient_has_pantar_wart,
            about_the_nail_of_the_patient_has_onychocryptosis=about_the_nail_of_the_patient_has_onychocryptosis,
            about_the_nail_of_the_patient_has_onycholysis=about_the_nail_of_the_patient_has_onycholysis,
            about_the_nail_of_the_patient_has_onychomycosis=about_the_nail_of_the_patient_has_onychomycosis,
            about_the_nail_of_the_patient_has_onychophoresis=about_the_nail_of_the_patient_has_onychophoresis,
            sensitive_to_pain=sensitive_to_pain,
            type_of_sock=type_of_sock,
            type_of_shoe=type_of_shoe,
            shoe_number=shoe_number,
            created_at=date,
            updated_at=date
        )
        response = self.__create_pathology.create(pathology=pathology)
        if response:
            self.__update_patient_to_active.update(is_active=1, id_patient=id_patient)
        return HttpResponse(status_code=201, body={"id": response})

    @staticmethod
    def __validate_have_foot_surgery(have_foot_surgery: int, which_foot: str):
        if have_foot_surgery is True and which_foot is None:
            raise MyCustomError(message="O campo [which_foot] não pode ser nulo") \


    def __check_patient_already_pathology_registrate(self, id_patient: int):
        pathology = self.__find_by_pathology_by_patient_id.find(id_patient=id_patient)
        if len(pathology) > 0:
            raise MyCustomError(message="Esse paciente ja tem patologia cadastrada.")
