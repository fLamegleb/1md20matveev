def func():
    try:
        user_input = input("Введите число для деления 300: ")
        number = float(user_input)
        if number == 0:
            raise ZeroDivisionError("Деление на ноль недопустимо")
        result = 300 / number
        print(f"Результат деления 300 на {number} равен: {result}")
    except ValueError:
        print("Ошибка: Введено некорректное значение. Введите число.")
    except ZeroDivisionError as e:
        print(f"Ошибка: {e}")

func()
