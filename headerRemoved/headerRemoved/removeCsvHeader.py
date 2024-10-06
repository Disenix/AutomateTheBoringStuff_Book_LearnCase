#! python3
# removeCsvHeader.py - Удаляет загооловок из всех CSV-Файлов в текущем рабочем каталоге

# Рабочий каталог

import csv, os

os.makedirs('headerRemoved', exist_ok=True)

# Пройти по всем файлам в текущем рабочем каталоге.
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue #skip non-csv files

    print('Удаление заголовка из ' + csvFilename + '...')

    # Прочитать CSV-файл (пропустив первую строку)
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue # Пропустить первую строку
        csvRows.append(row)
    csvFileObj.close()

    # Записать CSV-файл
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()

