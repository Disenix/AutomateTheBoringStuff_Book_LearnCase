# chat GPT
import re

def is_strong_password(password):
    # Проверка длины пароля (не менее 8 символов)
    if len(password) < 8:
        return False

    # Проверка наличия хотя бы одной заглавной буквы
    if not re.search(r'[A-Z]', password):
        return False

    # Проверка наличия хотя бы одной строчной буквы
    if not re.search(r'[a-z]', password):
        return False

    # Проверка наличия хотя бы одной цифры
    if not re.search(r'\d', password):
        return False

    # Если пароль прошел все проверки
    return True

# Пример использования функции
passwords = ["Password123", "weakpass", "12345678", "StrongPass1", "NoDigitsHere", "Short1"]
for pwd in passwords:
    if is_strong_password(pwd):
        print(f"'{pwd}' is a strong password.")
    else:
        print(f"'{pwd}' is not a strong password.")

# ну тут понятно более менее
