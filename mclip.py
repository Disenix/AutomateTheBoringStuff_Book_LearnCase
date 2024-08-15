#! python3
# mclip.py - A multi-clipboard program.

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: py mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]    # first command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)

# создание пакетного файла. создайте текстовый документ через блокнот

# в этом документе опишите путь до нашего скрипта без пробелов в формате:

# @py.exe C:\путь_к_файлу\mclip.py %*
# @pause

# сохраните наш файл как mclip.bat . мы сформировали пакетный файл,
# который теперь нужно переместить в C\Windows\
# теперь мы можем запускать наш скрипт через комбинацию клавиш Win+R и ввести команду " mclip agree " или например 'mclip busy'
