from src.core.usecase.schedule.ScheduleCanceledUseCase import ScheduleCanceledUseCase
from src.core.dataprovider.repository.schedule.ScheduleCancel import ScheduleCancel
from src.core.dataprovider.repository.patient.FindPatientById import FindPatientById
from src.core.usecase.utils.MyCustomError import MyCustomError
from src.core.usecase.utils.DateFormat import DateFormat


class AdminScheduleCanceledUseCaseImpl(ScheduleCanceledUseCase):

    __schedule_cancel: ScheduleCancel
    __find_patient_by_id: FindPatientById

    def __init__(self, schedule_cancel: ScheduleCancel, find_patient_by_id: FindPatientById):
        self.__schedule_cancel = schedule_cancel
        self.__find_patient_by_id = find_patient_by_id

    def execute(self, id_patient: int,  date: str) -> None:
        self.__patient_exists(id_patient=id_patient)
        date_cancel = DateFormat.str_to_datetime_schedule(value=date)
        self.__schedule_cancel.cancel(
            id_patient=id_patient, date=date_cancel, date_cancel=DateFormat.get_date_and_hour_current())
        return None

    def __patient_exists(self, id_patient: int):
        patient = self.__find_patient_by_id.find(id_patient=id_patient)
        if len(patient) < 1:
            raise MyCustomError(message="paciente não encontrado.", status_code=404)
