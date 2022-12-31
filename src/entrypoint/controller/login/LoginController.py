from src.entrypoint.schemas.login_schema import LoginInput
from src.dataProvider.repositories.patient.FindPatientByUsernameImpl import FindPatientByUsernameImpl
from src.dataProvider.service.JWTTokenGenerated import JWTTokenGenerated
from src.dataProvider.service.EncrypterImpl import EncrypterImpl
from src.core.usecase.login.impl.LoginUseCaseImpl import LoginUseCaseImpl


class LoginController:

    @staticmethod
    def handle(input_data: LoginInput):
        find_user_by_username = FindPatientByUsernameImpl()
        token = JWTTokenGenerated()
        encrypter = EncrypterImpl()
        login = LoginUseCaseImpl(token=token, get_patient_by_username=find_user_by_username, encrypter=encrypter)
        return login.execute(
            username=input_data.username,
            password=input_data.password
        )
