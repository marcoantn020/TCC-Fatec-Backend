from src.core.dataprovider.repository.schedule.FindScheduleTodayOrOtherDate import FindScheduleTodayOrOtherDate
from datetime import datetime
from src.dataProvider.config.DBConnection import connection


class FindScheduleTodayOrOtherDateImpl(FindScheduleTodayOrOtherDate):

    def find(self, datetime_init: datetime, datetime_end: datetime):
        query = f"SELECT mc.date_of_scheduling, p.id_patient ,p.first_name FROM medical_consultation mc " \
                f"INNER JOIN patient p ON p.id_patient = mc.id_patient " \
                f"WHERE mc.date_of_scheduling BETWEEN '{datetime_init}' AND '{datetime_end}'"
        return connection.read_query(query)
