#! python3
# mapIt.py - запускает карту в браузере, используя аддрес из
# командной строки

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # Получить адрес из командной строки.
    adress = ' '.join(sys.argv[1:])
else:
    # Получить адрес из буфера обмена.
    adress = pyperclip.paste()

webbrowser.open('http://www.google.com/maps/place/' + adress)
