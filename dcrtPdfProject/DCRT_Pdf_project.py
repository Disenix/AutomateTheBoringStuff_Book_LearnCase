#! python3

import PyPDF2

# Функция для чтения словаря
def load_dictionary(filename):
    with open(filename, 'r') as file:
        return [word.strip() for word in file.readlines()]

# Функция для перебора паролей
def brute_force_pdf(pdf_path, dictionary_path):
    # Чтение словаря
    words = load_dictionary(dictionary_path)

    # Открываем зашифрованный PDF
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)

        if not reader.is_encrypted:
            print("Файл не зашифрован.")
            return

        # Перебираем слова
        for word in words:
            # Пробуем строчную и заглавную форму слова
            for password in (word.lower(), word.upper()):
                print(f"Пробую пароль: {password}")
                try:
                    # Пробуем расшифровать
                    if reader.decrypt(password) == 1:
                        print(f"Пароль найден: {password}")
                        return password
                except:
                    pass  # Игнорируем ошибки

        print("Пароль не найден в словаре.")
        return None

# Укажи путь к твоему PDF и файлу словаря
pdf_file_path = 'encrypted.pdf'
dictionary_file_path = 'dictionary.txt'

# Запускаем процесс взлома
brute_force_pdf(pdf_file_path, dictionary_file_path)


# by ChatGPT
