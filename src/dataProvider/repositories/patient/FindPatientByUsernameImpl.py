from src.core.dataprovider.repository.patient.FindPatientByUsername import FindPatientByUsername
from src.dataProvider.config.DBConnection import connection
from src.dataProvider.config.query.FindBy import FindBy


class FindPatientByUsernameImpl(FindPatientByUsername):

    def find(self, username: str):
        query = FindBy.find(table="patient", column_name="username", value=username)
        result = connection.read_query(query)
        if not len(result):
            return result
        return result[0]
