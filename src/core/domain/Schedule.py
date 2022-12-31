from datetime import datetime
from typing import Union
from src.core.domain.util.ValidateFieldIsNone import ValidateFieldIsNone


class Schedule:
    __id: Union[int, None]
    __date_of_scheduling: datetime
    __date_unchecked: Union[None, datetime]
    __consultation_unchecked: int
    __consultation_completed: int
    __patient: int

    def __init__(self,
                 date_of_scheduling: datetime,
                 date_unchecked: Union[None, datetime],
                 consultation_unchecked: int,
                 consultation_completed: int,
                 id_patient: int) -> None:
        self.__id = None
        self.__date_of_scheduling = ValidateFieldIsNone.validate(
            field=date_of_scheduling, name_parameter="date_of_scheduling")
        self.__date_unchecked = date_unchecked
        self.__consultation_unchecked = ValidateFieldIsNone.validate(
            field=consultation_unchecked, name_parameter="consultation_unchecked")
        self.__patient = ValidateFieldIsNone.validate(
            field=id_patient, name_parameter="id_patient")
        self.__consultation_completed = ValidateFieldIsNone.validate(
            field=consultation_completed, name_parameter="consultation_completed")

    @property
    def id(self) -> int:
        return self.__id

    @property
    def date_of_scheduling(self) -> Union[None, datetime]:
        return self.__date_of_scheduling

    @property
    def date_unchecked(self) -> Union[None, datetime]:
        return self.__date_unchecked

    @property
    def consultation_completed(self) -> int:
        return self.__consultation_completed

    @property
    def consultation_unchecked(self) -> int:
        return self.__consultation_unchecked

    @property
    def patient(self) -> int:
        return self.__patient

    def json(self):
        return {
            "id": self.__id,
            "date_of_scheduling": self.__date_of_scheduling,
            "date_unchecked": self.__date_unchecked,
            "consultation_completed": self.__consultation_completed,
            "consultation_unchecked": self.__consultation_unchecked,
            "id_patient": self.__patient
        }
