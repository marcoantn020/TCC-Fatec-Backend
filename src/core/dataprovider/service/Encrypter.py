from abc import ABC
from abc import abstractmethod


class Encrypter(ABC):

    @abstractmethod
    def encrypter(self, value: str) -> str:
        raise Exception("Method not implemented: encrypter")

    @abstractmethod
    def decrypter(self, value: str, hash_value: str) -> bool:
        raise Exception("Method not implemented: decrypter")

