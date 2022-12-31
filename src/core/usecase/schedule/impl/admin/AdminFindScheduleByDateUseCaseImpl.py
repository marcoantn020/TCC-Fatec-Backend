from src.core.usecase.schedule.FindScheduleByDateUseCase import FindScheduleByDateUseCase
from src.core.usecase.utils.HttpResponse import HttpResponse
from src.core.usecase.utils.MyCustomError import MyCustomError
from src.core.dataprovider.repository.schedule.FindScheduleTodayOrOtherDate import FindScheduleTodayOrOtherDate
from datetime import datetime
from src.core.usecase.DTO.ScheduleDto import ScheduleDto


class AdminFindScheduleByDateUseCaseImpl(FindScheduleByDateUseCase):

    __find_schedule_today_or_other_date: FindScheduleTodayOrOtherDate

    def __init__(self, find_schedule_today_or_other_date: FindScheduleTodayOrOtherDate):
        self.__find_schedule_today_or_other_date = find_schedule_today_or_other_date

    def execute(self, date: str) -> HttpResponse:
        date_init, date_end = self.__str_to_datetime(value=date)
        result = self.__find_schedule_today_or_other_date.find(
            datetime_init=date_init, datetime_end=date_end)
        if len(result) < 1:
            raise MyCustomError(message="Nada agendado ate o momento", status_code=404)
        date_dto = ScheduleDto.format(result)
        return HttpResponse(status_code=200, body=date_dto)

    @staticmethod
    def __str_to_datetime(value: str):
        try:
            date_init = datetime.strptime(value, '%d/%m/%Y')
            value_time = value + " 23:00:00"
            date_end = datetime.strptime(value_time, '%d/%m/%Y  %H:%M:%S')
            return date_init, date_end
        except MyCustomError:
            MyCustomError(message=f"Digite a data no formato 00/00/00.")
