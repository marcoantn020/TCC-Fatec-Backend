from src.core.usecase.schedule.ScheduleUseCase import ScheduleUseCase
from src.core.dataprovider.repository.schedule.SchedulePodiatristConsultation import SchedulePodiatristConsultation
from src.core.dataprovider.repository.schedule.FindScheduleByScheduling import FindScheduleByScheduling
from src.core.domain.Schedule import Schedule
from src.core.usecase.utils.MyCustomError import MyCustomError
from src.core.usecase.utils.DateFormat import DateFormat
from datetime import datetime
from typing import Any, Dict


class ScheduleUseCaseImpl(ScheduleUseCase):

    __schedule_podiatrist_consultation: SchedulePodiatristConsultation
    __find_schedule_by_scheduling: FindScheduleByScheduling

    def __init__(self,
                 schedule_podiatrist_consultation: SchedulePodiatristConsultation,
                 find_schedule_by_scheduling: FindScheduleByScheduling) -> None:
        self.__schedule_podiatrist_consultation = schedule_podiatrist_consultation
        self.__find_schedule_by_scheduling = find_schedule_by_scheduling

    def execute(self, patient_id: int, date_of_scheduling: str, hour_of_scheduling: str) -> Dict[str, Any]:
        self.__validate_str_date(str_date=date_of_scheduling)
        self.__validate_str_hour(str_hour=hour_of_scheduling)

        date_input = self.__transform_input_str_in_datetime(
            date_of_scheduling=date_of_scheduling, hour_of_scheduling=hour_of_scheduling)

        self.__verify_date(date_of_scheduling=date_input)

        day_current = self.__get_day_current(date_input)
        self.__day_block(day_week=day_current)

        self.__valid_date_hour_to_schedule(date_input=date_input)
        self.__valida_hour(date_input)

        schedule: Schedule = Schedule(
            id_patient=patient_id,
            date_of_scheduling=date_input,
            date_unchecked=None,
            consultation_unchecked=0,
            consultation_completed=0
        )

        self.__schedule_podiatrist_consultation.schedule(schedule=schedule)

        return {"schedule": DateFormat.datetime_to_str_schedule(value=date_input)}

    def __verify_date(self, date_of_scheduling: datetime):
        schedule = self.__find_schedule_by_scheduling.find(date_of_scheduling=date_of_scheduling)
        if schedule:
            raise MyCustomError(message="esta data não está disponível.")

    @staticmethod
    def __valid_date_hour_to_schedule(date_input: datetime):
        timestamp_input = datetime.timestamp(date_input)
        now = DateFormat.get_date_and_hour_current()
        timestamp_current = datetime.timestamp(now)
        if timestamp_current > timestamp_input:
            raise MyCustomError(message=f"data e hora devem ser maiores que as atuais para agendamento.")

    @staticmethod
    def __valida_hour(date: datetime):
        hour_input = date.strftime("%H")
        ScheduleUseCaseImpl.__valid_hour_of_attendance(hour_input=hour_input)

    @staticmethod
    def __valid_hour_of_attendance(hour_input: str):
        hour_attendance = [8, 9, 10, 11, 12, 14, 15, 16, 17]
        if int(hour_input) not in hour_attendance:
            raise MyCustomError(message="Não atendemos no horário informado.")

    @staticmethod
    def __day_block(day_week: str):
        day_week_block = ['saturday', 'sunday']
        day_translate = {
            "Sunday": "Domingo",
            "Saturday": "Sabado",
        }
        if day_week in day_week_block:
            raise MyCustomError(message=f"nós não atendemos ao(s) {day_translate[day_week]}")

    @staticmethod
    def __get_day_current(date: datetime):
        return date.strftime("%A")

    @staticmethod
    def __transform_input_str_in_datetime(date_of_scheduling: str, hour_of_scheduling: str):
        datetime_str = date_of_scheduling + " " + hour_of_scheduling
        datetime_object = datetime.strptime(datetime_str, '%d/%m/%Y %H:%M:%S')
        return datetime_object

    @staticmethod
    def __validate_str_hour(str_hour: Any):
        if not isinstance(str_hour, str):
            raise MyCustomError(message="formato inválido, informe dessa maneira: HH:MM")

        date = str_hour.split(":")
        if date[1] != "00" or date[2] != "00":
            raise MyCustomError(message="digite apenas horas inteiras exemplo: 10:00")

        if len(date) != 3:
            raise MyCustomError(message="formato inválido, informe dessa maneira: HH:MM")

    @staticmethod
    def __validate_str_date(str_date: Any):
        if not isinstance(str_date, str):
            raise MyCustomError(message="formato inválido, informe dessa maneira: dd/mm/yyyy")

        date = str_date.split("/")
        if len(date) != 3:
            raise MyCustomError(message="formato inválido, informe dessa maneira: dd/mm/yyyy")
