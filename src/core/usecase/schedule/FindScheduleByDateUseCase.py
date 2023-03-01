from abc import ABC
from abc import abstractmethod
from typing import Any, Dict


class FindScheduleByDateUseCase(ABC):

    @abstractmethod
    def execute(self, date: str) -> Dict[str, Any]:
        raise Exception("Method not implemented: execute")
