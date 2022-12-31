from abc import ABC
from abc import abstractmethod
from typing import Union


class FindPatient(ABC):

    @abstractmethod
    def all(self, limit: int, offset: int, condition: Union[None, str]):
        raise Exception("Method not implemented: all")
