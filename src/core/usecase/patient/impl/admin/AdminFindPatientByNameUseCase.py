from src.core.usecase.patient.FindPatientByNameUseCase import FindPatientByNameUseCase
from src.core.dataprovider.repository.patient.FindPatientByName import FindPatientByName
from src.core.usecase.DTO.PatientDto import PatientDto
from src.core.usecase.utils.HttpResponse import HttpResponse
from src.core.usecase.utils.MyCustomError import MyCustomError


class AdminFindPatientByNameUseCaseImpl(FindPatientByNameUseCase):

    __find_patient_by_name: FindPatientByName

    def __init__(self, find_patient_by_name: FindPatientByName):
        self.__find_patient_by_name = find_patient_by_name

    def execute(self, name: str) -> HttpResponse:
        response = self.__find_patient_by_name.find(name=name)
        if not response:
            raise MyCustomError(status_code=204)

        response = PatientDto.format(response)
        return HttpResponse(status_code=200, body=response)
