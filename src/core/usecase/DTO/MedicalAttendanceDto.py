from src.core.usecase.utils.DateFormat import DateFormat
from typing import Any


class MedicalAttendanceDto:

    @staticmethod
    def format(medical_attendance: Any):
        if isinstance(medical_attendance, dict):
            return {
                "patient": medical_attendance["first_name"]
            }
        else:
            new_array: list = []
            for i in range(len(medical_attendance)):
                new_array.append({
                    "date_of_scheduling": medical_attendance[i]["date_of_scheduling"],
                    "patient": medical_attendance[i]["first_name"]
                })
            return new_array

