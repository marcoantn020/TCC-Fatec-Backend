from src.core.usecase.schedule.FindScheduleByPatientIdUseCase import FindScheduleByPatientIdUseCase
from src.core.dataprovider.repository.schedule.FindScheduleByPatientId import FindScheduleByPatientId
from src.core.usecase.utils.HttpResponse import HttpResponse
from src.core.usecase.utils.MyCustomError import MyCustomError
from src.core.usecase.DTO.ScheduleDto import ScheduleDto


class FindScheduleByPatientIdUseCaseImpl(FindScheduleByPatientIdUseCase):

    __find_schedule_by_patient_id: FindScheduleByPatientId

    def __init__(self, find_schedule_by_patient_id: FindScheduleByPatientId):
        self.__find_schedule_by_patient_id = find_schedule_by_patient_id

    def execute(self, patient_id: int, finish: int) -> HttpResponse:
        FindScheduleByPatientIdUseCaseImpl.__validate_finish(finsh=finish)
        schedule = self.__find_schedule_by_patient_id.find(id_patient=patient_id, finish=finish)
        schedule_dto = ScheduleDto.format(schedule=schedule)
        if schedule:
            return HttpResponse(status_code=200, body=schedule_dto)
        raise MyCustomError(message="Nada agendado.")

    @staticmethod
    def __validate_finish(finsh: int):
        finsh_valid = [0, 1]
        if finsh not in finsh_valid:
            raise MyCustomError(message="Infome 0 ou 1 no campo [finish]")
