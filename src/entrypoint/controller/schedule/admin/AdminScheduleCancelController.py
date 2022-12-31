from src.core.usecase.schedule.impl.admin.AdminScheduleCanceledUseCaseImpl import AdminScheduleCanceledUseCaseImpl
from src.dataProvider.repositories.schedule.ScheduleCancelImpl import ScheduleCancelImpl
from src.dataProvider.repositories.patient.FindPatientByIdImpl import FindPatientByIdImpl
from src.entrypoint.schemas.schedule_schema import ScheduleInputCancel


class AdminScheduleCancelController:

    @staticmethod
    def handle(input_data: ScheduleInputCancel):
        schedule_cancel = ScheduleCancelImpl()
        find_patient_by_id = FindPatientByIdImpl()
        schedule_canceled_use_case = AdminScheduleCanceledUseCaseImpl(
            schedule_cancel=schedule_cancel, find_patient_by_id=find_patient_by_id)
        return schedule_canceled_use_case.execute(
            id_patient=input_data.id_patient,
            date=input_data.date_of_scheduling)
