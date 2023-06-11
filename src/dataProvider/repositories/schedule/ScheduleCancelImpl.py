from src.core.dataprovider.repository.schedule.ScheduleCancel import ScheduleCancel
from datetime import datetime
from src.dataProvider.config.DBConnection import connection


class ScheduleCancelImpl(ScheduleCancel):

    def cancel(self, id_patient: int, date: datetime, date_cancel: datetime):
        query = f"UPDATE medical_consultation SET  consultation_unchecked = 1, date_unchecked = '{date_cancel}' " \
                f"WHERE date_of_scheduling LIKE '{date}' AND id_patient = '{id_patient}';"
        print(query)
        return connection.write_query(query)
