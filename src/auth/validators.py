import re


class PasswordValidator:
    @staticmethod
    def validate_password_strength(password: str) -> bool:
        """Validate password strength."""
        # Минимальная длина пароля
        min_length = 8

        # Проверка длины пароля
        if len(password) < min_length:
            return False

        # Проверка наличия хотя бы одной цифры
        if not any(char.isdigit() for char in password):
            return False

        # Проверка наличия хотя бы одной буквы в верхнем регистре
        if not any(char.isupper() for char in password):
            return False

        # Проверка наличия хотя бы одной буквы в нижнем регистре
        if not any(char.islower() for char in password):
            return False

        # Проверка наличия хотя бы одного специального символа
        special_characters = r"[ !@#$%^&*()_+{}\[\]:;<>,.?/~`-]"
        if not re.search(special_characters, password):
            return False

        return True
