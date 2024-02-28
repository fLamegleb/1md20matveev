def asd(word):
    if 'ф' in word:
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово")
input = input("Введите слово: ")
asd(input)