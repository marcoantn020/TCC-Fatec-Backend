from abc import ABC
from abc import abstractmethod
from src.core.domain.MedicalAttendance import MedicalAttendance
from datetime import datetime


class CreateMedicalAttendance(ABC):

    @abstractmethod
    def create(self, medical_attendance: MedicalAttendance, date_of_schedule: datetime):
        raise Exception("Method not implemented: create")
