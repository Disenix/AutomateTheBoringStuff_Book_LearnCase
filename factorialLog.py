import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Начало программы')

def factorial(n):
    logging.debug('Начало факториала(%s%%)' % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i равно ' + str(i) + ', total равно ' + str(total))
    logging.debug('Конец факториала(%s%%)' % (n))
    return total

print(factorial(5))
logging.debug('Конец программы')
