from src.core.usecase.patient.FindPatientByNameUseCase import FindPatientByNameUseCase
from src.core.dataprovider.repository.patient.FindPatientByName import FindPatientByName
from src.core.usecase.DTO.PatientDto import PatientDto
from src.core.usecase.utils.MyCustomError import MyCustomError
from typing import Any, Dict


class AdminFindPatientByNameUseCaseImpl(FindPatientByNameUseCase):

    __find_patient_by_name: FindPatientByName

    def __init__(self, find_patient_by_name: FindPatientByName):
        self.__find_patient_by_name = find_patient_by_name

    def execute(self, name: str) -> Dict[str, Any]:
        response = self.__find_patient_by_name.find(name=name)
        if not response:
            raise MyCustomError(status_code=204)

        response = PatientDto.format(response)
        return response
