from datetime import datetime
from src.core.usecase.patient.UpdatePatientUseCase import UpdatePatientUseCase
from src.core.usecase.utils.HttpResponse import HttpResponse
from src.core.dataprovider.repository.patient.FindPatientByUsername import FindPatientByUsername
from src.core.dataprovider.repository.patient.UpdatePatient import UpdatePatient
from src.core.dataprovider.service.Encrypter import Encrypter
from src.core.domain.Patient import Patient
from src.core.usecase.utils.MyCustomError import MyCustomError
from src.core.usecase.utils.DateFormat import DateFormat
from src.core.usecase.utils.Validations import Validations


class AdminUpdatePatientUseCaseImpl(UpdatePatientUseCase):
    __find_patient_by_username: FindPatientByUsername
    __update_patient: UpdatePatient
    __encrypter: Encrypter

    def __init__(self,
                 find_user_by_username: FindPatientByUsername,
                 update_patient: UpdatePatient,
                 encrypter: Encrypter) -> None:
        self.__find_patient_by_username = find_user_by_username
        self.__update_patient = update_patient
        self.__encrypter = encrypter

    def execute(self,
                id_patient: int,
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
                what_activity: str,
                is_admin: int = None
                ) -> HttpResponse:

        Validations.user_is_admin(is_admin=is_admin)

        Validations.validate_length_parameters_str(parameters={
            "last_name": last_name, "first_name": first_name,
            "username": username, "password": password
        }, length=5)

        Validations.validate_genre(value=genre, name_variable="genre")

        if birth_date:
            birth_date = DateFormat.str_to_datetime(value=birth_date)

        password_hashed = self.__encrypter.encrypter(password)
        date = datetime.now()
        patient: Patient = self.__validate_if_the_patient_exists(username=username)
        update_patient: Patient = Patient(
            id_patient=id_patient,
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password_hashed,
            birth_date=birth_date,
            email=email,
            is_admin=0,
            is_active=patient["is_active"],
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

        self.__update_patient.update(patient=update_patient)

        return HttpResponse(status_code=202, body={"message": "success", "data": None})

    def __validate_if_the_patient_exists(self, username: str) -> Patient:
        patient_exists = self.__find_patient_by_username.find(username)
        if not patient_exists:
            raise MyCustomError(message="User not found", status_code=404)
        return patient_exists

    def __validate_password(self, password: str, password_confirmation: str, patient: Patient) -> str:
        if password:
            if password != password_confirmation:
                raise MyCustomError(message="password/password_confirmation não são iguais")
            return self.__encrypter.encrypter(password)
        return patient["password"]
