#! python3
# getOpenWeather.py - Выводдит погоду для местоположения из командной строки

APPID = 'my API in email letter'

import json, requests, sys

# Вычислить местоположение из аргументов командной строки
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()

location = ' '.join(sys.argv[1:])

# Загрузите данные JSON из API OpenWeatherMap.org.
url = 'https://api.openweathermap.org/data/2.5/forecast?q=%s&cnt=3&APPID=%s' % (location, APPID)
response = requests.get(url)
response.raise_for_status()

# Раскомментируйте, чтобы увидеть необработанный текст JSON:
#print(response.text)

# Загружает данные JSON в переменную Python
weatherData = json.loads(response.text)

# Выводит описание погоды
w = weatherData['list']
print('Текущая погода в %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Завтра:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Послезавтра:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])

# Проверка чатом GPT выявила Старый API Endpoint.
# Они изменили API, и вместо него нужно использовать forecast или onecall.
# было: url = 'https://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=%s ' % (location, APPID)
# стало: url = 'https://api.openweathermap.org/data/2.5/forecast?q=%s&cnt=3&APPID=%s' % (location, APPID)
