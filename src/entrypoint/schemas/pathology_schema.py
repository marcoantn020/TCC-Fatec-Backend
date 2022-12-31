from pydantic import BaseModel
from pydantic import Field


class PathologyInputCreate(BaseModel):
    id_patient: int = Field("2")
    has_diabetes: int = Field("0")
    observations_diabetes: str = Field("")
    have_hypertension: int = Field("1")
    observations_hypertension: str = Field("lorem ipsu")
    take_medicines: int = Field("0")
    observations_medicines: str = Field("")
    allergic_to_medicine: int = Field("0")
    which_medicine: str = Field("")
    have_cancer: int = Field("0")
    which_type_cancer: str = Field("")
    has_pacemaker: int = Field("0")
    has_pin: int = Field("1")
    is_cadiaco: int = Field("0")
    have_foot_surgery: int = Field("1")
    which_foot: str = Field("pe direito")
    about_the_foot_of_the_patient_has_callus: int = Field("0")
    about_the_foot_of_the_patient_has_callosity: int = Field("0")
    about_the_foot_of_the_patient_has_fissure: int = Field("0")
    about_the_foot_of_the_patient_has_dryness: int = Field("0")
    about_the_foot_of_the_patient_has_psoriasis: int = Field("0")
    about_the_foot_of_the_patient_has_pantar_wart: int = Field("0")
    about_the_nail_of_the_patient_has_onychocryptosis: int = Field("0")
    about_the_nail_of_the_patient_has_onycholysis: int = Field("0")
    about_the_nail_of_the_patient_has_onychomycosis: int = Field("0")
    about_the_nail_of_the_patient_has_onychophoresis: int = Field("0")
    sensitive_to_pain: str = Field("pouca")
    type_of_sock: str = Field("meia de algodao")
    type_of_shoe: str = Field("tenis")
    shoe_number: str = Field("42")


class PathologyCreate(BaseModel):
    id: int
