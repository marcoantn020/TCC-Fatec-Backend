from src.core.usecase.patient.FindPatientByIdUseCase import FindPatientByIdUseCase
from src.core.dataprovider.repository.patient.FindPatientById import FindPatientById
from src.core.usecase.utils.HttpResponse import HttpResponse
from src.core.usecase.utils.MyCustomError import MyCustomError
from src.core.usecase.DTO.PatientDto import PatientDto


class FindPatientByIdUseCaseImpl(FindPatientByIdUseCase):
    __find_patient_by_id: FindPatientById

    def __init__(self, find_patient_by_id: FindPatientById) -> None:
        self.__find_patient_by_id = find_patient_by_id

    def execute(self, id_logged: int) -> HttpResponse:
        response = self.__find_patient_by_id.find(id_patient=id_logged)
        if not response:
            raise MyCustomError(status_code=204)

        response = PatientDto.format(response)

        return HttpResponse(status_code=200, body=response)
