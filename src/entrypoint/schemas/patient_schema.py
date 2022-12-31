from typing import Union
from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class PatientInputCreate(BaseModel):
    first_name: str = Field("Fulano")
    last_name: str = Field("da Silva")
    username: str = Field("fulano")
    password: str = Field("123456")
    password_confirmation: str = Field("123456")
    birth_date: str = Field("03/10/1995")
    email: str = Field("email@email.com")
    genre: str = Field("M")
    zipcode: str = Field("17000-012")
    city: str = Field("Vera Cruz")
    street: str = Field("Rua dos bobos")
    number: str = Field("125")
    district: str = Field("centro")
    practice_activity: int = Field("1")
    what_activity: str = Field("Futebol")


class PatientInputUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    username: Optional[str]
    password: Optional[str]
    password_confirmation: Optional[str]
    birth_date: Optional[str]
    email: Optional[str]
    genre: Optional[str]
    zipcode: Optional[str]
    city: Optional[str]
    street: Optional[str]
    number: Optional[str]
    district: Optional[str]
    practice_activity: Optional[Union[int, bool]]
    what_activity: Optional[str]


class PatientCreated(BaseModel):
    id: int = Field("150")


class PatientOutput(BaseModel):
    id: Optional[int]
    name: Optional[str]
    last_name: Optional[str]
    username: Optional[str]
    birth_date: Optional[str]
    email: Optional[str]
    genre: Optional[str]
    zipcode: Optional[str]
    city: Optional[str]
    street: Optional[str]
    number: Optional[str]
    district: Optional[str]
    practice_activity: Optional[Union[int, bool, str]]
    what_activity: Optional[str]
    created_at: Optional[str]
    updated_at: Optional[str]

