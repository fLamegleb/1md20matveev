def func(x):
    if x % 5 == 0:
        return (f"Ваше число {asd} делится на 5")
    else:
        return (f"Ваше число {asd} не делится на 5")
asd = int(input("Введите число: "))
res = func(asd)
print(res)