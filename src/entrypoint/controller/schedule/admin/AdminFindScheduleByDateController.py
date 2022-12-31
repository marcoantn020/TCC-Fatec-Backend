from src.dataProvider.repositories.schedule.FindScheduleTodayOrOtherDateImpl import FindScheduleTodayOrOtherDateImpl
from src.core.usecase.schedule.impl.admin.AdminFindScheduleByDateUseCaseImpl import AdminFindScheduleByDateUseCaseImpl
from src.entrypoint.schemas.schedule_schema import FindScheduleByDate


class AdminFindScheduleByDateController:

    @staticmethod
    def handle(input_data: FindScheduleByDate):
        find_schedule_today_or_other_date = FindScheduleTodayOrOtherDateImpl()
        find_schedule_by_date = AdminFindScheduleByDateUseCaseImpl(
            find_schedule_today_or_other_date=find_schedule_today_or_other_date
        )
        return find_schedule_by_date.execute(date=input_data.date_of_scheduling)
