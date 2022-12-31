from src.core.dataprovider.repository.patient.UpdatePatient import UpdatePatient
from src.core.domain.Patient import Patient
from src.dataProvider.config.query.Update import Update
from src.dataProvider.config.DBConnection import connection


class UpdatePatientImpl(UpdatePatient):

    def update(self, patient: Patient):
        sql = Update.execute(class_object=patient.json(), table="patient", column_where="id_patient")
        return connection.write_query(sql)
