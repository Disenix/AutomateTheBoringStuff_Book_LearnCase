#! python 3
# readCensusExcel.py - таблицы численности насления и количества переписных участков для
# каждого округа

import openpyxl, pprint
print('Открытие рабочей книги...')
wb = oprnpyxl.loand_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData = {}

# TODO
print('Чтение строк...')
for row in range(2, sheet.max_row + 1):
    # Каждая строка в электронной таблицк содержит данные по одному переписному участку
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    # Убедитесь, что ключ для этого штата существует
    countyData.setdefault(state, {})
    # Убедитесь, что ключ для  этого округа в этом штате существует.
    countyData[state].setdefault(county, {'tracts': 0, 'pop':0})

    # Каждая строка представляет один переписной участок, поэтому увеличиваем на единицу
    countyData[state][county]['tracts'] += 1
    # Увеличиваем население округа на население в этом переписном участке
    countyData[state][county]['pop'] += int(pop)

# Открыть новый текстовый файл и записать в него содержимое countyData
print('Запись результатов...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Готово')
