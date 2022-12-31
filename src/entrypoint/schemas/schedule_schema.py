
from pydantic import BaseModel
from pydantic import Field


class ScheduleInput(BaseModel):
    date_of_scheduling: str = Field("02/01/2023")
    hour_of_scheduling: str = Field("10:00:00")


class ScheduleOutput(BaseModel):
    schedule: str = Field("02/01/2023 10:00:00")


class DateOfScheduling(BaseModel):
    date_of_scheduling: str


class ScheduleInputCancel(BaseModel):
    date_of_scheduling: str = Field("02/01/2023")
    id_patient: int = Field("3")


class FindScheduleByDate(BaseModel):
    date_of_scheduling: str = Field("02/01/2023")


class ScheduleTodayOutput(BaseModel):
    date_of_scheduling: str = Field("02/01/2023 10:00:00")
    patient: str = Field("Ciclano")
