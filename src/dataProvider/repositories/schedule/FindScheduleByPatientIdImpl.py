from src.core.dataprovider.repository.schedule.FindScheduleByPatientId import FindScheduleByPatientId
from src.dataProvider.config.query.FindBy import FindBy
from src.dataProvider.config.DBConnection import connection


class FindScheduleByPatientIdImpl(FindScheduleByPatientId):

    def find(self, id_patient: int, finish: int):
        query = f"select * from medical_consultation " \
                f"where id_patient = {id_patient} and consultation_completed = {finish};"
        return connection.read_query(query)
