from src.entrypoint.schemas.schedule_schema import ScheduleInput
from src.core.usecase.schedule.impl.ScheduleUseCaseImpl import ScheduleUseCaseImpl
from src.dataProvider.repositories.schedule.SchedulePodiatristConsultationImpl import SchedulePodiatristConsultationImpl
from src.dataProvider.repositories.schedule.FindScheduleBySchedulingImpl import FindScheduleBySchedulingImpl


class ScheduleController:

    @staticmethod
    def handle(schedule: ScheduleInput, patient_id: int):
        find_schedule_by_scheduling = FindScheduleBySchedulingImpl()
        schedule_podiatrist_consultation = SchedulePodiatristConsultationImpl()
        schedule_use_case = ScheduleUseCaseImpl(
            schedule_podiatrist_consultation=schedule_podiatrist_consultation,
            find_schedule_by_scheduling=find_schedule_by_scheduling)
        return schedule_use_case.execute(
            patient_id=patient_id,
            date_of_scheduling=schedule.date_of_scheduling,
            hour_of_scheduling=schedule.hour_of_scheduling
        )
