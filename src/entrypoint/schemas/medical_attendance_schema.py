from pydantic import BaseModel
from pydantic import Field


class InputMedicalAttendance(BaseModel):
    id_patient: int = Field("25")
    left_foot_professional_observation: str = Field("nada acrescentar")
    right_foot_professional_observation: str = Field("nada acrescentar")
    type_pressure_left_foot: str = Field("32")
    type_pressure_right_foot: str = Field("36")
    left_foot_mono_filament_test: str = Field("15")
    right_foot_mono_filament_test: str = Field("15")
    left_foot_dermatological_pathology: str = Field("unha encravada")
    right_foot_dermatological_pathology: str = Field("nada acrescentar")
    pathology_present_in_nail_left_foot: str = Field("nada acrescentar")
    pathology_present_in_nail_right_foot: str = Field("nada acrescentar")
    performed_procedure: str = Field("Aqui é descrito que tipo de atendimento foi realizado")
    date_of_scheduling: str = Field("02/01/2023 10:00:00")


class OutputMedicalAttendance(BaseModel):
    attendance: str = Field("Atendimento do paciente Fulano realizado.")
