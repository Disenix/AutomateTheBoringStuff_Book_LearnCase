#! python3
# downloadXckd.py - Загружает все комиксы XKCD.

import requests, os, bs4

url = 'https://xkcd.com' # Начальный url
os.makedirs('xkcd', exist_ok=True) # сохранить комиксы в ./xkcd
while not url.endswith('#'):
    # Загрузить страницу
    print('Загрузка страницы %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup =  bs4.BeautifulSoup(res.text, 'html.parser')

    # Находит URL-адрес изображения комикса.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Не удалось найти изображение комикса')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        # Загрузите изображение
        print('Загрузка изобрадения %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

        # Сохраняем изображение в ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Получаем URL кнопки Prev.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print('Done.')


