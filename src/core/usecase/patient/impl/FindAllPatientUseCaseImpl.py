from src.core.usecase.patient.FindAllPatientUseCase import FindAllPatientUseCase
from src.core.dataprovider.repository.patient.FindPatient import FindPatient
from src.core.usecase.utils.HttpResponse import HttpResponse
from src.core.usecase.utils.MyCustomError import MyCustomError
from src.core.usecase.DTO.PatientDto import PatientDto


class FindAllPatientUseCaseImpl(FindAllPatientUseCase):
    __find_patients: FindPatient

    def __init__(self, find_patients: FindPatient) -> None:
        self.__find_patients = find_patients

    def execute(self, limit: int, offset: int) -> HttpResponse:
        limit = self.__verify_if_limit_is_none(limit)
        offset = self.__verify_if_offset_is_none(offset)
        response = self.__find_patients.all(limit=limit, offset=offset, condition="<>")
        if not response:
            raise MyCustomError(status_code=204)

        response = PatientDto.format(response)

        return HttpResponse(status_code=200, body=response)

    @staticmethod
    def __verify_if_limit_is_none(limit):
        if not limit:
            return 10
        return limit

    @staticmethod
    def __verify_if_offset_is_none(offset):
        if not offset:
            return 0

        if offset < 1:
            offset = 0
        return offset - 1
