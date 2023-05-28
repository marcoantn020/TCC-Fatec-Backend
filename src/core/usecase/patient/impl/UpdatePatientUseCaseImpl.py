from datetime import datetime
from src.core.usecase.patient.UpdatePatientUseCase import UpdatePatientUseCase
from src.core.dataprovider.repository.patient.FindPatientById import FindPatientById
from src.core.dataprovider.repository.patient.UpdatePatient import UpdatePatient
from src.core.dataprovider.service.Encrypter import Encrypter
from src.core.domain.Patient import Patient
from src.core.usecase.utils.MyCustomError import MyCustomError
from src.core.usecase.utils.DateFormat import DateFormat
from src.core.usecase.utils.Validations import Validations
from typing import Union
from typing import Any, Dict


class UpdatePatientUseCaseImpl(UpdatePatientUseCase):
    __find_patient_by_id: FindPatientById
    __update_patient: UpdatePatient
    __encrypter: Encrypter

    def __init__(self,
                 find_patient_by_id: FindPatientById,
                 update_patient: UpdatePatient,
                 encrypter: Encrypter) -> None:
        self.__find_patient_by_id = find_patient_by_id
        self.__update_patient = update_patient
        self.__encrypter = encrypter

    def execute(self,
                id_patient: int,
                first_name: str,
                last_name: str,
                username: str,
                password: str,
                password_confirmation: str,
                birth_date: Union[str, None],
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
                ) -> Dict[str, Any]:

        Validations.validate_length_parameters_str(parameters={
            "last_name": last_name, "first_name": first_name,
            "username": username, "password": password
        }, length=5)

        if genre:
            Validations.validate_genre(value=genre, name_variable="genre")

        if birth_date:
            birth_date = DateFormat.str_to_datetime(value=birth_date)

        if password:
            password = self.__encrypter.encrypter(password)

        date = datetime.now()

        patient: Patient = self.__validate_if_the_patient_exists(id_patient=id_patient)
        self.__validate_password( password, password_confirmation, patient)


        update_patient: Patient = Patient(
            id_patient=id_patient,
            first_name=first_name if first_name else patient["first_name"],
            last_name=last_name if last_name else patient["last_name"],
            username=username if username else patient["username"],
            password=password if password else patient["password"],
            birth_date=birth_date if birth_date else patient["birth_date"],
            email=email,
            is_admin=0,
            is_active=0,
            genre=genre,
            zipcode=zipcode if zipcode else patient["zipcode"],
            city=city if city else patient["city"],
            street=street if street else patient["street"],
            number=number if number else patient["number"],
            district=district if district else patient["district"],
            practice_activity=practice_activity,
            what_activity=what_activity,
            created_at=patient["created_at"],
            updated_at=date
        )

        self.__update_patient.update(patient=update_patient)
        return {"message": "success", "data": None}

    def __validate_if_the_patient_exists(self, id_patient: int) -> Patient:
        patient_exists = self.__find_patient_by_id.find(id_patient=id_patient)
        if not patient_exists:
            raise MyCustomError(message="Paciente não encontrado", status_code=404)
        return patient_exists

    def __validate_password(self, password: str, password_confirmation: str, patient: Patient) -> str:
        if password:
            if password != password_confirmation:
                raise MyCustomError(message="password/passwordConfirmation não são iguais")
            return self.__encrypter.encrypter(password)
        return patient["password"]
