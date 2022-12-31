from src.dataProvider.repositories.patient.FindPatientAllImpl import FindPatientAllImpl
from src.core.usecase.patient.impl.FindAllPatientUseCaseImpl import FindAllPatientUseCaseImpl


class AdminFindPatientAllController:

    @staticmethod
    def handle(limit: int, offset: int):
        find_all_patient = FindPatientAllImpl()
        find_all_patient_use_case = FindAllPatientUseCaseImpl(find_all_patient)
        return find_all_patient_use_case.execute(limit=limit, offset=offset)
