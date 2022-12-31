import re
from src.core.usecase.utils import MyCustomError


class ValidateCpf:

    @staticmethod
    def validate(cpf: str) -> str:
        # Verifica a formatação do CPF
        if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
            raise MyCustomError(message="Cpf with format invalid, expecting this: 000.000.000-00", status_code=400)

        # Obtém apenas os números do CPF, ignorando pontuações
        numbers = [int(digit) for digit in cpf if digit.isdigit()]

        # Verifica se o CPF possui 11 números ou se todos são iguais:
        if len(numbers) != 11 or len(set(numbers)) == 1:
            raise MyCustomError(message="Cpf not must have numbers equal", status_code=400)

        # Validação do primeiro dígito verificador:
        sum_of_products = sum(a * b for a, b in zip(numbers[0:9], range(10, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[9] != expected_digit:
            raise MyCustomError(message="Cpf invalid!", status_code=400)

        # Validação do segundo dígito verificador:
        sum_of_products = sum(a * b for a, b in zip(numbers[0:10], range(11, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[10] != expected_digit:
            raise MyCustomError(message="Cpf invalid!", status_code=400)

        return cpf