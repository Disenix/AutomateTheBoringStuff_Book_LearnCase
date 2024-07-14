def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result
    else:
        result = 3 * number + 1
        print(result)
        return result

# Бесконечный цикл для постоянного запроса чисел у пользователя
while True:
    while True:
        try:
            user_input = int(input("Введите целое число (или введите 'exit' для выхода): "))
            break  # Если ввод корректен, выходим из цикла
        except ValueError:
            print("Ошибка: необходимо ввести целое число или 'exit' для завершения.")

    # Продолжаем вызывать collatz() до тех пор, пока не получим 1
    while user_input != 1:
        user_input = collatz(user_input)

    # Запрос на повторное выполнение или выход
    continue_input = input("Хотите ввести другое число? (да/нет): ").strip().lower()
    if continue_input != 'да':
        print("Программа завершена.")
        break
