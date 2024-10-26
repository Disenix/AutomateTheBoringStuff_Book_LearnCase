#! python3
# threadedDownloadXkcd.py - загружает комиксы XKCD, используя несколько потоков

import requests, os, bs4, threading
os. makedirs('xkcd', exist_ok=True) # сохранить комиксы в ./xkcd

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Загрузить страницу
        print('Загрузка страницы https://xkcd.com/%s...' % (urlNumber))
        res = requests.get('https://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        # Найти URL-адрес изображения комикса
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Не удалось найти изображение комикса.')
        else:
            comicUrl = comicElem[0].get('src')
            # Загружаем изображения
            print('Загрузка изображения %s...' % (comicUrl))
            res = requests.get('https:' + comicUrl)
            res.raise_for_status()

            # сохраняем изображение в ./xkcd
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

# создает и запускает объекты Thread
downloadThreads = [] #Список всех объектов Thread
for i in range(0, 140, 10): # цикл 14 раз, создает 14 потоков
    start = i
    end = i + 9
    if start == 0:
        start = 1 # Комикса 0 нет, поэтому устанавливаем его в 1
    downloadThread = threading.Thread(target=downloadXkcd, args=(start, end))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Дождитесь завершения всех потоков
for downloadThread in downloadThreads:
    downloadThread.join()
    print('Done.')

