#! python3
# stopwatch.py - Простая программа - секундомер

import time

# Отображение инструкций программы
print('''Нажмите ENTER, чтобы начать. После этого нажмите ENTER,  чтобы "щелкнуть" секундомер.
Нажмите Ctrl-C, чтобы выйти.''')
input()             # нажмите Enter, чтобы начать
print('Начало')
startTime = time.time()   # Получить время начала первого круга
lastTime = startTime
lapNum = 1

#TODO: Начать отслеживание времени кругов
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time() # Сбросить время последнего круга
except KeyboardInterrupt:
    # Обработать исключение Ctrl-C, чтобы сообщение об ошибке не отображалось.
    print('\nDone.')

