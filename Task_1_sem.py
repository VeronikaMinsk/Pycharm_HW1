# Константы для проверки високосности
divisor_4 = 4
divisor_100 = 100
divisor_400 = 400

year = int(input("Введите год: "))

if year < 0:
    print("Введено некорректное значение. Год должен быть положительным числом.")
else:
    if year % divisor_400 == 0:
        print(year, "год - високосный")
    elif year % divisor_100 == 0:
        print(year, "год - невисокосный")
    elif year % divisor_4 == 0:
        print(year, "год - високосный")
    else:
        print(year, "год - невисокосный")