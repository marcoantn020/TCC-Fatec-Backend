from src.dataProvider.repositories.patient.CreatePatientImpl import CreatePatientImpl
from src.dataProvider.repositories.patient.FindPatientByUsernameImpl import FindPatientByUsernameImpl
from src.dataProvider.service.EncrypterImpl import EncrypterImpl
from src.core.usecase.patient.impl.CreatePatientUseCaseImpl import CreatePatientUseCaseImpl
from src.entrypoint.schemas.patient_schema import PatientInputCreate


class CreatePatientController:

    @staticmethod
    def handle(input_data: PatientInputCreate):
        create_patient = CreatePatientImpl()
        find_patient_by_username = FindPatientByUsernameImpl()
        encrypter = EncrypterImpl()
        create_patient_use_case = CreatePatientUseCaseImpl(create_patient, find_patient_by_username, encrypter)
        return create_patient_use_case.execute(
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
