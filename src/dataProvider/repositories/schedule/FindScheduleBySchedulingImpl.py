from datetime import datetime
from src.core.dataprovider.repository.schedule.FindScheduleByScheduling import FindScheduleByScheduling
from src.dataProvider.config.query.FindBy import FindBy
from src.dataProvider.config.DBConnection import connection


class FindScheduleBySchedulingImpl(FindScheduleByScheduling):

    def find(self, date_of_scheduling: datetime):
        sql = FindBy.find(table="medical_consultation", column_name="date_of_scheduling", value=date_of_scheduling)
        return connection.read_query(sql)


