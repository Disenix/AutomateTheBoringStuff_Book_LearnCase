import time
def calcProd():
    #Вычиcлить произведение первых 100 000 чисел
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
print('Результат имеет длину %s цифр.' % (len(str(prod))))
print('Вычисление заняло %s секунд.' % (endTime - startTime))
