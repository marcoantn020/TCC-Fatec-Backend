from src.dataProvider.repositories.patient.FindPatientByIdImpl import FindPatientByIdImpl
from src.core.usecase.patient.impl.FindPatientByIdUseCaseImpl import FindPatientByIdUseCaseImpl


class FindPatientByIdController:

    @staticmethod
    def handle(is_admin: int, id_patient: int):
        find_patient_by_id = FindPatientByIdImpl()
        find_patient_by_id_use_case = FindPatientByIdUseCaseImpl(find_patient_by_id=find_patient_by_id)
        return find_patient_by_id_use_case.execute(id_logged=id_patient, is_admin=is_admin)
