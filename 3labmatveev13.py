def is_magic_date(date_str):
    try:
        day, month, year = map(int, date_str.split('.'))
        if day * month == year % 100:
            return True
        else:
            return False
    except ValueError:
        return False

input_date = input("Введите дату в формате 'дд.мм.гггг': ")
if is_magic_date(input_date):
    print("Введенная дата является магической.")
else:
    print("Введенная дата не является магической.")