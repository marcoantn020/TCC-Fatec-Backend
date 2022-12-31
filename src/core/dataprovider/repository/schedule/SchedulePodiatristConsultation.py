from abc import ABC
from abc import abstractmethod
from src.core.domain.Schedule import Schedule


class SchedulePodiatristConsultation(ABC):

    @abstractmethod
    def schedule(self, schedule: Schedule):
        raise Exception("Method not implemented: schedule")
