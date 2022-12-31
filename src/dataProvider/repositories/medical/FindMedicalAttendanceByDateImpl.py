from src.core.dataprovider.repository.medical.FindMedicalAttendanceByDate import FindMedicalAttendanceByDate
from datetime import datetime
from src.dataProvider.config.DBConnection import connection
from src.dataProvider.config.query.FindBy import FindBy


class FindMedicalAttendanceByDateImpl(FindMedicalAttendanceByDate):

    def find(self, date_of_schedule: datetime):
        sql = FindBy.find(table="medical_consultation", column_name="date_of_scheduling", value=date_of_schedule)
        return connection.read_query(sql)
