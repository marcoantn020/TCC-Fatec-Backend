from src.dataProvider.config.DBConnection import connection
from src.dataProvider.config.query.Update import Update
from src.core.dataprovider.repository.pathology.UpdatePatientToActive import UpdatePatientToActive


class UpdatePatientToActiveImpl(UpdatePatientToActive):

    def update(self, is_active: int, id_patient: int):
        sql = Update.one_column(
            table="patient", column="is_active", value_column=is_active, column_where="id_patient", value=id_patient)
        return connection.write_query(sql)
