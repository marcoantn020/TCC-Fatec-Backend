import time
import jwt
from typing import Union
from src.core.dataprovider.service.Token import Token
from src.config.config import config


class JWTTokenGenerated(Token):

    def sign_jwt(self, id_logged: int, username: str, is_admin: Union[bool, int]):
        payload = {
            "id_logged": id_logged,
            "username": username,
            "is_admin": is_admin,
            "expiry": time.time() + 86400
        }
        token = jwt.encode(payload=payload, key=config["jwt"]["SECRET_KEY"], algorithm=config["jwt"]["ALGORITHM"])
        return token

    def decode_jwt(self, token: str):
        try:
            decode_token = jwt.decode(jwt=token, key=config["jwt"]["SECRET_KEY"], algorithms=[config["jwt"]["ALGORITHM"]])
            return decode_token if decode_token['expiry'] >= time.time() else None
        except:
            return {}
