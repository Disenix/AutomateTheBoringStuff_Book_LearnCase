def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Символ должен быть строкой из одного символа.')
    if width <= 2:
        raise Exception('Ширина должна быть больше 2.')
    if height <= 2:
        raise Exception('Высота должна быть больше 2.')

    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

for sym, w, h in (('*', 4, 4), ('0', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('Произошло исключение: ' + str(err))

