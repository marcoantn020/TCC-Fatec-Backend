
from datetime import datetime
from src.core.usecase.utils import MyCustomError
from typing import Dict


class Validations:

    @staticmethod
    def user_is_admin(is_admin: int):
        if is_admin != 1:
            raise MyCustomError(message="Você não é um administrador.", status_code=401)

    @staticmethod
    def validate_name_length(name: str, name_variable: str = "name", length: int = 3):
        if not name:
            raise MyCustomError(message=f"{name_variable} deve ser pelo menos {length} characteres.")
        if len(name) < length:
            raise MyCustomError(message=f"{name_variable} deve ser pelo menos {length} characteres.")

    @staticmethod
    def validate_password_length(password: str):
        if not password:
            raise MyCustomError(message=f"password deve ser pelo menos 5 characteres.")
        if len(password) < 5:
            raise MyCustomError(message=f"password deve ser pelo menos 5 characteres.")

    @staticmethod
    def is_datetime(date: any, name_variable: str):
        if not isinstance(date, datetime):
            raise MyCustomError(message=f"passar um datetime válido em [{name_variable}]")

    @staticmethod
    def validate_genre(value: str, name_variable: str):
        if not value or len(value) != 1:
            raise MyCustomError(message=f"Esperando apenas um caractere no campo [{name_variable}]")

        if value not in ['F', 'M', 'f', 'm']:
            raise MyCustomError(message=f"Esperando [M] ou [F] no campo [{name_variable}]")

    @staticmethod
    def validate_length_parameters_str(parameters: Dict[str, str], length: int):
        for field in parameters:
            if field and len(field) < length:
                Validations.validate_name_length(name=parameters[field], name_variable=field, length=length)
