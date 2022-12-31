from src.core.dataprovider.repository.medical.CreateMedicalAttendance import CreateMedicalAttendance
from src.core.domain.MedicalAttendance import MedicalAttendance
from src.dataProvider.config.DBConnection import connection
from src.dataProvider.config.query.Update import Update
from datetime import datetime


class CreateMedicalAttendanceImpl(CreateMedicalAttendance):

    def create(self, medical_attendance: MedicalAttendance, date_of_schedule: datetime):
        sql = Update.execute(class_object=medical_attendance.json(),
                             table="medical_consultation",
                             column_where="date_of_scheduling",
                             value=date_of_schedule)
        return connection.write_query(sql)
