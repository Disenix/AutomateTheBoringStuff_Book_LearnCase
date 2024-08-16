# chat GPT

import re

def regex_strip(string, chars=None):
    if chars is None:
        # Удаление пробельных символов из начала и конца строки
        return re.sub(r'^\s+|\s+$', '', string)
    else:
        # Экранирование символов, чтобы они правильно воспринимались в регулярном выражении
        chars = re.escape(chars)
        # Создание шаблона для удаления символов из начала и конца строки
        pattern = rf'^[{chars}]+|[{chars}]+$'
        return re.sub(pattern, '', string)

# Примеры использования функции
print(regex_strip("   Hello, World!   "))  # Должно вывести "Hello, World!"
print(regex_strip("...Hello, World!...", "."))  # Должно вывести "Hello, World!"
print(regex_strip("abcHelloabc", "abc"))  # Должно вывести "Hello"


# ответственно заявляю, что я ознакомился с приведенным кодом и темой и основными концепциями, однако освоение регулярных выражений займет какое то время и не всегда будет необходимо
