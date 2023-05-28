from typing import Any


class PatientDto:

    @staticmethod
    def format(patient: Any):
        if isinstance(patient, dict):

            return {
                "id": patient["id_patient"],
                "first_name": patient["first_name"],
                "last_name": patient["last_name"],
                "username": patient["username"],
                "birth_date": PatientDto.__validate_birth_date(patient["birth_date"]),
                "email": patient["email"],
                "genre": patient["genre"],
                "zipcode": patient["zipcode"],
                "city": patient["city"],
                "street": patient["street"],
                "number": patient["number"],
                "district": patient["district"],
                "practice_activity": patient["practice_activity"],
                "what_activity": patient["what_activity"],
                "created_at": PatientDto.__validate_created_at(patient["created_at"]),
                "updated_at": PatientDto.__validate_updated_at(patient["updated_at"])
            }
        else:
            new_array: list = []
            for i, value in enumerate(patient):
                new_array.append({
                    "id": patient[i]["id_patient"],
                    "name": patient[i]["first_name"],
                    "last_name": patient[i]["last_name"],
                    "username": patient[i]["username"],
                    "birth_date": PatientDto.__validate_birth_date(patient[i]["birth_date"]),
                    "email": patient[i]["email"],
                    "genre": patient[i]["genre"],
                    "zipcode": patient[i]["zipcode"],
                    "city": patient[i]["city"],
                    "street": patient[i]["street"],
                    "number": patient[i]["number"],
                    "district": patient[i]["district"],
                    "practice_activity": patient[i]["practice_activity"],
                    "what_activity": patient[i]["what_activity"],
                    "created_at": PatientDto.__validate_created_at(patient[i]["created_at"]),
                    "updated_at": PatientDto.__validate_updated_at(patient[i]["updated_at"])
                })
            return new_array

    @staticmethod
    def __validate_birth_date(birth_date: Any):
        if not birth_date:
            return None
        return birth_date.strftime("%d/%m/%Y")

    @staticmethod
    def __validate_created_at(created_at: Any):
        if not created_at:
            return None
        return created_at.strftime("%d/%m/%Y")

    @staticmethod
    def __validate_updated_at(updated_at: Any):
        if not updated_at:
            return None
        return updated_at.strftime("%d/%m/%Y")
