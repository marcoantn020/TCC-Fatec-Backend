import bcrypt
from src.core.dataprovider.service import Encrypter


class EncrypterImpl(Encrypter):

    def encrypter(self, value: str) -> str:
        return bcrypt.hashpw(value.encode('utf8'), bcrypt.gensalt(8)).decode("utf8")

    def decrypter(self, value: str, hash_value: str) -> bool:
        return bcrypt.checkpw(value.encode('utf8'), hash_value.encode("utf8"))



