#! python3
# countdown.py - простой скрипт обратного отсчета

import time, subprocess

timeLeft = 60
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1

# в конце обратного отсчета воспроизвести звуковой файл
subprocess.Popen(['start', 'alarm.wav'], shell=True)

# можно так же открыть текстоовый файл по окончанию
# таймера с надписью " время перерыва закончилось!"
# по сути таким образом создастся всплывающее окно
# или например использовать webbrowser.open(), чтобы открыть вебсайт
