#! python3
# project_DeletingUnneededFiles.py - программа поиска больших файлов

import os

def findLargeFiles(folder, size_threshold):
    """
    Ищет файлы, размер которых превышает указанный порог, и выводит их абсолютные пути.

    :param folder: Путь к папке для поиска файлов.
    :param size_threshold: Размер файла в байтах, выше которого файл считается большим.
    """
    # Проходим по всем файлам и папкам в указанной папке
    for foldername, subfolders, filenames in os.walk(folder):
        # получаем полный путь к файлу
        file_path - os.path.join(foldernamem, filename)

        try:
            # Получаем размер файла в байтах
            file_size = os.path.getsize(file_path)

            #проверяем, что размер файла больше указанного порога
            if file_size > size_threshold:
                # выводим абсолютный путь и размер файла
                print(f'Найден большой файл: {file_path} ({file_size / (1024 * 1024):.2f} MB)')
        except FileNotFoundError:
            print(f'Не удалось найти файл: {file_path}')
        except PermissionError:
            print(f'Нет доступа к файлу: {file_path}')

if __name__ == "__main__":
    folder_path = input("Введите путь к папке для поиска больших файлов: ")
    size_threshold_mb = input("Введите порог размера файла в МБ (например, 100): ")

    # преобразуем порог в байты
    size_threshold = int(size_threshold_mb) * 1024 * 1024

    findLargeFiles(folder_path, size_threshold)

# by chatGPT, write and edit - me


