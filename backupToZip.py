#! python3
# backupToZip.py - Копирует всю папку и ее содержимое в
# ZIP-файл, имя которого увеличивается

import zipfile, os

def backupToZip(folder):
    # Резервное копирование всего содержимого "folder" в ZIP-файл.

    folder = os.path.abspath(folder) # убедитесь, что folder является абсолютным

    # Определите имя файла, которое должен использовать этот код, на основе
    # того, какие файлы уже существуют.

    number = 1

    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1

    # Cоздание ZIP-файла
    print(f'Creating {zipFilename}...')
    backupToZip = zipfile.ZipFile(zipFilename, 'w')

    # Пройти по всему дереву папок и сжать файлы в каждой папке.
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')

        # Добавить текущую папку в ZIP-файл.
        backupZip.write(foldername)

        # Добавить все файлы в этой папке в ZIP-файл.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue   # не создавать резервную копию резервных ZIP-файлов
            backupZip.write(os.path.join(foldername, filename))
    backupToZip.close()
    print('Done.')

backupToZip('C:\\delicious')

