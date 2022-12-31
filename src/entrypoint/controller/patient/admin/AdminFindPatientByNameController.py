
from src.dataProvider.repositories.patient.FindPatientByNameImpl import FindPatientByNameImpl
from src.core.usecase.patient.impl.admin.AdminFindPatientByNameUseCase import AdminFindPatientByNameUseCaseImpl


class AdminFindPatientByNameController:

    @staticmethod
    def handle(name: str):
        find_patient_by_name = FindPatientByNameImpl()
        find_patient_by_name_use_case = AdminFindPatientByNameUseCaseImpl(find_patient_by_name=find_patient_by_name)
        return find_patient_by_name_use_case.execute(name=name)
