import random

correct = 0
max = 3

while max > 0:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    a = f"{num1} + {num2} = "

    answer = int(input(a))

    if answer == num1 + num2:
        print("Правильно!")
        correct += 1
    else:
        print("Ответ неверный")
        max -= 1

print(f"Игра окончена. Правильных ответов: {correct}")