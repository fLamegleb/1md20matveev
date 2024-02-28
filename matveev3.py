cvet1 = input ("Введите цвет:")
cvet2 = input ("Введите второй цвет:")
if cvet1 == "Красный" and cvet2 == "Синий" or  cvet2 == "Красный" and cvet1== "Синий":
    print("Фиолетовый")
elif cvet1 == "Красный" and cvet2 == "Желтый" or  cvet2 == "Красный" and cvet1== "Желтый":
    print("Оранжевый")
elif cvet1 == "Синий" and cvet2 == "Желтый" or  cvet2 == "Синий" and cvet1== "Желтый":
    print("Зеленый")
else:
    print("Ошибка!")