#! python3
# searchpypi.py - открывает несколько резкльтатов поиска

import requests, sys, webbrowser, bs4
print('Searching...') # отображать текст во время загрузки страницы результатов поиска
res = requests.get('http://google.com/search?q=' 'https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Извлекает ссылки на самые популярные результаты поиска.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# открывает вкладку браузера для каждого резульата.
linkElems = soup.select('.package-snippet')

numOpen = min(5,len(linkElems))

for i in range(numOpen):
    uelToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)

