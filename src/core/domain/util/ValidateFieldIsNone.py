from typing import Any
from src.core.usecase.utils import MyCustomError


class ValidateFieldIsNone:

    @staticmethod
    def validate(field: Any, name_parameter: str):
        if isinstance(field, str):
            field = field.strip()

        if isinstance(field, bool):
            return field

        if isinstance(field, int):
            return field

        if not field:
            raise MyCustomError(f"[{name_parameter}] não pode ser nulo")
        return field
