from typing import Any


class LoginDto:

    @staticmethod
    def format(user: Any):
        if isinstance(user, dict):
            return {
                "id": user["id_patient"],
                "name": user["first_name"],
                "username": user["username"],
                "admin": user["is_admin"]
            }
        else:
            new_array: list = []
            for i in range(len(user)):
                new_array.append({
                    "id": user[i]["id_person"],
                    "name": user["first_name"],
                    "username": user[i]["username"],
                    "admin": user[i]["is_admin"]
                })
            return new_array
