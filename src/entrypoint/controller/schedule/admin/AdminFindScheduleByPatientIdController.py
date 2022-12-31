from src.dataProvider.repositories.schedule.FindScheduleByPatientIdImpl import FindScheduleByPatientIdImpl
from src.core.usecase.schedule.impl.FindScheduleByPatientIdUseCaseImpl import FindScheduleByPatientIdUseCaseImpl


class AdminFindScheduleByPatientIdController:

    @staticmethod
    def handle(id_patient: int, finish: int):
        find_schedule_by_patient_id = FindScheduleByPatientIdImpl()
        find_schedule_by_patient_id_use_case = FindScheduleByPatientIdUseCaseImpl(
            find_schedule_by_patient_id=find_schedule_by_patient_id)
        return find_schedule_by_patient_id_use_case.execute(
            patient_id=id_patient,
            finish=finish
        )
