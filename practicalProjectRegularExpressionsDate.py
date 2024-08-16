#chat GPT

import re

# Регулярное выражение для формата ДД/ММ/ГГГГ
date_pattern = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/([12]\d{3})$'

date_string = "29/02/2024"  # Пример даты

match = re.match(date_pattern, date_string)
if match:
    day, month, year = match.groups()
    day = int(day)
    month = int(month)
    year = int(year)
    print(f"Day: {day}, Month: {month}, Year: {year}")
else:
    print("Invalid date format")

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def is_valid_date(day, month, year):
    # Дни в месяцах
    days_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30,
        5: 31, 6: 30, 7: 31, 8: 31,
        9: 30, 10: 31, 11: 30, 12: 31
    }

    # Учет високосного года
    if is_leap_year(year):
        days_in_month[2] = 29

    # Проверка допустимости
    if month in days_in_month and 1 <= day <= days_in_month[month]:
        return True
    return False

if match:
    day, month, year = match.groups()
    day = int(day)
    month = int(month)
    year = int(year)

    if is_valid_date(day, month, year):
        print(f"The date {day:02}/{month:02}/{year} is valid.")
    else:
        print(f"The date {day:02}/{month:02}/{year} is invalid.")
else:
    print("Invalid date format")

# ответственно заявляю, что я ознакомился с приведенным кодом и темой и основными концепциями, однако освоение регулярных выражений займет какое то время и не всегда будет необходимо
# это касается и остальных практических проектов в Регулярных выражениях, кроме
