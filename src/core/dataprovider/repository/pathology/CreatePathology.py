from abc import ABC
from abc import abstractmethod

from src.core.domain.Pathology import Pathology


class CreatePathology(ABC):

    @abstractmethod
    def create(self, pathology: Pathology) -> int:
        raise Exception("Method not implemented: create")
