from src.dataProvider.config.DBConnection import connection
from src.dataProvider.config.query.FindBy import FindBy
from src.core.dataprovider.repository.pathology.FindByPathologyByPatientId import FindByPathologyByPatientId


class FindByPathologyByPatientIdImpl(FindByPathologyByPatientId):

    def find(self, id_patient: int):
        sql = FindBy.find(table="pathology", column_name="id_patient", value=id_patient)
        return connection.read_query(sql)
