from src.core.dataprovider.repository.schedule.SchedulePodiatristConsultation import SchedulePodiatristConsultation
from src.dataProvider.config.DBConnection import connection
from src.dataProvider.config.query.Create import Create
from src.core.domain.Schedule import Schedule


class SchedulePodiatristConsultationImpl(SchedulePodiatristConsultation):

    def schedule(self, schedule: Schedule):
        sql = Create.execute(class_object=schedule.json(), table="medical_consultation")
        return connection.write_query(sql)
