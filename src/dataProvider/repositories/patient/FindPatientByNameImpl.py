from src.core.dataprovider.repository.patient.FindPatientByName import FindPatientByName
from src.dataProvider.config.DBConnection import connection
from src.dataProvider.config.query.FindLike import FindLike


class FindPatientByNameImpl(FindPatientByName):

    def find(self, name: str):
        query = FindLike.find(table="patient", column_name="first_name", value=name)
        result = connection.read_query(query)
        if not len(result):
            return result
        return result[0]
