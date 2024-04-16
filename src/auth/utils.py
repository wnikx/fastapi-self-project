import secrets


def generate_token_invate():
    """Генерирование случайного токена для инвайта"""
    return secrets.token_hex(16)
