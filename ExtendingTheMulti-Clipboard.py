import shelve
import pyperclip
import sys

mcb_shelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3:
    command = sys.argv[1].lower()
    keyword = sys.argv[2]

    if command == 'save':
        mcb_shelf[keyword] = pyperclip.paste()
    elif command == 'delete':
        if keyword in mcb_shelf:
            del mcb_shelf[keyword]
            print(f'Keyword "{keyword}" deleted.')
        else:
            print(f'Keyword "{keyword}" not found.')
elif len(sys.argv) == 2:
    command = sys.argv[1].lower()

    if command == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
        print('Keywords copied to clipboard.')
    elif command == 'delete':
        mcb_shelf.clear()
        print('All keywords deleted.')
    elif command in mcb_shelf:
        pyperclip.copy(mcb_shelf[command])
        print(f'Content for "{command}" copied to clipboard.')
    else:
        print(f'Keyword "{command}" not found.')

mcb_shelf.close()

# Generate by ChatGPT
''' Как это работает:
1.Удаление конкретного ключевого слова:

Если вы введете команду delete <keyword>, программа проверит,
существует ли ключевое слово, и удалит его. Если ключевое
слово не найдено, программа сообщит об этом.

2.Удаление всех ключевых слов:

Если вы введете команду delete, программа удалит
все ключевые слова из полки с помощью метода clear().

Примеры использования:
python mcb.py save spam — сохраняет текущий текст из буфера обмена под ключом spam.
python mcb.py spam — копирует текст, сохраненный под ключом spam, обратно в буфер обмена.
python mcb.py list — копирует все ключевые слова в буфер обмена.
python mcb.py delete spam — удаляет ключевое слово spam.
python mcb.py delete — удаляет все ключевые слова.

Эти расширения помогут вам лучше управлять данными в многобуферной системе,
добавляя возможность удаления отдельных элементов или очистки всей полки целиком.'''
