n = int(input("Введите количество строк шоколадки: "))
m = int(input("Введите количество столбцов шоколадки: "))
k = int(input("Введите количество долек, которые нужно отломить: "))

if k > n * m:
    print("Невозможно отломить такое количество долек")
elif k % n == 0 or k % m == 0:
    print("Можно отломить такое количество долек")
else:
    print("Невозможно отломить такое количество долек")