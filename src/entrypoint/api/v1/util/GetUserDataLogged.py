from src.dataProvider.service.JWTBearer import JWTBearer
from fastapi import Request


class GetUserDataLogged:

    @staticmethod
    def get_username(request: Request) -> str:
        username_user_logged = JWTBearer().get_id_user_logged(request)
        return username_user_logged["username"]

    @staticmethod
    def get_id(request: Request) -> int:
        id_logged = JWTBearer().get_id_user_logged(request)
        return id_logged["id_logged"]

    @staticmethod
    def get_user_is_admin(request: Request) -> int:
        username_user_logged = JWTBearer().get_id_user_logged(request)
        return username_user_logged["is_admin"]
