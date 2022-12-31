from src.dataProvider.config.DBConnection import connection
from src.dataProvider.config.query.Create import Create
from src.core.domain.Pathology import Pathology
from src.core.dataprovider.repository.pathology.CreatePathology import CreatePathology


class CreatePathologyImpl(CreatePathology):

    def create(self, pathology: Pathology) -> int:
        sql = Create.execute(class_object=pathology.json(), table="pathology")
        return connection.write_query(sql)
