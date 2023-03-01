from typing import Dict, Any

from src.core.usecase.login.LoginUsecase import LoginUseCase
from src.core.dataprovider.repository.patient.FindPatientByUsername import FindPatientByUsername
from src.core.dataprovider.service import Encrypter
from src.core.domain import Patient
from src.core.usecase.utils.MyCustomError import MyCustomError
from src.core.dataprovider.service.Token import Token
from src.core.usecase.DTO.LoginDto import LoginDto


class LoginUseCaseImpl(LoginUseCase):
    __token: Token
    __find_patient_by_username: FindPatientByUsername
    __encrypter: Encrypter

    def __init__(self, token: Token, get_patient_by_username: FindPatientByUsername, encrypter: Encrypter) -> None:
        self.__token = token
        self.__find_user_by_username = get_patient_by_username
        self.__encrypter = encrypter

    def execute(self, username: str, password: str) -> Dict[str, Any]:
        patient_exists: Patient = self.__find_user_by_username.find(username=username)
        if not patient_exists:
            raise MyCustomError(message="Usuário/Senha incorretos.")

        if not self.__encrypter.decrypter(password, patient_exists["password"]):
            raise MyCustomError(message="Usuário/Senha incorretos.")

        user = LoginDto.format(user=patient_exists)

        token__ = self.__token.sign_jwt(
            id_logged=user["id"], username=user['username'], is_admin=patient_exists["is_admin"])
        return {"access_token": token__, "user": user}
