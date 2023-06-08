from src.core.usecase.utils.DateFormat import DateFormat
from typing import Any


class ScheduleDto:

    @staticmethod
    def format(schedule: Any):
        if isinstance(schedule, dict):
            return {
                "date_of_scheduling": DateFormat.datetime_to_str_schedule(value=schedule["date_of_scheduling"]),
                "patient": ScheduleDto.__check_name(schedule["first_name"])
            }
        else:
            new_array: list = []
            for i in range(len(schedule)):
                new_array.append({
                    "date_of_scheduling": DateFormat.datetime_to_str_schedule(value=schedule[i]["date_of_scheduling"]),
                    "patient": ScheduleDto.__check_name(schedule[i]["first_name"])
                })
            return new_array

    @staticmethod
    def __check_name(name: str):
        if not name:
            return ""
        return name
