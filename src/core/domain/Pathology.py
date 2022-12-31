from datetime import datetime
from typing import Union
from src.core.domain.util.ValidateFieldIsNone import ValidateFieldIsNone


class Pathology:
    __id_pathology: Union[None, int]
    __id_patient: int
    __has_diabetes: int
    __observations_diabetes: str
    __have_hypertension: int
    __observations_hypertension: str
    __take_medicines: int
    __observations_medicines: str
    __allergic_to_medicine: int
    __which_medicine: str
    __have_cancer: int
    __which_type_cancer: str
    __has_pacemaker: int
    __has_pin: int
    __is_cadiaco: int
    __have_foot_surgery: int
    __which_foot: str
    __about_the_foot_of_the_patient_has_callus: int
    __about_the_foot_of_the_patient_has_callosity: int
    __about_the_foot_of_the_patient_has_fissure: int
    __about_the_foot_of_the_patient_has_dryness: int
    __about_the_foot_of_the_patient_has_psoriasis: int
    __about_the_foot_of_the_patient_has_pantar_wart: int
    __about_the_nail_of_the_patient_has_onychocryptosis: int
    __about_the_nail_of_the_patient_has_onycholysis: int
    __about_the_nail_of_the_patient_has_onychomycosis: int
    __about_the_nail_of_the_patient_has_onychophoresis: int
    __sensitive_to_pain: str
    __type_of_sock: str
    __type_of_shoe: str
    __shoe_number: str
    __created_at: datetime
    __updated_at: datetime

    def __init__(self,
                 id_patient: int,
                 has_diabetes: int,
                 observations_diabetes: str,
                 have_hypertension: int,
                 observations_hypertension: str,
                 take_medicines: int,
                 observations_medicines: str,
                 allergic_to_medicine: int,
                 which_medicine: str,
                 have_cancer: int,
                 which_type_cancer: str,
                 has_pacemaker: int,
                 has_pin: int,
                 is_cadiaco: int,
                 have_foot_surgery: int,
                 which_foot: str,
                 about_the_foot_of_the_patient_has_callus: int,
                 about_the_foot_of_the_patient_has_callosity: int,
                 about_the_foot_of_the_patient_has_fissure: int,
                 about_the_foot_of_the_patient_has_dryness: int,
                 about_the_foot_of_the_patient_has_psoriasis: int,
                 about_the_foot_of_the_patient_has_pantar_wart: int,
                 about_the_nail_of_the_patient_has_onychocryptosis: int,
                 about_the_nail_of_the_patient_has_onycholysis: int,
                 about_the_nail_of_the_patient_has_onychomycosis: int,
                 about_the_nail_of_the_patient_has_onychophoresis: int,
                 sensitive_to_pain: str,
                 type_of_sock: str,
                 type_of_shoe: str,
                 shoe_number: str,
                 created_at: datetime,
                 updated_at: datetime) -> None:
        self.__id_pathology = None
        self.__id_patient = ValidateFieldIsNone.validate(field=id_patient, name_parameter="id_person")
        self.__has_diabetes = has_diabetes
        self.__observations_diabetes = observations_diabetes
        self.__have_hypertension = have_hypertension
        self.__observations_hypertension = observations_hypertension
        self.__take_medicines = take_medicines
        self.__observations_medicines = observations_medicines
        self.__allergic_to_medicine = allergic_to_medicine
        self.__which_medicine = which_medicine
        self.__have_cancer = have_cancer
        self.__which_type_cancer = which_type_cancer
        self.__has_pacemaker = has_pacemaker
        self.__has_pin = has_pin
        self.__is_cadiaco = is_cadiaco
        self.__have_foot_surgery = have_foot_surgery
        self.__which_foot = which_foot
        self.__about_the_foot_of_the_patient_has_callus = about_the_foot_of_the_patient_has_callus
        self.__about_the_foot_of_the_patient_has_callosity = about_the_foot_of_the_patient_has_callosity
        self.__about_the_foot_of_the_patient_has_fissure = about_the_foot_of_the_patient_has_fissure
        self.__about_the_foot_of_the_patient_has_dryness = about_the_foot_of_the_patient_has_dryness
        self.__about_the_foot_of_the_patient_has_psoriasis = about_the_foot_of_the_patient_has_psoriasis
        self.__about_the_foot_of_the_patient_has_pantar_wart = about_the_foot_of_the_patient_has_pantar_wart
        self.__about_the_nail_of_the_patient_has_onychocryptosis = about_the_nail_of_the_patient_has_onychocryptosis
        self.__about_the_nail_of_the_patient_has_onycholysis = about_the_nail_of_the_patient_has_onycholysis
        self.__about_the_nail_of_the_patient_has_onychomycosis = about_the_nail_of_the_patient_has_onychomycosis
        self.__about_the_nail_of_the_patient_has_onychophoresis = about_the_nail_of_the_patient_has_onychophoresis
        self.__sensitive_to_pain = sensitive_to_pain
        self.__type_of_sock = type_of_sock
        self.__type_of_shoe = type_of_shoe
        self.__shoe_number = shoe_number
        self.__created_at = created_at
        self.__updated_at = updated_at

    def id(self) -> Union[None, int]:
        return self.__id_pathology

    def id_patient(self) -> int:
        return self.__id_patient

    def has_diabetes(self) -> int:
        return self.__has_diabetes

    def observations_diabetes(self) -> str:
        return self.__observations_diabetes

    def have_hypertension(self) -> int:
        return self.__have_hypertension

    def observations_hypertension(self) -> str:
        return self.__observations_hypertension

    def take_medicines(self) -> int:
        return self.__take_medicines

    def observations_medicines(self) -> str:
        return self.__observations_medicines

    def allergic_to_medicine(self) -> int:
        return self.__allergic_to_medicine

    def which_medicine(self) -> str:
        return self.__which_medicine

    def have_cancer(self) -> int:
        return self.__have_cancer

    def which_type_cancer(self) -> str:
        return self.__which_type_cancer

    def has_pacemaker(self) -> int:
        return self.__has_pacemaker

    def has_pin(self) -> int:
        return self.__has_pin

    def is_cadiaco(self) -> int:
        return self.__is_cadiaco

    def have_foot_surgery(self) -> int:
        return self.__have_foot_surgery

    def which_foot(self) -> str:
        return self.__which_foot

    def about_the_foot_of_the_patient_has_callus(self) -> int:
        return self.__about_the_foot_of_the_patient_has_callus

    def about_the_foot_of_the_patient_has_callosity(self) -> int:
        return self.__about_the_foot_of_the_patient_has_callosity

    def about_the_foot_of_the_patient_has_fissure(self) -> int:
        return self.__about_the_foot_of_the_patient_has_fissure

    def about_the_foot_of_the_patient_has_dryness(self) -> int:
        return self.__about_the_foot_of_the_patient_has_dryness

    def about_the_foot_of_the_patient_has_psoriasis(self) -> int:
        return self.__about_the_foot_of_the_patient_has_psoriasis

    def about_the_foot_of_the_patient_has_pantar_wart(self) -> int:
        return self.__about_the_foot_of_the_patient_has_pantar_wart

    def about_the_nail_of_the_patient_has_onychocryptosis(self) -> int:
        return self.__about_the_nail_of_the_patient_has_onychocryptosis

    def about_the_nail_of_the_patient_has_onycholysis(self) -> int:
        return self.__about_the_nail_of_the_patient_has_onycholysis

    def about_the_nail_of_the_patient_has_onychomycosis(self) -> int:
        return self.__about_the_nail_of_the_patient_has_onychomycosis

    def about_the_nail_of_the_patient_has_onychophoresis(self) -> int:
        return self.__about_the_nail_of_the_patient_has_onychophoresis

    def sensitive_to_pain(self) -> str:
        return self.__sensitive_to_pain

    def type_of_sock(self) -> str:
        return self.__type_of_sock

    def type_of_shoe(self) -> str:
        return self.__type_of_shoe

    def shoe_number(self) -> str:
        return self.__shoe_number

    def created_at(self) -> datetime:
        return self.__created_at

    def updated_at(self) -> datetime:
        return self.__updated_at

    def json(self):
        return {
            "id": self.__id_pathology,
            "id_patient": self.__id_patient,
            "has_diabetes": self.__has_diabetes,
            "observations_diabetes": self.__observations_diabetes,
            "have_hypertension": self.__have_hypertension,
            "observations_hypertension": self.__observations_hypertension,
            "take_medicines": self.__take_medicines,
            "observations_medicines": self.__observations_medicines,
            "allergic_to_medicine": self.__allergic_to_medicine,
            "which_medicine": self.__which_medicine,
            "have_cancer": self.__have_cancer,
            "which_type_cancer": self.__which_type_cancer,
            "has_pacemaker": self.__has_pacemaker,
            "has_pin": self.__has_pin,
            "is_cadiaco": self.__is_cadiaco,
            "have_foot_surgery": self.__have_foot_surgery,
            "which_foot": self.__which_foot,
            "about_the_foot_of_the_patient_has_callus": self.__about_the_foot_of_the_patient_has_callus,
            "about_the_foot_of_the_patient_has_callosity": self.__about_the_foot_of_the_patient_has_callosity,
            "about_the_foot_of_the_patient_has_fissure": self.__about_the_foot_of_the_patient_has_fissure,
            "about_the_foot_of_the_patient_has_dryness": self.__about_the_foot_of_the_patient_has_dryness,
            "about_the_foot_of_the_patient_has_psoriasis": self.__about_the_foot_of_the_patient_has_psoriasis,
            "about_the_foot_of_the_patient_has_pantar_wart": self.__about_the_foot_of_the_patient_has_pantar_wart,
            "about_the_nail_of_the_patient_has_onychocryptosis": self.__about_the_nail_of_the_patient_has_onychocryptosis,
            "about_the_nail_of_the_patient_has_onycholysis": self.__about_the_nail_of_the_patient_has_onycholysis,
            "about_the_nail_of_the_patient_has_onychomycosis": self.__about_the_nail_of_the_patient_has_onychomycosis,
            "about_the_nail_of_the_patient_has_onychophoresis": self.__about_the_nail_of_the_patient_has_onychophoresis,
            "sensitive_to_pain": self.__sensitive_to_pain,
            "type_of_sock": self.__type_of_sock,
            "type_of_shoe": self.__type_of_shoe,
            "shoe_number": self.__shoe_number,
            "created_at": self.__created_at,
            "updated_at": self.__updated_at,
        }
