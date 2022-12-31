from typing import Union
from datetime import datetime
from src.core.domain.util.ValidateFieldIsNone import ValidateFieldIsNone


class Patient:
    __id: Union[None, int]
    __first_name: str
    __last_name: str
    __username: str
    __password: str
    __birth_date: Union[datetime, None]
    __email: str
    __is_admin: int
    __is_active: int
    __genre: str
    __zipcode: str
    __city: str
    __street: str
    __number: str
    __district: str
    __practice_activity: int
    __what_activity: str
    __created_at: datetime
    __updated_at: datetime

    def __init__(self,
                 id_patient: Union[None, int],
                 first_name: str,
                 last_name: str,
                 username: str,
                 password: str,
                 birth_date: Union[datetime, None],
                 email: str,
                 is_admin: int,
                 is_active: int,
                 genre: str,
                 zipcode: str,
                 city: str,
                 street: str,
                 number: str,
                 district: str,
                 practice_activity: int,
                 what_activity: str,
                 created_at: Union[datetime, None],
                 updated_at: Union[datetime, None]) -> None:
        self.__id = id_patient
        self.__first_name = ValidateFieldIsNone.validate(field=first_name, name_parameter="first_name")
        self.__last_name = ValidateFieldIsNone.validate(field=last_name, name_parameter="last_name")
        self.__username = ValidateFieldIsNone.validate(field=username, name_parameter="username")
        self.__password = ValidateFieldIsNone.validate(field=password, name_parameter="password")
        self.__birth_date = ValidateFieldIsNone.validate(field=birth_date, name_parameter="birth_date")
        self.__email = email
        self.__is_admin = is_admin
        self.__is_active = is_active
        self.__genre = ValidateFieldIsNone.validate(field=genre, name_parameter="genre")
        self.__zipcode = ValidateFieldIsNone.validate(field=zipcode, name_parameter="zipcode")
        self.__city = ValidateFieldIsNone.validate(field=city, name_parameter="city")
        self.__street = ValidateFieldIsNone.validate(field=street, name_parameter="street")
        self.__number = ValidateFieldIsNone.validate(field=number, name_parameter="number")
        self.__district = ValidateFieldIsNone.validate(field=district, name_parameter="district")
        self.__practice_activity = practice_activity
        self.__what_activity = what_activity
        self.__created_at = created_at
        self.__updated_at = updated_at

    @property
    def id(self) -> int:
        return self.__id

    @property
    def first_name(self) -> str:
        return self.__first_name

    @property
    def last_name(self) -> str:
        return self.__last_name

    @property
    def username(self) -> str:
        return self.__username

    @property
    def password(self) -> str:
        return self.__password

    @property
    def birth_date(self) -> datetime:
        return self.__birth_date

    @property
    def email(self) -> str:
        return self.__last_name

    @property
    def is_admin(self) -> int:
        return self.__is_admin

    @property
    def is_active(self) -> int:
        return self.__is_active

    @property
    def genre(self) -> str:
        return self.__genre

    @property
    def zipcode(self) -> str:
        return self.__zipcode

    @property
    def city(self) -> str:
        return self.__city

    @property
    def street(self) -> str:
        return self.__street

    @property
    def number(self) -> str:
        return self.__number

    @property
    def district(self) -> str:
        return self.__district

    @property
    def practice_activity(self) -> Union[int, bool]:
        return self.__practice_activity

    @property
    def what_activity(self) -> str:
        return self.__what_activity

    @property
    def created_at(self) -> datetime:
        return self.__created_at

    @property
    def updated_at(self) -> datetime:
        return self.__updated_at

    def json(self):
        return {
            "id": self.__id,
            "first_name": self.__first_name,
            "last_name": self.__last_name,
            "username": self.__username,
            "password": self.__password,
            "birth_date": self.__birth_date,
            "email": self.__email,
            "is_admin": self.__is_admin,
            "is_active": self.__is_active,
            "genre": self.__genre,
            "zipcode": self.__zipcode,
            "city": self.__city,
            "street": self.__street,
            "number": self.__number,
            "district": self.__district,
            "practice_activity": self.__practice_activity,
            "what_activity": self.__what_activity,
            "created_at": self.__created_at,
            "updated_at": self.__updated_at
        }
