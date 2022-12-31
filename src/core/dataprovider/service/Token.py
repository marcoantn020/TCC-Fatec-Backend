from abc import ABC
from abc import abstractmethod
from typing import Union


class Token(ABC):

    @abstractmethod
    def sign_jwt(self, id_logged: int, username: str, is_admin: Union[bool, int]):
        raise Exception("Method not implemented: signJWT")

    @abstractmethod
    def decode_jwt(self, value: str):
        raise Exception("Method not implemented: verify_access_token")
