a = 1
b = ' '
while a == 1:
    c = input('Введите слово: ')
    b += (c+' ')
    if c == 'stop':
        print(b)