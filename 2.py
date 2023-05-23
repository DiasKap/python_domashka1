ticket_number = input("Введите номер билета (6 цифр): ")

# Проверяем, что введенный номер состоит из 6 цифр
if len(ticket_number) != 6 or not ticket_number.isdigit():
    print("Некорректный номер билета")
else:
    # Разбиваем номер на две половины
    first_half = ticket_number[:3]
    second_half = ticket_number[3:]

    # Считаем суммы цифр в каждой половине
    first_sum = sum(int(digit) for digit in first_half)
    second_sum = sum(int(digit) for digit in second_half)

    # Проверяем, является ли билет счастливым
    if first_sum == second_sum:
        print("Билет счастливый!")
    else:
        print("Билет несчастливый :(")