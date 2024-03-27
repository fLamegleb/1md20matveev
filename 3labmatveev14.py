def is_lucky_ticket(ticket_number):
    if len(ticket_number) % 2 != 0:
        return False
    half_length = len(ticket_number) // 2
    first_half = ticket_number[:half_length]
    second_half = ticket_number[half_length:]
    sum_first_half = sum(int(digit) for digit in first_half)
    sum_second_half = sum(int(digit) for digit in second_half)
    return sum_first_half == sum_second_half

ticket_number = input("Введите номер билета: ")
if is_lucky_ticket(ticket_number):
    print("Билет счастливый!")
else:
    print("Билет не счастливый.")