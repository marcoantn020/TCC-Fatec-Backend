from src.core.dataprovider.repository.patient.FindPatient import FindPatient
from src.dataProvider.config.DBConnection import connection
from src.dataProvider.config.query.FindAll import FindAll
from typing import Union


class FindPatientAllImpl(FindPatient):

    def all(self, limit: int, offset: int, condition: Union[None, str]):
        query = ''
        if limit and offset:
            query += FindAll.all(table="patient", limit=limit, offset=offset, column_where="is_admin", value=1, condition=condition)
        else:
            query += FindAll.all(table="patient", column_where="is_admin", value=1, condition=condition)
        return connection.read_query(query)
