#! python3
# resizeAndAddLogo.py - Изменяет размер всех изображений в текущем каталоге, чтобы они
# уместились в квадрате 300х300, и добавляет catlogo.png в правый нижний угол.

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

# Открываем изображение логотипа
logoIm = Image.open(LOGO_FILENAME).convert("RGBA")
originalLogoWidth, originalLogoHeight = logoIm.size

# Создаем папку для результатов
os.makedirs('withLogo', exist_ok=True)

# Перебираем все файлы в рабочем каталоге
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == LOGO_FILENAME:
        continue  # Пропустить файлы, не являющиеся изображениями, и сам файл логотипа

    im = Image.open(filename).convert("RGBA")
    width, height = im.size

    # Проверяем, нужно ли изменить размер изображения
    if width > SQUARE_FIT_SIZE or height > SQUARE_FIT_SIZE:
        # Вычисляем новые ширину и высоту
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        # Изменяем размер изображения
        print(f'Resizing {filename}...')
        im = im.resize((width, height), Image.LANCZOS)

    # Пропорционально уменьшаем логотип
    logoScaleFactor = 0.2  # Логотип займет 20% ширины изображения
    newLogoWidth = int(width * logoScaleFactor)
    newLogoHeight = int((originalLogoHeight / originalLogoWidth) * newLogoWidth)
    logoImResized = logoIm.resize((newLogoWidth, newLogoHeight), Image.LANCZOS)

    # Располагаем логотип в правом нижнем углу
    position = (width - newLogoWidth - 10, height - newLogoHeight - 10)  # 10px отступ

    # Добавляем логотип
    print(f'Adding logo to {filename}...')
    im.paste(logoImResized, position, logoImResized)

    # Сохраняем результат
    output_path = os.path.join('withLogo', filename)
    im.convert("RGB").save(output_path)
    print(f'Saved to {output_path}')

