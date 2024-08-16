#! python3
# phoneAndEmail.py - Находит номера телефонов и адреса электронной почты в буфере обмена.


import pyperclip, re


phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?   # код города
    (\s|-|\.)?   # разделитель
    (\d{3})   # первые 3 цифры
    (\s|-|\.)   # разделитель
    (\d{4})   # последние 4 цифры
    (\s*(ext|x|ext.)\s*(\d{2,5}))?   # расширение
    )''', re.VERBOSE)

# Cоздать регулярное выражение для электронной почты.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   # username
    @                   # @ symbol
    [a-zA-Z0-9.-]+      # domain name
    (\.[a-zA-Z]{2,4})   # dot-something
    )''', re.VERBOSE)

# Найти совпадения в тексте буфера обмена.
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Копирует результаты в буфер обмена
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Скопировано в буфер обмена:')
    print('\n'.join(matches))
else:
    print('Номера телефонов и адреса электронной почты не найдены.')
