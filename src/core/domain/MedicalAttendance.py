from datetime import datetime
from typing import Union
from src.core.domain.util.ValidateFieldIsNone import ValidateFieldIsNone


class MedicalAttendance:
    __id_medical_consultation: Union[int, None]
    __id_patient: int
    __id_pathology: int
    __left_foot_professional_observation: str
    __right_foot_professional_observation: str
    __type_pressure_left_foot: str
    __type_pressure_right_foot: str
    __left_foot_mono_filament_test: str
    __right_foot_mono_filament_test: str
    __left_foot_dermatological_pathology: str
    __right_foot_dermatological_pathology: str
    __pathology_present_in_nail_left_foot: str
    __pathology_present_in_nail_right_foot: str
    __performed_procedure: str
    __consultation_completed: int
    __date_consultation_completed: datetime

    def __init__(self,
                 id_patient: int,
                 id_pathology: int,
                 left_foot_professional_observation: str,
                 right_foot_professional_observation: str,
                 type_pressure_left_foot: str,
                 type_pressure_right_foot: str,
                 left_foot_mono_filament_test: str,
                 right_foot_mono_filament_test: str,
                 left_foot_dermatological_pathology: str,
                 right_foot_dermatological_pathology: str,
                 pathology_present_in_nail_left_foot: str,
                 pathology_present_in_nail_right_foot: str,
                 performed_procedure: str,
                 consultation_completed: int,
                 date_consultation_completed: datetime) -> None:
        self.__id_medical_consultation = None
        self.__id_patient = ValidateFieldIsNone.validate(field=id_patient, name_parameter="id_patient")
        self.__id_pathology = ValidateFieldIsNone.validate(field=id_pathology, name_parameter="id_pathology")
        self.__left_foot_professional_observation = left_foot_professional_observation
        self.__right_foot_professional_observation = right_foot_professional_observation
        self.__type_pressure_left_foot = type_pressure_left_foot
        self.__type_pressure_right_foot = type_pressure_right_foot
        self.__left_foot_mono_filament_test = left_foot_mono_filament_test
        self.__right_foot_mono_filament_test = right_foot_mono_filament_test
        self.__left_foot_dermatological_pathology = left_foot_dermatological_pathology
        self.__right_foot_dermatological_pathology = right_foot_dermatological_pathology
        self.__pathology_present_in_nail_left_foot = pathology_present_in_nail_left_foot
        self.__pathology_present_in_nail_right_foot = pathology_present_in_nail_right_foot
        self.__performed_procedure = ValidateFieldIsNone.validate(field=performed_procedure, name_parameter="performed_procedure")
        self.__consultation_completed = ValidateFieldIsNone.validate(field=consultation_completed, name_parameter="consultation_completed")
        self.__date_consultation_completed = date_consultation_completed

    def id_medical_consultation(self) -> int:
        return self.__id_medical_consultation

    def id_patient(self) -> int:
        return self.__id_patient

    def id_pathology(self) -> int:
        return self.__id_pathology

    def left_foot_professional_observation(self) -> str:
        return self.__left_foot_professional_observation

    def right_foot_professional_observation(self) -> str:
        return self.__right_foot_professional_observation

    def type_pressure_left_foot(self) -> str:
        return self.__type_pressure_left_foot

    def type_pressure_right_foot(self) -> str:
        return self.__type_pressure_right_foot

    def left_foot_mono_filament_test(self) -> str:
        return self.__left_foot_mono_filament_test

    def right_foot_mono_filament_test(self) -> str:
        return self.__right_foot_mono_filament_test

    def left_foot_dermatological_pathology(self) -> str:
        return self.__left_foot_dermatological_pathology

    def right_foot_dermatological_pathology(self) -> str:
        return self.__right_foot_dermatological_pathology

    def pathology_present_in_nail_left_foot(self) -> str:
        return self.__pathology_present_in_nail_left_foot

    def pathology_present_in_nail_right_foot(self) -> str:
        return self.__pathology_present_in_nail_right_foot

    def performed_procedure(self) -> str:
        return self.__performed_procedure

    def consultation_completed(self) -> int:
        return self.__consultation_completed

    def date_consultation_completed(self) -> datetime:
        return self.__date_consultation_completed

    def json(self):
        return {
            "id": self.__id_medical_consultation,
            "id_patient": self.__id_patient,
            "id_pathology": self.__id_pathology,
            "left_foot_professional_observation": self.__left_foot_professional_observation,
            "right_foot_professional_observation": self.__right_foot_professional_observation,
            "type_pressure_left_foot": self.__type_pressure_left_foot,
            "type_pressure_right_foot": self.__type_pressure_right_foot,
            "left_foot_mono_filament_test": self.__left_foot_mono_filament_test,
            "right_foot_mono_filament_test": self.__right_foot_mono_filament_test,
            "left_foot_dermatological_pathology": self.__left_foot_dermatological_pathology,
            "right_foot_dermatological_pathology": self.__right_foot_dermatological_pathology,
            "pathology_present_in_nail_left_foot": self.__pathology_present_in_nail_left_foot,
            "pathology_present_in_nail_right_foot": self.__pathology_present_in_nail_right_foot,
            "performed_procedure": self.__performed_procedure,
            "consultation_completed": self.__consultation_completed,
            "date_consultation_completed": self.__date_consultation_completed
        }
