from datetime import datetime

from src.core.usecase.patient.CreatePatientUseCase import CreatePatientUseCase
from src.core.dataprovider.repository.patient import CreatePatient
from src.core.dataprovider.repository.patient import FindPatientByUsername
from src.core.dataprovider.service import Encrypter
from src.core.usecase.utils import HttpResponse
from src.core.usecase.utils import MyCustomError
from src.core.usecase.utils import DateFormat
from src.core.usecase.utils import Validations

from src.core.domain import Patient


class CreatePatientUseCaseImpl(CreatePatientUseCase):
    __create_patient: CreatePatient
    __get_patient_by_username: FindPatientByUsername
    __encrypter: Encrypter

    def __init__(self,
                 create_patient: CreatePatient,
                 get_patient_by_username: FindPatientByUsername,
                 encrypter: Encrypter) -> None:
        self.__create_patient = create_patient
        self.__get_patient_by_username = get_patient_by_username
        self.__encrypter = encrypter

    def execute(self,
                first_name: str,
                last_name: str,
                username: str,
                password: str,
                password_confirmation: str,
                birth_date: str,
                email: str,
                genre: str,
                zipcode: str,
                city: str,
                street: str,
                number: str,
                district: str,
                practice_activity: int,
                what_activity: str
                ) -> HttpResponse:

        Validations.validate_name_length(name=first_name, name_variable="first_name", length=4)
        Validations.validate_name_length(name=last_name, name_variable="last_name", length=4)
        Validations.validate_name_length(name=username, name_variable="username", length=4)
        Validations.validate_name_length(name=password, name_variable="password", length=5)
        Validations.validate_name_length(name=zipcode, name_variable="zipcode", length=5)
        Validations.validate_genre(value=genre, name_variable="genre")
        birth = DateFormat.str_to_datetime(value=birth_date)
        self.__check_if_the_passwords_are_the_same(password, password_confirmation)
        self.__check_if_patient_already_exists(username=username)

        password_hashed = self.__encrypter.encrypter(password)
        date = datetime.now()

        patient: Patient = Patient(
            id_patient=None,
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password_hashed,
            birth_date=birth,
            email=email,
            is_admin=0,
            is_active=0,
            genre=genre,
            zipcode=zipcode,
            city=city,
            street=street,
            number=number,
            district=district,
            practice_activity=practice_activity,
            what_activity=what_activity,
            created_at=date,
            updated_at=date
        )

        response = self.__create_patient.create(patient=patient)
        return HttpResponse(status_code=201, body={"id": response})

    def __check_if_patient_already_exists(self, username: str):
        if self.__get_patient_by_username.find(username):
            raise MyCustomError(message="este paciente já existe")

    @staticmethod
    def __check_if_the_passwords_are_the_same(password: str, password_confirmation: str):
        if password != password_confirmation:
            raise MyCustomError(message="senhas nao sao as mesmas")
