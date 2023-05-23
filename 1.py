number = input("Введите 3-значное число: ")
if len(number) != 3:
    print("Ошибка! Введите 3-значное число.")
else:
    sum = int(number[0]) + int(number[1]) + int(number[2])
    print("Сумма цифр введенного числа:", sum)