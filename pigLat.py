# Aнглийский на Pig Latin
print('Введите английское сообщение для перевода на Pig Latin:')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatin = [] # Список слов на Pig Latin

for word in message.split():
    # Разделите небуквы в начале этого слова:
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue

    # Разделяем небуквы в конце этого слова:
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters = word[-1] + suffixNonLetters
        word = word[:-1]

    # запоминаем, было ли слово заглавными или заглавным
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower() # делаем слово строчным  для перевода
    # Pазделить согласные в начале этого слова:
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    # Добавить окончание Pig Latin к слову:
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

    # вернуть слово к верхнему или заглавному регистру:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # Добавить небуквы обратно в начало или конец слова
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

# Объединить все слова в одну строку:
print(' '.join(pigLatin))
