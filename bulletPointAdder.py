#! python 3
# bulletPointAdder.py - добавляет маркеры Википедии в начало
# каждой строки текста в буфере обмена

import pyperclip
text = pyperclip.paste()

# TODO: Разделить строки и добавить звездочки
lines = text.split('\n')
for i in range(len(lines)):# проходит по всем индексам в списке "lines"
    lines[i] = '* ' + lines[i] # добавляет звездочку к каждой строке в списке "lines"

text = '\n'.join(lines)

pyperclip.copy(text)
