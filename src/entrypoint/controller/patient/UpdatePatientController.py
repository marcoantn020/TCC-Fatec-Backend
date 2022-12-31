
from src.entrypoint.schemas.patient_schema import PatientInputUpdate
from src.dataProvider.repositories.patient.UpdatePatientImpl import UpdatePatientImpl
from src.dataProvider.repositories.patient.FindPatientByIdImpl import FindPatientByIdImpl
from src.dataProvider.service.EncrypterImpl import EncrypterImpl
from src.core.usecase.patient.impl.UpdatePatientUseCaseImpl import UpdatePatientUseCaseImpl


class UpdatePatientController:

    @staticmethod
    def handle(id_patient: int, input_data: PatientInputUpdate):
        update_patient = UpdatePatientImpl()
        find_patient_by_id = FindPatientByIdImpl()
        encrypter = EncrypterImpl()
        update_patient_use_case = UpdatePatientUseCaseImpl(
            find_patient_by_id=find_patient_by_id, update_patient=update_patient, encrypter=encrypter)
        return update_patient_use_case.execute(
            id_patient=id_patient,
            first_name=input_data.first_name,
            last_name=input_data.last_name,
            username=input_data.username,
            password=input_data.password,
            password_confirmation=input_data.password_confirmation,
            birth_date=input_data.birth_date,
            email=input_data.email,
            genre=input_data.genre,
            zipcode=input_data.zipcode,
            city=input_data.city,
            street=input_data.street,
            number=input_data.number,
            district=input_data.district,
            practice_activity=input_data.practice_activity,
            what_activity=input_data.what_activity
        )
