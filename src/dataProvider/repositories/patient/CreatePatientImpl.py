from src.core.dataprovider.repository.patient.CreatePatient import CreatePatient
from src.core.domain.Patient import Patient
from src.dataProvider.config.DBConnection import connection
from src.dataProvider.config.query.Create import Create


class CreatePatientImpl(CreatePatient):

    def create(self, patient: Patient) -> int:
        sql = Create.execute(class_object=patient.json(), table="patient")
        return connection.write_query(sql)
