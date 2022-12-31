from src.dataProvider.repositories.patient.FindPatientByIdImpl import FindPatientByIdImpl
from src.core.usecase.patient.impl.admin.AdminFindPatientByIdIUseCaseImpl import AdminFindPatientByIdIUseCaseImpl


class AdminFindPatientByIdController:

    @staticmethod
    def handle(id_patient: int):
        find_patient_by_id = FindPatientByIdImpl()
        find_patient_by_id_use_case = AdminFindPatientByIdIUseCaseImpl(find_patient_by_id=find_patient_by_id)
        return find_patient_by_id_use_case.execute(id_patient=id_patient)
