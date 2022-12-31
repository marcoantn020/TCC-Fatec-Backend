from src.core.dataprovider.repository.patient.FindPatientById import FindPatientById
from src.dataProvider.config.DBConnection import connection
from src.dataProvider.config.query.FindBy import FindBy


class FindPatientByIdImpl(FindPatientById):

    def find(self, id_patient: int):
        query = FindBy.find(table="patient", column_name="id_patient", value=id_patient)
        result = connection.read_query(query)
        if not len(result):
            return result
        return result[0]
