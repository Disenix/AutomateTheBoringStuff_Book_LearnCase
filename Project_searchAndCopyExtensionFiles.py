#! python3
# Project_searchAndCopyExtensionFiles.py - программа поиска и копирования
# определенных файлов по папкам

import os
import shutil

def selective_copy(source_folder, extensions, destination_folder):
    """
    Копирует файлы с указанными расширениями из source_folder и всех его подкаталогов в destination_folder.

    :param source_folder: Путь к исходной папке для поиска файлов.
    :param extensions: Список расширений файлов, которые нужно копировать.
    :param destination_folder: Путь к папке, куда будут копироваться файлы.
    """

    # Создаем папку назначения, если она не существует
    os.makedirs(destination_folder, exist_ok=True)

    # Проходим по всем файлам и папкам в исходной папке
    for foldername, subfolders, filenames in os.walk(source_folder):
        for filename in filenames:
            # Проверяем, что расширение файла совпадает с заданным
            if any(filename.lower().endswith(ext) for ext in extensions):
                # Получаем полный путь к файлу
                file_path = os.path.join(foldername, filename)

                # Копируем файл в папку назначения
                shutil.copy(file_path, destination_folder)
                print(f'Copy {file_path} in {destination_folder}')

if __name__ == "__main__":
    source_folder = input("Введите путь к исходной папке: ")
    destination_folder = input("Введите путь к папке назначения: ")
    extensions = input("Введите расширения файлов для копирования (через запятую, например, .jpg, pdf): ").split(',')

    selective_copy(source_folder, extensions, destination_folder)

 #by chatGPT
