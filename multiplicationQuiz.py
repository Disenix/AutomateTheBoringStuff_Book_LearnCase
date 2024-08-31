# multiplicationQuiz.py - проект: Тест по умножению

import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
    # Выберите два случайных числа:
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    promt = '#%s: %sx %s = ' % (questionNumber, num1, num2)

    try:
        # Правильные ответы обрабатываются allowRegexes.
        # Неправильные ответы обрабатываются blockRegexes с пользовательским сообщением.
        pyip.inputStr(promt, allowRegexes=['^%s$' % (num1 * num2)],
                             blockRegexes=[('.*', 'Incorrect!')],
                             timeout=8, limit=3)

    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        # Этот блок выполняется, если в блоке  try не было вызвано никаких исключений.
        print('Correct!')
        correctAnswers += 1
    time.sleep(1) # Короткая пауза, чтобы пользователь мог увидеть результат.
print('Score: %s / %s' % (correctAnswers, numberOfQuestions))

