# Regular expressions(regexes). Регулярные выражения
# isPhoneNumber.py - программа поиска номера телефона в строке

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False

    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False

    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

message = 'Позвоните мне завтра по телефону 415-555-1011. 415-555-9999 - мой офис.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Найден номер телефона: ' + chunk)
print('Готово')


# \d{3}-\d{3}-\d{4}
