#! python3
# renameDates.py - переименовывает имена файлов с американским форматом даты MM-DD-YYYY
# в европейский DD-MM-YYYY.

import shutil, os, re

# Создает регулярное выражение, которое сопоставляет файлы с американским форматом даты
datePattern = re.compile(r"""^(.*?) # Весь текст перед датой
    ((0|1)?\d)- # одна или две цифры для месяца
    ((0|1|2|3)?\d)- # одна или две цтфры для дня
    ((19|20)\d\d) # четыре цифры для года
    (.*?)$ # весь текст после даты
    """, re.VERBOSE)

# Пройтись по файлам в рабочем каталоге.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # Пропустить файлы без даты.
    if mo == None:
        continue

    # Получить различные части имени файла
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Формируем имя файла в европейском стиле.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Получаем полные абсолютные пути к файлам
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Переименовываем файлы
    print(f'Renaming "{amerFilename}" to "{euroFilename}"...')
    #shutil.move(amerFilename, euroFilename) # расомментировать после тестирования
